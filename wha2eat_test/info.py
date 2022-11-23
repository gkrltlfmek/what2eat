from flask import Flask, request, jsonify
import sys, os
app = Flask(__name__)

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

  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

