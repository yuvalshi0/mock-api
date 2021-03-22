"""
This Task was not given in the end to candidates
"""
import flask_restful
from time import sleep
from random import randrange
import threading
from resources.atomic_list import AtomicCounterList
from flask_restful import Resource, reqparse
from .authenticate import authenticate
from .randfact import get_fact

count = AtomicCounterList()


def very_secret_calc(complexity=60):
    id = count.increment()
    sleep(randrange(int(complexity / 2), complexity))
    count.decrement(id)


class LongCalcInitiator(Resource):
    method_decorators = [authenticate]

    def error_message(self):
        return flask_restful.abort(400, status=0, error='The calculation parameter is invalid!')

    def too_many_calcs(self):
        return flask_restful.abort(400, status=4, error='I running too much calculations here!!')

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('param', type=int, location='json')
        args = parser.parse_args()
        param = args.get('param') or 60

        if not 5 <= param <= 60:
            return self.error_message()

        if len(count) >= 2:
            return self.too_many_calcs()

        threading.Thread(target=very_secret_calc, args=[param]).start()
        return {'status': 1, 'message': 'Starting calculation!', 'calc_id': count.value, 'max_time': param}


class LongCalculatorStatus(Resource):
    method_decorators = [authenticate]

    def get(self, id):
        if not str(id).isnumeric():
            return flask_restful.abort(400, status=0, error='Invalid Calculation ID')
        if int(id) in count.finished_list:
            return {'status': 2, 'message': 'Calculation finished!'}
        if int(id) in count.list:
            return {'status': 1, 'message': 'Calculation is still running, in the meantime enjoy a funfact', 'fact': f"{get_fact()}"}
        return {'status': 3, 'mesaage': 'Calculation not found!'}
