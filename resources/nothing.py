from flask_restful import Resource


class NothingResource(Resource):

    def nothing_to_see_here(self):
        return {'message': 'Nothing to see here..'}

    def get(self):
        return self.nothing_to_see_here()

    def post(self):
        return self.nothing_to_see_here()
