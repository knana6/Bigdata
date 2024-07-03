# 프로그래머 :  SH, MH 
# 해양 환경 빅데이터 분석기 제작 

import matplotlib.pyplot as plt
import matplotlib.image as img

def showImg(imgname) :
    imgTest = img.imread("c:/Users/PC/Desktop/해양_환경_분석기_자료/" + imgname)
    plt.imshow(imgTest)
    plt.show()

print(" 해양 환경 빅데이터 분석기 ")

print(" 안녕하세요, 원하는 해수욕장의 이름을 입력 해주신 뒤 측정을 원하시는 값을 입력해 주세요")
print(" 기준: 2023년 부산시 해양환경 현황 공공데이터 기반")

A = input(" 해수욕장 이름을 입력해주세요: ")
B = input(" 측정하고 싶은 값을 입력해주세요: ")

if A == '해운대' :
    if B == '금속':
        showImg("Hae1.jpg")
    elif B == '염분':
        showImg("Hae2.jpg")
    elif B == '투명도':
        showImg("Hae3.jpg")
    elif B == '수질': 
        showImg("Hae4.jpg")
    elif B == '수소 이온 농도':
        showImg("Hae5.jpg")
    else :
        print("입력 오류. 다시 실행하세요")
elif A == '광안리' :
    if B == '금속':
        showImg("Gan1.jpg")
    elif B == '염분':
        showImg("Gan2.jpg")
    elif B == '투명도':
        showImg("Gan3.jpg")
    elif B == '수질':
        showImg("Gan4.jpg")
    elif B == '수소 이온 농도':
        showImg("Gan5.jpg")
    else :
        print("입력 오류. 다시 실행하세요")
elif A == '송도' :
    if B == '금속': 
        showImg("Song1.jpg")
    elif B == '염분':
        showImg("Song2.jpg")
    elif B == '투명도':
        showImg("Song3.jpg")
    elif B == '수질':
        showImg("Song4.jpg")
    elif B == '수소 이온 농도':
        showImg("Song5.jpg")
    else :
        print("입력 오류. 다시 실행하세요")
elif A == '다대포' :
    if B == '금속':
        showImg("Dae1.jpg")
    elif B == '염분':
        showImg("Dae2.jpg")
    elif B == '투명도':
        showImg("Dae4.jpg")
    elif B == '수질':
        showImg("Dae4.jpg")
    elif B == '수소 이온 농도':
        showImg("Dae5.jpg")
    else :
       print("입력 오류. 다시 실행하세요")
