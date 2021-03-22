"""
Task 2
"""
from flask_restful import Resource
import flask_restful
from .authenticate import authenticate


class ItemResource(Resource):
    method_decorators = [authenticate]

    def get(self, id):
        if int(id) == 1:
            return []
        if int(id) == 2:
            return [1]
        return flask_restful.abort(400, message="Unknown id")
