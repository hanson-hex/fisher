from flask import Blueprint

from . import web

@web.route('/url')
def login():
    pass