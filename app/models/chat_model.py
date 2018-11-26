import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import user_model, member_model


##################GET###################################################

def get_chats():
    return db.query_all("""
        SELECT *
        FROM chats
    """)


def get_chat_by_chat_id(chat_id):
    try:
        result = db.query_one("""
            SELECT *
            FROM chats 
            WHERE chat_id = %(chat_id)s
        """, chat_id=chat_id)
        if result is None:
            raise exceptions.ChatNotFoundException
    except Exception:
        raise exceptions.ChatNotFoundException


def get_chats_by_user_id(user_id, limit=10):
    try:
        return db.query_all("""
            SELECT * 
            FROM chats
            WHERE user_id = %(user_id)s
            LIMIT %(limit)s
        """, user_id=user_id, limit=limit)
    except Exception:
        raise exceptions.ChatNotFoundException()


def search_chat_by_param(user_id, search_param):
    try:
        return db.query_one("""
            SELECT *
            FROM chats
            WHERE user_id = %(user_id)s and is_group_chat = false and topic like %(search_param)s
        """, user_id=user_id, search_param=search_param)
    except Exception:
        raise exceptions.ChatNotFoundException()


def leave_from_group_chat(user_id, chat_id):
    pass


##################CREATE#################################################


def create_chat_by_user_id(user_id, companion_id):
    chat_id = utils.get_uuid()
    member_user_id = utils.get_uuid()
    member_companion_id = utils.get_uuid()

    db.edit_query("""
        INSERT INTO chats (
            chat_id, 
            is_group_chat, 
            topic
        ) 
        VALUES (
            %(chat_id)s, 
            false, 
            %(topic)s
        )
    """, chat_id=chat_id, topic=user_id)

    member_model.create_member(member_user_id, user_id, chat_id)
    member_model.create_member(member_companion_id, companion_id, chat_id)


def create_group_chat(topic):
    chat_id = utils.get_uuid()
    db.edit_query("""
        INSERT INTO chats (
            chat_id, 
            topic
        )
        VALUES (
            %(chat_id)s, 
            %(topic)s
        )
    """, chat_id=chat_id, topic=topic)
