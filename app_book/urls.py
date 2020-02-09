from app_book.controller import get_authors, new_quote
from manager.baseapp import BaseApp
from manager.wrappers import pass_data, inject_db, jsonify


#
# def call_router(app):
#     # wrappers = [check_auth, inject_db, jsonify, timeit]
#     app.route('/getallbooks', 'GET', get_authors, apply=[inject_db, jsonify])
#     app.route('/q', 'POST', new_quote, apply=[pass_data, inject_db, jsonify])

class BookRoute(BaseApp):
    def call_router(self, core):
        core.route('/getallbooks', 'GET', get_authors, apply=[inject_db, jsonify])
        core.route('/q', 'POST', new_quote, apply=[pass_data, inject_db, jsonify])
