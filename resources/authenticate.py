import flask_restful
from functools import wraps
from flask import request


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        from .key import key
        acct = request.headers.get('key') == key and key is not None  # custom account lookup function

        if acct:
            return func(*args, **kwargs)

        flask_restful.abort(401, message='unauthorized, please provide a valid key')
    return wrapper
