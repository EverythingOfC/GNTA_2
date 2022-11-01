import requests
import json
import datetime

def weather_check():
    weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

    #본인 일반 인증키 => encoding 추천
    service_key = "LHkxTfpgVj4eYu0jt6bsdU%2FKKtTcJ4572LI609b9F7fjyZkURhLGVv6rjWrj3EWLWpfiSvvbYgj8aWiovnSWwg%3D%3D"
    # base_date = datetime.datetime.today().strftime("%Y%m%d") #20210628
    base_date = '20221010'
    base_time = "1100"
    nx = '60'
    ny = '126' #용산구

    # http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst
    # ?serviceKey=인증키&numOfRows=10&pageNo=1
    # &base_date=20210628&base_time=0500&nx=55&ny=127, dataType

    payload = "serviceKey=" + service_key + "&" +\
                "numOfRows=10&pageNo=1" + "&" +\
                "dataType=json" + "&" +\
                "base_date=" + base_date + "&" +\
                "base_time=" + base_time + "&" +\
                "nx=" + nx + "&" + \
                "ny=" + ny

    weather = dict()
    weather['date'] = base_date
    pty_code = {'0':'없음', '1':'비', '2':'비/눈', '3':'눈', '4':'소나기'}
    # 값요청
    res = requests.get(weather_url + payload)
    # result = res.json()
    try:
        result = res.json().get('response').get('body').get('items')
        # print(result)
        for item in result['item']:
            # print(item)
            # print("*")

            # 기온
            if item['category'] == 'TMP' :
                weather['tmp'] = item['fcstValue']

            # 강수 상태
            if item['category'] == 'PTY':
                weather['code'] = item['fcstValue']
                weather['state'] = pty_code[item['fcstValue']]
    except:
        print("날씨 정보 가져오기 실패", res.text)

    return weather

# 내가 나를(함수) 호출할때 이 파일이 __main__임.
if __name__ =='__main__':
    temp = dict()
    temp = weather_check()
    print(temp)