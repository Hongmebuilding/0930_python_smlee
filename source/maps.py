import folium
from folium import Marker
import webbrowser

import pandas as pd
import csv



# 1. excel에서 pd를 이용해 데이터 추출
def find_hospital(sido_cd='서울', typ_cd='상급종합'):
    df_init = pd.read_csv('1. 병원정보서비스 2021.6.csv', encoding='cp949')
#    print('*' * 40)
#    print(df_init.head(30))

    # 필요한 컬럼만 별도 저장
    # 가로 or 세로선에서 보고 싶은 것만 ''
    df_data = df_init[['요양기관명','종별코드명','시도코드명','주소','총의사수','x좌표','y좌표']]
#    print(df_data.head())

#    df_data2 = df_data[df_data.시도코드명 == '서울']
#    df_data3 = df_data2[df_data2.종별코드명 == '상급종합']
    df_data2 = df_data[df_data.시도코드명 == sido_cd]
    df_data3 = df_data2[df_data2.종별코드명 == typ_cd].reset_index(drop=True)

    print(df_data3)

    # folium setting
    # default_location = [37.541, 126.986]  # 서울 대표 좌표
    # default_zoom = 12
    # hmap = folium.Map(location=default_location,
    #                   control_scale=True,
    #                   zoom_start=default_zoom)

# 2. 지도에 데이터 넣기(folium)
    for row in df_data3.itertuples():
        idx, hptl_name, typ_cd, sido_cd, addr, docnum, lng, lat = row
        print(idx, hptl_name, lng, lat)

        if idx == 0:
            default_location = [lat, lng]  # 검색 결과 대표 좌표
            default_zoom = 12
            hmap = folium.Map(location=default_location,
                              control_scale=True,
                              zoom_start=default_zoom)

        iframe = hptl_name + '(' + str(docnum) + ')' + '<br>' + addr
        popup = folium.Popup(iframe, min_width=100, max_width=300)  # 말풍선
        Marker(location=[lat, lng],
               tooltip=hptl_name,
               popup=popup).add_to(hmap)

    # html로 저장
    hmap.save('hospital_info.html')

    # 자동으로 web browser 띄우기
    webbrowser.open('hospital_info.html')


