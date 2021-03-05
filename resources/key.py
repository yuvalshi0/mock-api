
from flask_restful import Resource
import random
import string

global key
key = None


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class KeyResource(Resource):

    def post(self):
        global key
        key = randomword(15)
        return {'key': key}
