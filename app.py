from flask import Flask, redirect
from flask_restful import Resource, Api
from flask_pymongo import pymongo
from datetime import datetime
import secrets

app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient("mongodb://db:27017/")

def get_schema(schema):
    if schema == 'string':
        return {
            'original_string': None,
            'modified_string': None,
            'timestamp': datetime.now()
        }
    else:
        return 'Schema was not found'

class Redirect(Resource):
    def get(self):
        return redirect('/add/you_can_change_this', code=302)

class TestEndpoint(Resource):
    def get(self, example_string):
        # If no string was written, return this.
        if example_string == 'you_can_change_this':
            return {'msg': 'Please write which string you want to add.'}

        # Connect to db.
        db = client.db['example_strings']

        # Get needed schema
        schema = get_schema('string')

        # Generate a token.
        secret_token = secrets.token_hex(16)

        # Add original string.
        schema['original_string'] = example_string

        # Add modified string.
        schema['modified_string'] = example_string + secret_token

        # Insert data.
        db.insert_one(schema)
        return {'msg': 'Data was added!'}

api.add_resource(Redirect, '/')
api.add_resource(TestEndpoint, '/add/<string:example_string>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)