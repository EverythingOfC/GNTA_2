import pandas as pd
import requests
import json
import datetime
import pandas as pd


def weather_check():
    service_key = '434566486e746b66343949565a6a53'
    url = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/fcltOpenInfo_GN/1/20/1168000000"

    response = requests.get(url)

    r_dict = json.loads(response.text)

    r_dict = r_dict['fcltOpenInfo_GN']['row'] # 필요한 행만 담음.

    print(r_dict)
    for i in r_dict:
        print(i['FCLT_NM'])

        print("하하")




# 내가 나를(함수) 호출할때 이 파일이 __main__임.
if __name__ =='__main__':
    temp = dict()
    temp = weather_check()
    print(temp)