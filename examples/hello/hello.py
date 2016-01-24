from flask import Flask
from flask.ext.restaction import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    """hello world"""
    schema_inputs = {
        "get": {"name": ("safestr&required&default='world'", "you name")}
    }
    schema_outputs = {
        "get": {"hello": "unicode&required"}
    }

    def get(self, name):
        """welcome to flask-restaction"""
        return {"hello": name}

api.add_resource(Hello)
api.gen_resjs()
api.gen_resdocs()

if __name__ == '__main__':
    app.run(debug=True)
