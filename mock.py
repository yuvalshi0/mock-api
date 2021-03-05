from resources.item import ItemResource
from resources.very_long_calc import LongCalcInitiator, LongCalculatorStatus
import sys
from flask import Flask
from flask_restful import Api
from resources.tree import TreeResource
from resources.key import KeyResource
from resources.tipsy_fibb import TipsyFibbonachi
from resources.nothing import NothingResource
from colored import fg, attr
import logging


PORT = 7117

app = Flask(__name__)
api = Api(app)

log = logging.getLogger('werkzeug')
log.disabled = True

api.add_resource(TreeResource, '/tree')
api.add_resource(KeyResource, '/key')
api.add_resource(TipsyFibbonachi, '/tipsy')
api.add_resource(NothingResource, '/')
api.add_resource(LongCalcInitiator, '/calc')
api.add_resource(LongCalculatorStatus, '/calc/<id>')
api.add_resource(ItemResource, '/item/<id>/children')

if __name__ == '__main__':
    try:
        print(f"{fg('yellow')}{attr('bold')} Automation QA Evaluation Execrise{attr('reset')}")
        print(f"{fg('yellow')}{attr('bold')} Running on port: {PORT}{attr('reset')}")
        print(f"{fg('green')}{attr('bold')} Good Luck!{attr('reset')}")
        cli = sys.modules['flask.cli']
        cli.show_server_banner = lambda *x: ""
        app.run(port=PORT)
    except Exception as e:
        print(f"{fg('red')}{attr('bold')} Failed to run the server{attr('reset')}")
        print(f"{fg('red')}Failure Reason: {str(e)}{attr('reset')}")
