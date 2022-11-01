import GNTA_DongJak as DJ
import GNTA_GangNam as GN
import GNTA_JongRo as JR
import matplotlib.pyplot as plt

if __name__ =='__main__':

    dongjak = DJ.society_welfare() # 동작구 데이터
    gangnam = GN.society_welfare() # 강남구 데이터
    jongro = JR.society_welfare()  # 종로구 데이터

    plt.rc('font', family='Malgun Gothic')
    plt.style.use('ggplot')

    fig = plt.figure(figsize=(30,10)) # 캔버스 크기
    ax1 = fig.add_subplot(3,1,1) # 서브플롯1
    ax2 = fig.add_subplot(3,1,2) # 서브플롯2
    ax3 = fig.add_subplot(3,1,3) # 서브플롯3

    for gu,axe,restrict,color in zip( [dongjak,gangnam,jongro] , [ax1,ax2,ax3] , ['동작구','강남구','종로구'], ['red','green','blue']): # 3개의 구 데이터를 순환
        x = list(gu.index) # 해당 구 데이터 인덱스
        y = list(gu.values) # 해당 구 데이터 값

        temp = axe.bar(x,y, width=0.4, color = color, label= restrict+' 복지시설')  # 데이터 막대를 temp에 저장

        for rect in temp: # 막대 위에 수치 표시를 위함
            height = rect.get_height()
            axe.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=15)

        axe.set_ylim(0,25) # y축 범위 제한
        axe.set_title(restrict+' 복지시설 수', size=18, weight='bold') # 각 화면의 제목
        axe.set_xticklabels(x,fontsize=9,rotation=-10) # 각 화면의 x축 레이블
        axe.legend(fontsize=10) # 각 화면의 범례

    plt.tight_layout(h_pad=3,w_pad=3)  # 세로 여백과 가로 여백 설정
    plt.show() # 표시


