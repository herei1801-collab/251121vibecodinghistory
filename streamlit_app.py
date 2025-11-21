import streamlit as st
import folium
from streamlit.components.v1 import html

# ----------------------------
# 데이터: 2차 세계대전 주요 전투
# ----------------------------
BATTLES = [
    {
        "name": "Battle of Britain",
        "year": "1940",
        "lat": 51.5074,
        "lon": -0.1278,
        "front": "Western Front",
        "emoji": "✈️🇬🇧",
        "image_url": "https://via.placeholder.com/300x200?text=Battle+of+Britain",
        "description": (
            "영국 상공에서 벌어진 독일 공군과 영국 공군의 대규모 공중전. "
            "독일의 영국 침공 계획(해사사자 작전)을 좌절시킨 결정적인 전투였다."
        ),
    },
    {
        "name": "Battle of Stalingrad",
        "year": "1942–1943",
        "lat": 48.7080,
        "lon": 44.5133,
        "front": "Eastern Front",
        "emoji": "🏙️🔥",
        "image_url": "https://via.placeholder.com/300x200?text=Stalingrad",
        "description": (
            "소련 스탈린그라드에서 벌어진 동부전선의 최대 격전. "
            "독일군이 포위·섬멸되면서 전쟁의 흐름이 소련 쪽으로 기울게 되었다."
        ),
    },
    {
        "name": "Battle of Midway",
        "year": "1942",
        "lat": 28.2000,
        "lon": -177.3500,
        "front": "Pacific War",
        "emoji": "⚓️✈️",
        "image_url": "https://via.placeholder.com/300x200?text=Midway",
        "description": (
            "태평양 한가운데 미드웨이 해역에서 벌어진 미·일 해전. "
            "미국이 일본 항공모함 4척을 격침시키며 태평양 전쟁의 주도권을 잡았다."
        ),
    },
    {
        "name": "Second Battle of El Alamein",
        "year": "1942",
        "lat": 30.8381,
        "lon": 28.9550,
        "front": "North Africa",
        "emoji": "🏜️🚚",
        "image_url": "https://via.placeholder.com/300x200?text=El+Alamein",
        "description": (
            "이집트 엘알라메인에서 벌어진 북아프리카 전선의 결정적 승부. "
            "연합군 몽고메리 장군이 롬멜의 독일-이탈리아군을 격퇴했다."
        ),
    },
    {
        "name": "D-Day (Normandy Landings)",
        "year": "1944",
        "lat": 49.3323,
        "lon": -0.6210,
        "front": "Western Front",
        "emoji": "🌊🪖",
        "image_url": "https://via.placeholder.com/300x200?text=Normandy",
        "description": (
            "프랑스 노르망디 해안에 상륙한 연합군의 대규모 작전. "
            "서부 전선을 여는 데 성공하며 나치 독일을 압박하는 계기가 되었다."
        ),
    },
    {
        "name": "Battle of the Bulge",
        "year": "1944–1945",
        "lat": 50.0000,
        "lon": 6.0000,
        "front": "Western Front",
        "emoji": "🌲❄️",
        "image_url": "https://via.placeholder.com/300x200?text=Bulge",
        "description": (
            "벨기에와 룩셈부르크 일대 아르덴 숲에서 벌어진 독일의 최후 반격 작전. "
            "초기에는 독일이 우세했지만, 결국 연합군이 방어에 성공했다."
        ),
    },
    {
        "name": "Battle of Kursk",
        "year": "1943",
        "lat": 51.7300,
        "lon": 36.1939,
        "front": "Eastern Front",
        "emoji": "🛡️🚜",
        "image_url": "https://via.placeholder.com/300x200?text=Kursk",
        "description": (
            "소련 쿠르스크 돌출부에서 벌어진 역사상 최대 규모의 전차전. "
            "소련군이 독일의 공격을 격퇴하며 동부전선의 주도권을 완전히 장악했다."
        ),
    },
    {
        "name": "Battle of Berlin",
        "year": "1945",
        "lat": 52.5200,
        "lon": 13.4050,
        "front": "Eastern Front",
        "emoji": "🏰💥",
        "image_url": "https://via.placeholder.com/300x200?text=Berlin",
        "description": (
            "소련군이 독일 수도 베를린을 포위·공격한 최후 결전. "
            "히틀러의 자살과 독일의 항복으로 유럽 전선이 종결되었다."
        ),
    },
    {
        "name": "Attack on Pearl Harbor",
        "year": "1941",
        "lat": 21.3667,
        "lon": -157.9333,
        "front": "Pacific War",
        "emoji": "🌺💣",
        "image_url": "https://via.placeholder.com/300x200?text=Pearl+Harbor",
        "description": (
            "일본 해군이 하와이 진주만의 미 해군 기지를 기습 공격한 사건. "
            "이를 계기로 미국이 공식적으로 2차 세계대전에 참전했다."
        ),
    },
    {
        "name": "Guadalcanal Campaign",
        "year": "1942–1943",
        "lat": -9.4300,
        "lon": 160.0500,
        "front": "Pacific War",
        "emoji": "🌴⚔️",
        "image_url": "https://via.placeholder.com/300x200?text=Guadalcanal",
        "description": (
            "솔로몬 제도 과달카날 섬을 둘러싼 미·일 간의 공중·해상·지상전. "
            "미군이 승리하여 일본의 남태평양 진출을 저지했다."
        ),
    },
    {
        "name": "Battle of Iwo Jima",
        "year": "1945",
        "lat": 24.7867,
        "lon": 141.3189,
        "front": "Pacific War",
        "emoji": "🏝️🇺🇸",
        "image_url": "https://via.placeholder.com/300x200?text=Iwo+Jima",
        "description": (
            "일본 이오지마 섬에서 벌어진 격렬한 전투. "
            "미군이 섬을 점령하여 일본 본토 폭격을 위한 전진 기지를 확보했다."
        ),
    },
    {
        "name": "Battle of Okinawa",
        "year": "1945",
        "lat": 26.3344,
        "lon": 127.8056,
        "front": "Pacific War",
        "emoji": "🌧️💣",
        "image_url": "https://via.placeholder.com/300x200?text=Okinawa",
        "description": (
            "일본 오키나와 섬에서 벌어진 태평양 전쟁 최대 규모의 상륙전. "
            "치열한 전투와 민간인 피해가 이어지며 전쟁의 참혹함을 보여주었다."
        ),
    },
]

# ----------------------------
# 스트림릿 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="🌍 2차 세계대전 주요 전투 지도",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 2차 세계대전 주요 전투 지도 앱")
st.markdown(
    """
**folium**과 **Streamlit**을 이용해 2차 세계대전의 주요 전투들을 한눈에 볼 수 있는 인터랙티브 지도입니다.  

각 전투 마커를 클릭하면  
📷 전투 관련 이미지(플레이스홀더)와  
📝 간단한 설명을 확인할 수 있습니다.
    """
)

st.markdown("---")

# ----------------------------
# 사이드바 필터
# ----------------------------
st.sidebar.header("⚙️ 전투 필터")
fronts = sorted({b["front"] for b in BATTLES})
selected_fronts = st.sidebar.multiselect(
    "전선(Front)를 선택하세요:",
    options=fronts,
    default=fronts,
    help="보고 싶은 전선을 선택해 전투 마커를 필터링할 수 있습니다.",
)

# 필터 적용
filtered_battles = [b for b in BATTLES if b["front"] in selected_fronts]

st.sidebar.markdown("------")
st.sidebar.markdown("🪖 **표시 중인 전투 수:** **{}** 개".format(len(filtered_battles)))
st.sidebar.markdown("💡 마커를 클릭해 사진과 설명을 확인해 보세요!")

# ----------------------------
# folium 지도 생성
# ----------------------------
# 전세계가 보이도록 대략적인 중심과 줌 레벨 설정
m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB positron")

for battle in filtered_battles:
    popup_html = f"""
    <div style="width:250px;">
        <h4>{battle['emoji']} {battle['name']} ({battle['year']})</h4>
        <img src="{battle['image_url']}" alt="{battle['name']}" 
             style="width:100%; border-radius:8px; margin-bottom:8px;">
        <p style="font-size:13px; line-height:1.4;">
            {battle['description']}
        </p>
        <p style="font-size:12px; color:gray; margin-top:4px;">
            🌐 Front: {battle['front']}
        </p>
    </div>
    """
    iframe = folium.IFrame(html=popup_html, width=260, height=260)
    popup = folium.Popup(iframe, max_width=260)

    folium.Marker(
        location=[battle["lat"], battle["lon"]],
        popup=popup,
        tooltip=f"{battle['emoji']} {battle['name']}",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

# ----------------------------
# Streamlit
