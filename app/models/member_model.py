import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import chat_model


##################GET###################################################

def get_members():
    return db.query_all("""
        SELECT *
        FROM members
    """)


def get_member_by_member_id(member_id):
    try:
        result = db.query_one("""
            SELECT *
            FROM members
            WHERE member_id = %(member_id)s
        """, member_id=member_id)
        if result is None:
            raise exceptions.MemberNotFoundException
        else:
            return result
    except Exception:
        raise exceptions.MemberNotFoundException


def get_member_by_user_id_and_chat_id(user_id, chat_id):
    try:
        member = db.query_one("""
            SELECT *
            FROM members 
            WHERE user_id = %(user_id)s AND chat_id = %(chat_id)s
        """, user_id=user_id, chat_id=chat_id)
        if member is None:
            raise exceptions.MemberNotFoundException()
        else:
            return member
    except Exception:
        raise exceptions.MemberNotFoundException()


##################CREATE#################################################


def create_member(member_id, user_id, chat_id):
    if member_id is None:
        member_id = utils.get_uuid()
    db.edit_query("""
            INSERT INTO members (
                member_id ,
                user_id, 
                chat_id
            ) 
            VALUES (
                %(member_id)s, 
                %(user_id)s, 
                chat_id
            )
        """, member_id=member_id, user_id=user_id, chat_id=chat_id)


def add_member_to_group_chat(chat_id, user_id):
    try:
        chat = chat_model.get_chat_by_chat_id(chat_id)
    except Exception:
        raise exceptions.ChatNotFoundException

    # TODO throw exception when chat is not found
    if chat is not None:
        member_id = utils.get_uuid()
        db.edit_query("""
            INSERT INTO members (
                member_id, 
                user_id, 
                chat_id
            )
            VALUES (
                %(member_id)s,
                %(user_id)s, 
                %(chat_id)s
            )
        """, member_id=member_id, user_id=user_id, chat_id=chat_id)
