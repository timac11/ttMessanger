import flask
import psycopg2
import psycopg2.extras
import blinker
from app import config, app


def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(
            dbname=config.DATABASE, user=config.USER_NAME, host='127.0.0.1', password=config.PASSWORD
        )
    return flask.g.dbconn


def get_cursor():
    connection = get_connection()
    return connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


def query_one(query, **params):
    with get_cursor() as cursor:
        cursor.execute(query, params)
        return dict(cursor.fetchone())


def query_all(query, **params):
    with get_cursor() as cursor:
        cursor.execute(query, params)
        result = []
        print(cursor.rowcount)
        for _ in [0, cursor.rowcount]:
            result.append(dict(cursor.fetchone()))
        return result


def _rollback_db(sender, exception, **extra):
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.rollback()
        conn.close()
        delattr(flask.g, 'dbconn')


def _commit_db():
    if hasattr(flask.g, 'dbconn'):
        conn = flask.g.dbconn
        conn.commit()
        conn.close()
        delattr(flask.g, 'dbconn')


flask.got_request_exception.connect(_rollback_db, app)
flask.request_finished.connect(_commit_db, app)
