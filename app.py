import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="WWII Battles Map", layout="wide")

st.title("🌍 2차 세계대전 주요 전투 지도")
st.markdown(
    """
왼쪽 지도에서 **이모지 마커**를 클릭하면  
오른쪽에서 해당 전투의 **정보와 사진**이 보여집니다.
"""
)

# 2차 세계대전 주요 전투 데이터
battles = [
    {
        "id": "britain",
        "name": "브리튼 전투 (Battle of Britain)",
        "period": "1940년 7월 ~ 10월",
        "theater": "서부전선 · 공중전",
        "lat": 51.5074,
        "lon": -0.1278,
        "emoji": "✈️",
        "summary": "독일 공군 루프트바페가 영국 본토의 제공권을 장악하기 위해 벌인 공중전. 영국 공군의 방어 성공으로 독일의 영국 침공 계획(‘바다사자 작전’)이 좌절되었다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/IWM-CH4222_Battle_of_Britain.jpg/640px-IWM-CH4222_Battle_of_Britain.jpg",
    },
    {
        "id": "pearl_harbor",
        "name": "진주만 공습 (Attack on Pearl Harbor)",
        "period": "1941년 12월 7일",
        "theater": "태평양전선 · 해공전",
        "lat": 21.3667,
        "lon": -157.9333,
        "emoji": "🚢",
        "summary": "일본 해군이 미국 하와이 진주만을 기습 공격하여 미국 태평양 함대에 큰 손실을 입혔다. 이 공격을 계기로 미국이 본격적으로 2차 세계대전에 참전하게 된다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/USS_Arizona_burning-Pearl_Harbor.jpg/640px-USS_Arizona_burning-Pearl_Harbor.jpg",
    },
    {
        "id": "stalingrad",
        "name": "스탈린그라드 전투 (Battle of Stalingrad)",
        "period": "1942년 8월 ~ 1943년 2월",
        "theater": "동부전선 · 시가전",
        "lat": 48.7080,
        "lon": 44.5140,
        "emoji": "💣",
        "summary": "독일군과 소련군이 볼가 강 유역의 산업 도시 스탈린그라드를 두고 벌인 치열한 전투. 독일 제6군이 포위·항복하면서 독일의 동부전선 공세가 꺾이는 전환점이 되었다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Bundesarchiv_Bild_183-R77767%2C_Stalingrad%2C_Ruinen%2C_Roten_Armee.jpg/640px-Bundesarchiv_Bild_183-R77767%2C_Stalingrad%2C_Ruinen%2C_Roten_Armee.jpg",
    },
    {
        "id": "el_alamein",
        "name": "엘 알라메인 전투 (Second Battle of El Alamein)",
        "period": "1942년 10월 ~ 11월",
        "theater": "북아프리카 전선",
        "lat": 30.8330,
        "lon": 28.9550,
        "emoji": "🪖",
        "summary": "이집트 엘 알라메인에서 영국 몽고메리 장군이 지휘하는 연합군이 롬멜이 이끄는 추축군을 격파하였다. 북아프리카에서 추축군의 후퇴가 시작되는 계기가 되었다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/British_tank_advance_El_Alamein_1942.jpg/640px-British_tank_advance_El_Alamein_1942.jpg",
    },
    {
        "id": "midway",
        "name": "미드웨이 해전 (Battle of Midway)",
        "period": "1942년 6월 4일 ~ 7일",
        "theater": "태평양전선 · 해전",
        "lat": 28.2000,
        "lon": -177.3500,
        "emoji": "⚓",
        "summary": "미국과 일본 사이에 벌어진 항공모함 중심의 대규모 해전. 미국이 일본 항공모함 4척을 격침시키며 태평양에서 전략적 주도권을 확보했다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Battle_of_Midway_USS_Yorktown_under_attack.jpg/640px-Battle_of_Midway_USS_Yorktown_under_attack.jpg",
    },
    {
        "id": "normandy",
        "name": "노르망디 상륙작전 (D-Day, Operation Overlord)",
        "period": "1944년 6월 6일",
        "theater": "서부전선 · 상륙작전",
        "lat": 49.4144,
        "lon": -0.8769,
        "emoji": "🪖",
        "summary": "연합군이 프랑스 노르망디 해안에 대규모 상륙작전을 감행하여 서유럽 탈환의 교두보를 확보했다. 서부전선 개막의 상징적인 작전이다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Omaha_Beach_Landing_Craft_Approach.jpg/640px-Omaha_Beach_Landing_Craft_Approach.jpg",
    },
    {
        "id": "kursk",
        "name": "쿠르스크 전투 (Battle of Kursk)",
        "period": "1943년 7월 ~ 8월",
        "theater": "동부전선 · 기갑전",
        "lat": 51.7300,
        "lon": 36.1939,
        "emoji": "🚜",
        "summary": "역사상 최대 규모의 전차전으로 알려진 전투. 소련군이 독일의 기갑 공세를 저지하고 반격에 성공하여 동부전선에서 주도권을 장악했다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Bundesarchiv_Bild_101I-218-0504-36%2C_Russland%2C_Panzer_VI_%28Tiger_I%29.jpg/640px-Bundesarchiv_Bild_101I-218-0504-36%2C_Russland%2C_Panzer_VI_%28Tiger_I%29.jpg",
    },
    {
        "id": "guadalcanal",
        "name": "과달카날 전투 (Guadalcanal Campaign)",
        "period": "1942년 8월 ~ 1943년 2월",
        "theater": "태평양전선 · 섬 전투",
        "lat": -9.6430,
        "lon": 160.1560,
        "emoji": "🌴",
        "summary": "솔로몬 제도 과달카날 섬을 둘러싸고 미·일 양국이 벌인 장기 전투. 미군이 비행장을 확보하고 일본군을 축출하면서 태평양 전쟁의 흐름을 바꾸었다.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Guadalcanal_US_Marines_landing_1942.jpg/640px-Guadalcanal_US_Marines_landing_1942.jpg",
    },
    {
        "id": "moscow",
        "name": "모스크바 공방전 (Battle of Moscow)",
        "period": "1941년 10월 ~ 1942년 1월",
        "theater": "동부전선",
        "lat": 55.7558,
        "lon": 37.6173,
        "emoji": "❄️",
        "summary": "독일군이 소련의 수도 모스크바를 점령하려 했으나, 혹한과 소련군의 반
