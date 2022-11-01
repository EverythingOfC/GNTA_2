import pandas as pd
import requests
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',60)


def society_welfare():
    service_key = '434566486e746b66343949565a6a53'
    url = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/fcltOpenInfo_GN/1/52/1168000000" # 총 52개의 데이터가 있다.

    response = requests.get(url)

    r_dict = json.loads(response.text) # json파일을 불러온다.
    r_dict = r_dict['fcltOpenInfo_GN']['row'] # 필요한 행만 담음.
    print(r_dict)


    df = pd.DataFrame(r_dict) # 데이터프레임으로 변환
    df.drop(['JRSD_SGG_SE','FCLT_CD','JRSD_SGG_NM','JRSD_SGG_CD'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
    df.columns = ['시설명','시설종류','시설종류상세','시설장명','시설주소'] # 칼럼명을 알아보기 쉽게 바꿈.


    df['시설종류'] = df['시설종류'].str.replace("\(노인\)","") # 중복된 단어 제거
    df['시설종류'] = df['시설종류'].str.replace("\(소규모\)","") # 중복된 단어 제거
    df['시설종류'] = df['시설종류'].str.replace("\(장애인\)","") # 중복된 단어 제거

    result = df['시설종류상세'].value_counts()

    x = list(result.index)
    y = list(result.values)

    plt.rc('font', family='Malgun Gothic')
    plt.style.use('ggplot')
    plt.figure(figsize=(15,8))

    print(result)

    result = plt.bar(result.index,result.values,width=0.7,color='yellowgreen')

    for rect in result:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=15)

    plt.title('강남구 시설종류별 복지시설 개수',size=25)
    plt.xticks(size=10,rotation=0,weight='bold')
    plt.xlabel('시설종류',size=15)
    plt.ylabel('개수',size=15)
    plt.legend(fontsize=15)
    plt.show()

# 내가 나를(함수) 호출할때 이 파일이 __main__임.
if __name__ =='__main__':

    society_welfare()