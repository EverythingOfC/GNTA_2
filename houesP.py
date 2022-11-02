import pandas as pd
import requests
import json
import datetime
import pandas as pd
import matplotlib.pyplot as plt

service_key = '43686c666373756e38316b4d697778' #Encoding인증키
year='2021'

url1 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/1/1000/"+year+"/11680/강남구/" #한번에 1000건씩밖에 안 된다...ㅠㅠ
url2 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/1001/2000/"+year+"/11680/강남구/"
url3 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/2001/3000/"+year+"/11680/강남구/"
url4 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/3001/4000/"+year+"/11680/강남구/"
url5 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/4001/5000/"+year+"/11680/강남구/"
url6 = "http://openapi.seoul.go.kr:8088/"+service_key+"/json/tbLnOpendataRtmsV/5001/5924/"+year+"/11680/강남구/"

# url = "http://openapi.seoul.go.kr:8088/" +service_key+ "/json/tbLnOpendataRtmsV/1/5/2022/11500/강서구/10500/일반/0758/0002/마곡일성트루엘플래닛/오피스텔"
#총 5924

res1 = requests.get(url1) #json 파일 형식으로 받아오게 돼어 있음
res2 = requests.get(url2)
res3 = requests.get(url3)
res4 = requests.get(url4)
res5 = requests.get(url5)
res6 = requests.get(url6)
# res = requests.get(url).text
# res = requests.get(url).content

# print(res1)
# print(type(res1))
# print('')
res1_1 = json.loads(res1.text) #딕셔너리네
res2_1 = json.loads(res2.text)
res3_1 = json.loads(res3.text)
res4_1 = json.loads(res4.text)
res5_1 = json.loads(res5.text)
res6_1 = json.loads(res6.text)

# print(res1_1)
# print(res2_1)
# print(type(res1_1))
# print('')

res1_2 = res1_1['tbLnOpendataRtmsV']['row']
res2_2 = res2_1['tbLnOpendataRtmsV']['row']
res3_2 = res3_1['tbLnOpendataRtmsV']['row']
res4_2 = res4_1['tbLnOpendataRtmsV']['row']
res5_2 = res5_1['tbLnOpendataRtmsV']['row']
res6_2 = res6_1['tbLnOpendataRtmsV']['row']

df1 = pd.DataFrame(res1_2)
df2 = pd.DataFrame(res2_2)
df3 = pd.DataFrame(res3_2)
df4 = pd.DataFrame(res4_2)
df5 = pd.DataFrame(res5_2)
df6 = pd.DataFrame(res6_2)


df1.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df1.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']
df2.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df2.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']
df3.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df3.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']
df4.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df4.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']
df5.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df5.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']
df6.drop(['SGG_CD','SGG_NM','BJDONG_CD','LAND_GBN','LAND_GBN_NM','BONBEON','BUBEON','DEAL_YMD','RIGHT_GBN','CNTL_YMD','BUILD_YEAR','REQ_GBN','RDEALER_LAWDNM'],inplace=True,axis=1) # 시각화에 쓸모 없는 데이터 삭제
df6.columns = ['접수연도','법정동명','건물명','물건금액(만원)','건물면적','토지면적','층','건물용도']

resultDF = pd.concat([df1,df2,df3,df4,df5,df6])

print(resultDF)