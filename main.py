import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="⚔️ 2차 세계대전 주요 전투", layout="wide")

# 전투 데이터
battles = {
    "진주만": {
        "coords": [21.3099, -157.8581],
        "emoji": "💣",
        "date": "1941년 12월 7일",
        "description": """
        **일본의 기습 공격**
        
        일본 제국 해군이 미국 하와이 진주만 해군 기지를 기습 공격한 사건입니다. 
        이 공격으로 미국이 2차 세계대전에 참전하게 되었습니다.
        
        • 공격 시간: 오전 7시 48분
        • 일본 항공모함 6척에서 350여 대의 항공기 출격
        • 미군 전함 8척 파괴, 2,403명 사망
        • 미국의 대일 선전포고로 이어짐
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/USS_Arizona_during_the_Japanese_surprise_air_attack_on_the_American_pacific_fleet%2C_7_December_1941._-_NARA_-_195617_-_Edit.jpg/800px-USS_Arizona_during_the_Japanese_surprise_air_attack_on_the_American_pacific_fleet%2C_7_December_1941._-_NARA_-_195617_-_Edit.jpg"
    },
    "스탈린그라드": {
        "coords": [48.7080, 44.5133],
        "emoji": "🏭",
        "date": "1942년 8월 - 1943년 2월",
        "description": """
        **전쟁의 전환점**
        
        나치 독일과 소련 사이의 치열한 공방전으로, 2차 세계대전의 전환점이 된 전투입니다.
        
        • 기간: 약 6개월간의 격전
        • 소련의 승리로 동부전선 전세 역전
        • 양측 합계 약 200만 명의 사상자 발생
        • 독일 6군 전멸, 파울루스 원수 항복
        • 시가전의 참혹함으로 유명
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/RIAN_archive_602161_Center_of_Stalingrad_after_liberation.jpg/800px-RIAN_archive_602161_Center_of_Stalingrad_after_liberation.jpg"
    },
    "노르망디 상륙작전": {
        "coords": [49.3964, -0.8633],
        "emoji": "🚢",
        "date": "1944년 6월 6일 (D-Day)",
        "description": """
        **역사상 최대의 상륙작전**
        
        연합군이 프랑스 노르망디 해안에 상륙하여 서부전선을 개설한 작전입니다.
        
        • 작전명: 오버로드 작전 (Operation Overlord)
        • 참가 병력: 약 15만 6천명
        • 상륙 함정: 5,000척 이상
        • 항공기: 11,000대 지원
        • 유타, 오마하, 골드, 주노, 소드 5개 해안 동시 상륙
        • 유럽 해방의 시작점
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Into_the_Jaws_of_Death_23-0455M_edit.jpg/800px-Into_the_Jaws_of_Death_23-0455M_edit.jpg"
    },
    "미드웨이": {
        "coords": [28.2072, -177.3735],
        "emoji": "✈️",
        "date": "1942년 6월 4-7일",
        "description": """
        **태평양 전쟁의 전환점**
        
        미국 해군이 일본 해군을 격파한 결정적 해전입니다.
        
        • 일본 항공모함 4척 격침 (아카기, 카가, 소류, 히류)
        • 미국 항공모함 요크타운 1척 손실
        • 일본 해군의 전력 약화
        • 태평양 전쟁에서 미군이 주도권 장악
        • 항공모함 중심 해전의 새로운 패러다임
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Hiryu_burning.jpg/800px-Hiryu_burning.jpg"
    },
    "쿠르스크": {
        "coords": [51.7373, 36.1873],
        "emoji": "🛡️",
        "date": "1943년 7-8월",
        "description": """
        **역사상 최대의 전차전**
        
        독일과 소련 사이의 대규모 기갑전으로, 역사상 최대 규모의 전차전입니다.
        
        • 참가 전차: 양측 합계 약 6,000대
        • 독일의 마지막 대규모 공세
        • 소련의 방어와 반격 성공
        • 티거, 판터 등 신형 독일 전차 투입
        • 동부전선에서 소련의 확실한 우위 확립
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Bundesarchiv_Bild_101I-022-2926-12%2C_Russland%2C_Panzer_VI_%28Tiger_I%29_in_Fahrt.jpg/800px-Bundesarchiv_Bild_101I-022-2926-12%2C_Russland%2C_Panzer_VI_%28Tiger_I%29_in_Fahrt.jpg"
    },
    "베를린": {
        "coords": [52.5200, 13.4050],
        "emoji": "🏛️",
        "date": "1945년 4월 16일 - 5월 2일",
        "description": """
        **유럽 전쟁의 종결**
        
        소련군의 베를린 공략으로 나치 독일이 항복한 최종 전투입니다.
        
        • 소련군 약 250만 명 투입
        • 시가전으로 수많은 건물 파괴
        • 4월 30일 히틀러 자살
        • 5월 2일 베를린 함락
        • 5월 8일 독일 무조건 항복 (VE-Day)
        • 유럽 전쟁 종료
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Reichstag_after_the_allied_bombing_of_Berlin.jpg/800px-Reichstag_after_the_allied_bombing_of_Berlin.jpg"
    },
    "이오지마": {
        "coords": [24.7544, 141.3197],
        "emoji": "⛰️",
        "date": "1945년 2-3월",
        "description": """
        **치열한 섬 전투**
        
        미군이 일본 본토 폭격을 위한 중간 기지를 확보하기 위해 벌인 전투입니다.
        
        • 36일간의 치열한 전투
        • 수리바치산 정상에 성조기 게양 (유명한 사진)
        • 일본군 2만여 명 중 대부분 전사
        • 미군 사상자 약 2만 6천명
        • 동굴과 갱도를 활용한 일본군의 완강한 저항
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/WW2_Iwo_Jima_flag_raising.jpg/800px-WW2_Iwo_Jima_flag_raising.jpg"
    },
    "엘 알라메인": {
        "coords": [30.8296, 28.9519],
        "emoji": "🏜️",
        "date": "1942년 10-11월",
        "description": """
        **사막의 여우를 막아내다**
        
        북아프리카에서 영국군이 롬멜의 독일 아프리카 군단을 격파한 전투입니다.
        
        • 몽고메리 장군의 영국 8군 vs 롬멜 원수
        • 사막 전투의 전환점
        • 처칠: "전쟁의 끝은 아니지만, 시작의 끝"
        • 북아프리카에서 추축국 세력 약화
        • 연합군의 반격 시작
        """,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/The_British_Army_in_North_Africa_1942_E18874.jpg/800px-The_British_Army_in_North_Africa_1942_E18874.jpg"
    }
}

# 타이틀
st.title("⚔️ 2차 세계대전 주요 전투 지도")
st.markdown("## 📍 지도의 이모지를 클릭하여 전투 정보를 확인하세요!")

# 2개 컬럼 생성
col1, col2 = st.columns([2, 1])

with col1:
    # Folium 지도 생성
    m = folium.Map(
        location=[30, 20],
        zoom_start=2,
        tiles="OpenStreetMap"
    )
    
    # 각 전투를 마커로 추가
    for battle_name, battle_info in battles.items():
        folium.Marker(
            location=battle_info["coords"],
            popup=folium.Popup(f"{battle_info['emoji']} {battle_name}", max_width=200),
            tooltip=f"{battle_info['emoji']} {battle_name}",
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 30px; cursor: pointer;">
                    {battle_info['emoji']}
                </div>
            """)
        ).add_to(m)
    
    # 지도 표시 및 클릭 이벤트 받기
    map_data = st_folium(m, width=None, height=600, returned_objects=["last_object_clicked"])

with col2:
    st.markdown("### 📖 전투 정보")
    
    # 클릭된 마커가 있으면 해당 정보 표시
    if map_data and map_data.get("last_object_clicked"):
        clicked_coords = map_data["last_object_clicked"]
        clicked_lat = clicked_coords["lat"]
        clicked_lng = clicked_coords["lng"]
        
        # 클릭된 좌표와 일치하는 전투 찾기
        selected_battle = None
        for battle_name, battle_info in battles.items():
            if (abs(battle_info["coords"][0] - clicked_lat) < 0.1 and 
                abs(battle_info["coords"][1] - clicked_lng) < 0.1):
                selected_battle = battle_name
                break
        
        if selected_battle:
            battle_info = battles[selected_battle]
            
            # 전투 정보 표시
            st.markdown(f"## {battle_info['emoji']} {selected_battle}")
            st.markdown(f"**📅 {battle_info['date']}**")
            st.markdown("---")
            st.markdown(battle_info['description'])
            st.markdown("---")
            st.markdown("**📷 전투 사진**")
            st.image(battle_info['image'], use_container_width=True)
    else:
        # 초기 화면 - 안내 메시지
        st.info("👈 왼쪽 지도에서 이모지를 클릭하면 전투 정보가 여기에 표시됩니다!")
        st.markdown("---")
        st.markdown("### 📋 수록된 전투")
        for battle_name, battle_info in battles.items():
            st.markdown(f"{battle_info['emoji']} **{battle_name}** - {battle_info['date']}")

# 하단 정보
st.markdown("---")
st.markdown("💡 **Tip**: 지도를 확대/축소하고 드래그하여 다양한 전투 위치를 확인할 수 있습니다!")
