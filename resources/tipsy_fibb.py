"""
Task 4
"""
import random
from flask_restful import Resource, reqparse
import flask_restful
from .authenticate import authenticate

SIZE_ERROR_MESSAGE = 'Array size it too big!'


def fib(n, number_one, number_two):
    a, b = number_one, number_two
    mistake = random.choice([1, 0, -1])
    for _ in range(n):
        yield a + mistake
        a, b = b, a + b


class TipsyFibbonachi(Resource):
    method_decorators = [authenticate]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('number_one', type=int, location='json')
        parser.add_argument('number_two', type=int, location='json')
        parser.add_argument('size', type=int, location='json')
        args = parser.parse_args()

        number_one = args.get('number_one') or 0
        number_two = args.get('number_two') or 1
        size = args.get('size') or 10

        if not 0 < size <= 1000:
            flask_restful.abort(400, message={'size': SIZE_ERROR_MESSAGE})

        return {'list': list(fib(size, number_one, number_two))}
