import pandas as pd
import requests
import json

def society_welfare(): # 동작구 사회복지시설 데이터를 정제

    service_key = '425753564e746b6636305947536953'
    url = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/fcltOpenInfo_GN/1/113/1159000000" # 총 113개 데이터

    response = requests.get(url)

    r_dict = json.loads(response.text) # json파일을 불러온다.
    r_dict = r_dict['fcltOpenInfo_GN']['row'] # 필요한 행만 담음.

    df = pd.DataFrame(r_dict) # 데이터프레임으로 변환
    df.drop(['JRSD_SGG_SE','FCLT_CD','JRSD_SGG_NM','JRSD_SGG_CD'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
    df.columns = ['시설명','시설종류','시설종류상세','시설장명','시설주소'] # 칼럼명을 알아보기 쉽게 바꿈.

    df['시설종류'] = df['시설종류'].str.replace("\(노인\)","") # 중복된 단어 제거
    df['시설종류'] = df['시설종류'].str.replace("\(소규모\)","") # 중복된 단어 제거
    df['시설종류'] = df['시설종류'].str.replace("\(장애인\)","") # 중복된 단어 제거
    df['시설종류상세'] = df['시설종류상세'].str.replace('자활시설','재활시설') # 오타 제거

    result = df['시설종류상세'].value_counts()  # 각 시설종류의 개수 리턴

    return result





