from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    return 'hi'


if __name__ == "__main__":
    print("Starting python flask server")
    app.run()
#E:\OFFICE\deep_learning\bengaluru_house_price_prediction\server\artifacts\columns.json