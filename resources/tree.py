from math import radians
from flask_restful import Resource, reqparse
import flask_restful
import faker
from random import randrange
from .authenticate import authenticate

fake = faker.Faker()

INVALID_TREE_MESSAGE = "Tree depth is invalid!"
INVALID_AGE_MESSAGE = "Max age is invalid!"


def generate_leaf(max_age=50):
    name = fake.name()
    date = fake.city()
    company = fake.company()
    phone_number = fake.phone_number()
    job = fake.job()
    age = max(randrange(max_age), 1)
    return {'name': name, 'address': date, 'age': age, 'company': company, 'job': job, 'phone_number': phone_number}


def generate_tree(depth, max_age=50):
    tree = generate_leaf(max_age)
    temp = tree
    for _ in range(depth):
        temp['connection'] = generate_leaf(max_age)
        temp = temp['connection']
    return tree


def generate_hard_tree(depth, max_age=50):
    if depth == 0:
        tree = generate_leaf(max_age)
        tree['connection'] = []
        return tree
    tree = generate_leaf(max_age)
    temp = tree
    for current_depth in range(depth):
        temp['connection'] = []
        rand_range = randrange(1, 10)
        chosen = max(0, rand_range - 1)
        for _ in range(rand_range):
            temp['connection'].append(generate_hard_tree((depth - current_depth - 3), max_age=max_age))
        temp = temp['connection'][chosen]
    return tree


class TreeResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('depth', type=int, required=True, help=INVALID_TREE_MESSAGE, location='args')
        parser.add_argument('age', type=int, required=False, help=INVALID_AGE_MESSAGE, location='args')
        parser.add_argument('hard', type=bool, required=False, location='args')
        args = parser.parse_args()
        depth = args.get('depth')
        max_age = args.get('age') or 50
        hard = bool(args.get('hard'))
        max_tree_depth = 50 if not hard else 15

        if not 0 < depth <= max_tree_depth:
            flask_restful.abort(400, message={"depth": INVALID_TREE_MESSAGE})

        if not 0 < max_age <= 120:
            flask_restful.abort(400, message={"depth": INVALID_AGE_MESSAGE})

        tree = generate_tree(depth, max_age=max_age) if not hard else generate_hard_tree(depth, max_age=max_age)
        return tree
