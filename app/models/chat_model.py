import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import member_model
from app import db as sql_alchemy_db
from app.models.entities import chat


def get_chats():
    return sql_alchemy_db.session.query(chat.Chat).all()


def get_chat_by_chat_id(chat_id):
    return sql_alchemy_db.session.query(chat.Chat).filter_by(chat_id=chat_id).all()


def get_chats_by_user_id(user_id):
    return sql_alchemy_db.session.query(chat.Chat).filter_by(user_id=user_id).all()


def search_chat_by_param(user_id, search_param):
    try:
        return db.query_one("""
            SELECT *
            FROM chats
            WHERE user_id = %(user_id)s and is_group_chat = false and topic like %(search_param)s
        """, user_id=user_id, search_param=search_param)
    except Exception:
        raise exceptions.ChatNotFoundException()


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
