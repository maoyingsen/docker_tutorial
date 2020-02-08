from flask import Flask
from flask import jsonify
from flask import Response
 
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
 
 
@app.route('/hello',methods=['GET'])
def hello():
    return jsonify({'name': 'daniel','age': '31'})
    #return "Oh, Hello World from Flask Docker nginx"

 
if __name__ == '__main__':
    app.run(debug=DEBUG, host = HOST, port = PORT)