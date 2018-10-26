from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    if request.method=='POST':
        if int(version)==1:
            return jsonify(version=1,predict=request.get_json()['predict'])
       	return jsonify(version=0,predict=request.get_json()['old_predict'])
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа {"version":1, "predict":<predict_value>}
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return "Для получения результата /get_classifier_result/<version:0,1> "

if __name__ == "__main__":
    app.run()
