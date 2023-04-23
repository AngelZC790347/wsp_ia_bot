from flask import Flask, request, Response
from heyoo import WhatsApp
from chat import generate_response
import os
import config
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == os.getenv('HUB_VERIFY_TOKEN'):
            return request.args.get("hub.challenge")
        else:
            return Response(status=401)
    chanel = WhatsApp(token=os.getenv('WSP_API_KEY'), phone_number_id=os.getenv('TEST_NUMBER_ID'))
    data = request.get_json()
    data2 = data["entry"][0]["changes"][0]["values"]
    message = data2["messages"][0]["text"]["body"]
    response = generate_response(message, data2["contacts"][0]["profile"]["name"])
    print(chanel.send_message(response.replace(f"{config.ia_name}: ", ""), data2["contacts"][0]["wa_id"]))
    return Response(status=202, body="sended")


if __name__ == '__main__':
    app.run(port=8080, debug=False)
