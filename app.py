from flask import Flask, request
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class Check(Resource):
    def get(self):
        return { 'msg' : 'hello world :: sixth build' } ,200


api.add_resource(Check, '/')
app.run(host='0.0.0.0', port=5000)

