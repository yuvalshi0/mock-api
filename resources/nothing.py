"""
Task 1
"""
from flask_restful import Resource
from .authenticate import authenticate


class NothingResource(Resource):
    method_decorators = [authenticate]

    def nothing_to_see_here(self):
        return {'message': 'Got a key!'}

    def get(self):
        return self.nothing_to_see_here()

    def post(self):
        return self.nothing_to_see_here()
