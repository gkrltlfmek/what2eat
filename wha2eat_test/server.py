from flask import Flask, json, request, jsonify
import sys, os
import datetime
import pandas as pd
from io import StringIO
from collections import namedtuple
from urllib.parse import urlparse
from PyKakao import KakaoLocal

app = Flask(__name__)

app = Flask(__name__)

menuData = pd.read_csv("./table.csv", header=None, encoding="utf=8")

def return_print(*prt_str):
    io = StringIO()
    print(*prt_str, file=io, end="")
    return io.getvalue()

def get_img_content(coding='utf-8'):
    with open('./TodayPicture/TodayMenu.png', 'rb') as f:
        img_data = base64.b64encode(f.read()).decode(coding)
        return img_data


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        'type': 'buttons',
        'buttons': ['아무것도아님']
    }
    return jsonify(dataSend)

@app.route('/test', methods=['GET'])
def Test():
    return "hello"

@app.route('/message_hamji', methods=['POST'])
def Message():
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n", "")
    print(content)
    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    price = "가격은 점심 저녁 : 5,500원\n 도시락 3500원";
    dayweek = datetime.datetime.today().weekday()
    # print(content)
    if content == "월요일 메뉴":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title" : "월요일 메뉴",
                                    "description": menuData[0][0] + "\n" + menuData[0][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "화요일 메뉴":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title" : "화요일 메뉴",
                                    "description": menuData[1][0] + "\n" + menuData[1][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "수요일 메뉴":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "수요일 메뉴",
                                    "description": menuData[2][0] + "\n" + menuData[2][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "목요일 메뉴":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title" : "목요일 메뉴",
                                    "description": menuData[3][0] + "\n" + menuData[3][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "금요일 메뉴":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    #"title": day_weeks,
                                    "title" : "금요일 메뉴",
                                    "description": menuData[4][0] + "\n" + menuData[4][1]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == "얼마야?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "가격정보",
                                    "description": price
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
    elif content == "오늘 밥은?":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [{
                    "simpleText": {
                        "text": "메뉴를 눌러주세요"
                    }
                }],
                "quickReplies": [
                    {
                        "action": "message",
                        "label": "월요일 메뉴",
                        "messageText": "월요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "화요일 메뉴",
                        "messageText": "화요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "수요일 메뉴",
                        "messageText": "수요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "목요일 메뉴",
                        "messageText": "목요일 메뉴"
                    },
                    {
                        "action": "message",
                        "label": "금요일 메뉴",
                        "messageText": "금요일 메뉴"
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "메뉴가 궁금하시면 다음버튼을 눌러주세요"
                        }
                    }],
                "quickReplies": [
                    {
                        "action": "message",
                        "label": "오늘 밥은?",
                        "messageText": "오늘 밥은?"
                    },
                    {
                        "action": "message",
                        "label": "얼마야?",
                        "messageText": "얼마야?"
                    }
                ],
            }
        }
    return jsonify(dataSend)

@app.route('/info', methods=['POST'])

def info():
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n","")
    print(content)

    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]

    if content == "화도관" or content == "화도":
            dataSend = {
              "version": "2.0",
              "template": {
                 "outputs": [
                    {
                        "simpleText": {
                            "text": "https://place.map.kakao.com/17563675",
                     }
                }
            ]
        }
    }
    elif content == "문화관" or content == "문화" or content == "문":
          dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "https://place.map.kakao.com/22535573",
                    }
                }
            ]
        }
    }

    elif content == "80주년기념관" or content == "기념관" or content == "기":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/823736351",
                        }
                }
            ]
        }
    }


    elif content == "옥의관" or content == "옥의" or content == "옥":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17567827",
                        }
                }
            ]
        }
    }
    elif content == "비마관" or content == "비마" or content == "비":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17561911",
                        }
                }
            ]
        }
    }
    elif content == "새빛관" or content == "새빛" or content == "새":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/715015774",
                        }
                }
            ]
        }
    }
    elif content == "참빛관" or content == "참빛" or content == "참":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/27202326",
                        }
                }
            ]
        }
    }

    elif content == "누리관" or content == "누리" or content == "누" or content == "누리섬":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/12721052",
                        }
                }
            ]
        }
    }
    elif content == "한울관" or content == "한울" or content == "한":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17566581",
                        }
                }
            ]
        }
    }
    elif content == "연구관" or content == "연구" or content == "연":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17562012",
                        }
                }
            ]
        }
    }
    elif content == "한천재" or content == "한천":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/1966903651",
                        }
                }
            ]
        }
    }

    elif content == "복지관" or content == "복지" or content == "복" or content == "동아리" or content == "동아리실":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17565051",
                        }
                }
            ]
        }
    }
    elif content == "다산재" or content == "다산" or content == "다":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/17567346",
                        }
                }
            ]
        }
    }
    elif content == "SNK비타민센터" or content == "SNK" or content == "SNK비타민" or content == "비타민센터":
        dataSend = {
                "version": "2.0",
                "template": {
                        "outputs": [
                        {
                                "simpleText": {
                                "text": "https://place.map.kakao.com/840278011",
                        }
                }
            ]
        }
    }
    return jsonify(dataSend)

@app.route('/message_recommend', methods=['POST'])
def Message_recommend() :
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n", "")
    print(content)
    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]

@app.route('/restaurant', methods=['POST'])

def Restaurant():
    MAX_INDEX = 5
    i=0
    req = request.get_json()
    content = req["userRequest"]["utterance"]
    content = content.replace("\n","")
    print(content)

    #api 키
    service_key = "e3eb9a3014472ef87450e05d5e0b78c1"
    KL = KakaoLocal(service_key)

    id_value = req["userRequest"]["user"]["id"]
    block_value = req["userRequest"]["block"]["id"]

    category_group_code = None
    x, y = 127.058338066917, 37.6193203481648    # 중심 좌표
    radius = 500                                 # 반경거리(m)

    result = KL.search_keyword(content,category_group_code, x, y, radius)
    index = min(len(result["documents"]), 5)
    res_info = ""
    if (index <= 0) :
        res_info = "검색 결과가 없습니다"
    else :
        for i in range(index) :
            tmp_str = return_print(result["documents"][i]["place_url"])
            print(tmp_str)
            res_info += tmp_str +"\n"
            tmp_str = return_print("가게 이름 : " + result["documents"][i]["place_name"])
            res_info += tmp_str +"\n"
            tmp_str = return_print("전화번호: " + result["documents"][i]["phone"])
            res_info += tmp_str +"\n"
            tmp_str = return_print("주소 : " + result["documents"][i]["road_address_name"])
            res_info += tmp_str +"\n"
    dataSend = {
          "version": "2.0",
          "template": {
             "outputs": [
                {
                    "simpleText": {
                        "text": res_info,
                        }
            }
        ]
    }
 }

    return jsonify(dataSend)
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)