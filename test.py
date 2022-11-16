from flask import Flask
import sys
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask!"

@app.route('/coffe', methods=['POST'])
def kw_facility() :
    req = requests.get_json()
    
    facility_name = req["action"]["deatilParams"]["facility_name"]["value"]
    #json파일 읽기
    
    answer = kw_facility
    # answer = "새빛관"
    
    res = {
        "version": "2.0",
        "templates": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : answer
                    }
                }
            ]
        }
    }
    
    return jsonify(res)
    # 답변 넘기기

#메인 함수
if __name__ == "__main__":
    #application.run(host='0.0.0.0', port=int(sys.argv[1]), threaded=True) ==> port번호를 쉘에서 입력받음
    application.run(host='0.0.0.0', port=5000, threaded=True)
