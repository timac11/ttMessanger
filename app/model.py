import app.db as db
import uuid


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
    print(result)
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
    chat_id = uuid.uuid1()
    member_user_id = uuid.uuid1()
    member_companion_id = uuid.uuid1()
    db.query_one("""
        INSERT INTO chats (chat_id, is_group_chat, topic) 
        VALUES (%(chat_id)s, false, 'hardcaded_value')
    """, chat_id=chat_id)
    db.query_one("""
        INSERT INTO members (member_id ,user_id, chat_id) 
        VALUES (%(member_id)s, %(user_id)s, chat_id)
    """, member_id=member_user_id ,user_id=user_id, chat_id=chat_id)
    db.query_one("""
        INSERT INTO members (member_id, user_id, chat_id) 
        VALUES (%(member_id)s , %(user_id)s, %(chat_id)s)
    """, member_id=member_companion_id, user_id=companion_id, chat_id=chat_id)


def create_group_chat(user_id, topic):
    pass


def add_member_to_group_chat(chat_id, user_ids):
    pass


def leave_from_group_chat(user_id):
    pass


def create_message(user_id, chat_id, content, attach_id):
    pass


def upload_file(user_id, content, chat_id):
    pass
