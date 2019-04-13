import app.db as db
from app.exceptions import exceptions
from app.models import user_model, chat_model
from app import db as sql_alchemy_db
from app.models.entities import message as message


def get_messages():
    return sql_alchemy_db.session.query(message.Message).all()


## TODO refactoring
def get_messages_by_user_id(user_id):
    return sql_alchemy_db.session.query(message.Message).filter_by(user_id=user_id).all()


def create_message(user_id, chat_id, content):
    message_add = message.Message(user_id, chat_id, content)
    sql_alchemy_db.session.add(message_add)
    sql_alchemy_db.session.commit()
    return message_add


## TODO change to sql alchemy
def read_message(user_id, chat_id, message_id):
    try:
        user_model.get_user_by_id(user_id)
    except Exception:
        raise exceptions.UserNotFoundException
    try:
        chat_model.get_chat_by_chat_id(chat_id)
    except Exception:
        raise exceptions.ChatNotFoundException

    db.edit_query("""
        UPDATE members SET last_read_message_id = %(message_id)s
        WHERE user_id = %(user_id) AND chat_id = %(chat_id)
    """, user_id=user_id, chat_id=chat_id, message_id=message_id)
