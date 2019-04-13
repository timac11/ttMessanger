import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import chat_model
from app import db as sql_alchemy_db
from app.models.entities import member as member


def get_members():
    return sql_alchemy_db.session.query(member.Member).all()


def get_member_by_member_id(member_id):
    return sql_alchemy_db.session.query(member.Member).filter_by(member_id=member_id)


def get_member_by_user_id_and_chat_id(user_id, chat_id):
    return sql_alchemy_db.session.query(member.Member).filter_by(user_id=user_id, chat_id=chat_id)


def create_member(member_id, user_id, chat_id):
    member_add = member.Member(user_id, chat_id)
    sql_alchemy_db.session.add(member_add)
    sql_alchemy_db.session.commit()
    return member_add


## TODO refactoring
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
