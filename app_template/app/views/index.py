from flask import render_template
from flask.ext.sqlalchemy import get_debug_queries
from app import app
from config import DATABASE_QUERY_TIMEOUT


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= DATABASE_QUERY_TIMEOUT:
            app.logger.warning(
                "SLOW QUERY: {}\nParameters: {}\nDuration: {0:.2f}s\nContext: {}\n".format(
                    query.statement, query.parameters, query.duration, query.context
                ))
    return response


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
