import app.db as db
from app.exceptions import exceptions


##################GET###################################################

def get_users():
    return db.query_all("""
        SELECT *
        FROM users
    """)


def get_user_by_id(user_id):
    try:
        result = db.query_one("""
            SELECT *
            FROM users
            WHERE user_id = %(user_id)s
        """, user_id=user_id)
    except Exception:
        raise exceptions.UserNotFoundException
    if result is None:
        raise exceptions.UserNotFoundException
    else:
        return result


def search_users(search_param, limit=10):
    try:
        return db.query_all("""
            SELECT *
            FROM users
            WHERE nick like %(search_param)s or name like %(search_params)s
            LIMIT %(limit)s
        """, search_param=search_param, limit=limit)
    except Exception:
        raise exceptions.UserNotFoundException()
