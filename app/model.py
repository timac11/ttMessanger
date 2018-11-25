import app.db as db
from app import utils

"""
    /get_messages_by_user_id
"""


def get_messages_by_user_id(user_id, limit=10):
    result = db.query_all("""
        SELECT *
        FROM messages
        WHERE user_id = %(user_id)s
        LIMIT %(limit)s
    """, user_id=user_id, limit=limit)
    return result

"""
    /list_chats/
"""


def get_chats_by_user_id(user_id, limit=10):
    return db.query_all("""
        SELECT * 
        FROM chats
        WHERE user_id = %(user_id)s
        ORDER BY added_at DESC
        LIMIT %(limit)s
    """, user_id=user_id, limit=limit)


"""
    /search_chats/
"""


def search_chat_by_param(user_id, search_param):
    return db.query_one("""
        SELECT *
        FROM chats
        WHERE user_id = %(user_id)s and is_group_chat = false and topic like %(search_param)s
    """, user_id=user_id, search_param=search_param)


"""
    /search_users/
"""


def search_users(search_param, limit=10):
    return db.query_all("""
        SELECT *
        FROM users
        WHERE nick like %(search_param)s or name like %(search_params)s
        LIMIT %(limit)s
    """, search_param=search_param, limit=limit)


"""
    /create_pers_chat/
"""


def create_chat_by_user_id(user_id, companion_id):
    chat_id = utils.get_uuid()
    member_user_id = utils.get_uuid()
    member_companion_id = utils.get_uuid()
    db.edit_query("""
        INSERT INTO chats (chat_id, is_group_chat, topic) 
        VALUES (%(chat_id)s, false, %(topic)s)
    """, chat_id=chat_id, topic=user_id)
    db.edit_query("""
        INSERT INTO members (member_id ,user_id, chat_id) 
        VALUES (%(member_id)s, %(user_id)s, chat_id)
    """, member_id=member_user_id ,user_id=user_id, chat_id=chat_id)
    db.edit_query("""
        INSERT INTO members (member_id, user_id, chat_id) 
        VALUES (%(member_id)s , %(user_id)s, %(chat_id)s)
    """, member_id=member_companion_id, user_id=companion_id, chat_id=chat_id)


"""
    /create_message
"""


def create_message(user_id, chat_id, content, attachment):
    message_id = utils.get_uuid()
    member = db.query_one("""
        SELECT *
        FROM members 
        WHERE user_id = %(user_id)s AND chat_id = %(chat_id)s
    """, user_id=user_id, chat_id=chat_id)
    # TODO throw exceptions: user/member not found
    if member is None or member.get('member_id') is None:
        return {}

    db.edit_query("""
        INSERT INTO messages (message_id, chat_id, user_id, content)
        VALUES (%(message_id)s, %(chat_id)s, %(user_id)s, %(content)s)
    """, message_id=str(message_id), chat_id=str(chat_id), user_id=str(user_id), content=str(content))

    if attachment is not None:
        attachment_id = utils.get_uuid()
        db.edit_query("""
            INSERT INTO attachments (attachment_id, chat_id, user_id, message_id, "type", url)
            VALUES (%(attachment_id)s , %(chat_id)s, %(user_id)s, %(message_id)s, %(type_)s, %(url)s)
        """, attachment_id=attachment_id, chat_id=chat_id, user_id=user_id,
                     message_id=message_id, type_=attachment['type'], url=attachment['url'])


def read_message(user_id, chat_id, message_id):
    db.edit_query("""
        UPDATE members SET last_read_message_id = %(message_id)s
        WHERE user_id = %(user_id) AND chat_id = %(chat_id)
    """, user_id=user_id, chat_id=chat_id, message_id=message_id)


def create_group_chat(user_id, topic):
    pass


def add_member_to_group_chat(chat_id, user_ids):
    pass


def leave_from_group_chat(user_id):
    pass


def upload_file(user_id, content, chat_id):
    pass
