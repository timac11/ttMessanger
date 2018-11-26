import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import user_model, member_model, chat_model


##################GET###################################################


def get_messages_by_user_id(user_id, limit=10):
    user = user_model.get_user_by_id(user_id)
    if user is None:
        raise exceptions.UserNotFoundException
    try:
        result = db.query_all("""
            SELECT *
            FROM messages
            WHERE user_id = %(user_id)s
            LIMIT %(limit)s
        """, user_id=user_id, limit=limit)
    except Exception:
        raise exceptions.MessageNotFoundException()
    return result


##################CREATE#################################################


def create_message(user_id, chat_id, content, attachment):
    message_id = utils.get_uuid()
    try:
        member_model.get_member_by_user_id_and_chat_id(user_id, chat_id)
    except Exception:
        raise exceptions.MemberNotFoundException()

    db.edit_query("""
        INSERT INTO messages (
            message_id, 
            chat_id, 
            user_id, 
            content
        )
        VALUES (
            %(message_id)s, 
            %(chat_id)s, 
            %(user_id)s, 
            %(content)s
        )
    """, message_id=str(message_id), chat_id=str(chat_id), user_id=str(user_id), content=str(content))


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
