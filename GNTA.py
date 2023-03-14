import requests
import json
import datetime

def weather_check():
    KEY = "6c5458706a6873683935514d4a6252"
    url = "http://openapi.seoul.go.kr:8088/" + KEY + "/xml/VolInfo/1/15/A-01/20210313/12/"

    response = requests.get(url).content.decode('utf-8')
    print(response)

# 내가 나를(함수) 호출할때 이 파일이 __main__임.
if __name__ =='__main__':
    temp = dict()
    temp = weather_check()
    print(temp)




