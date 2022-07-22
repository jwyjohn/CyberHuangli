from flask import Flask
from flask_restful import Resource, Api
from calenda import get_huangli

app = Flask(__name__)
api = Api(app)

salt = "今日も１日元気に遊ぼーぜー！"

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Huangli(Resource):
    def get(self):
        return get_huangli(salt)

api.add_resource(Huangli, '/')

if __name__ == '__main__':
    app.run(debug=True)