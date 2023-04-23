from flask import Flask, request, Response
from heyoo import WhatsApp
from chat import generate_response


app = Flask(__name__)
WSP_API_KEY = "EAASWfzoCFZBQBAHhZAXQZBO4cepR9Yt0d6UfZCnQlYHbwsIIGx4HwBZA3aF7BD65z43jTukOLdUc2NRDHKAWuMixz7QonKTYdPZCxEhveknHShNxYA1DnvjZCNRIOzxcSzCBIPJhKLeMYY8ILSZBsoUxkmeA175NQIE4bZA7ZAAY6Qhbr2axNQmqBZAvwpKmTJb5FWSVyr4pUm3bwZDZD"


@app.route('/', methods=['GET', 'POST'])
def home():
    chanel = WhatsApp(token=WSP_API_KEY, phone_number_id="121334227598736")
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == "my_wsp":
            return request.args.get("hub.challenge")
        else:
            return Response(status=401)
    data = request.get_json()
    print("19 : ", data)
    data2 = data["entry"][0]["changes"][0]["values"]
    message = data2["messages"][0]["text"]["body"]
    response = generate_response(message, data2["contacts"][0]["profile"]["name"])
    print(chanel.send_message(response.replace("Javier Milei: ", ""), data2["contacts"][0]["wa_id"]))
    return Response(status=202, body="se envio")


if __name__ == '__main__':
    app.run(port=8080, debug=False)
