from app import db as sql_alchemy_db
from app.models.entities import user as user


def create_user(nick, name, avatar, male):
    user_add = user.User(nick, name, avatar, male)
    sql_alchemy_db.session.add(user_add)
    sql_alchemy_db.session.commit()
    return user_add


def get_users():
    return sql_alchemy_db.session.query(user.User).all()


def get_user_by_id(user_id):
    return sql_alchemy_db.session.query(user.User).filter_by(user_id=user_id).all()


## TODO possible to get users by search params
## TODO add filter param
def search_users(nick):
    return sql_alchemy_db.session.query(user.User).filter_by(nick=nick).all()
