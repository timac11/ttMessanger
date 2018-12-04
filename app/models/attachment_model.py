import app.db as db
from app import utils
from app.exceptions import exceptions
from app.models import user_model, member_model


# TODO verify that user chat and message exists
def create_attachment(user_id, chat_id, message_id, type, url):
    attachment_id = utils.get_uuid()
    print('attachment_id {}'.format(attachment_id))
    print('user_id {}'.format(user_id))
    print('chat_id {}'.format(chat_id))
    print('message_id {}'.format(message_id))
    db.edit_query("""
        INSERT INTO attachments (
            attachment_id, 
            user_id, 
            chat_id,
            message_id, 
            "type", 
            url
        )
        VALUES (
            %(attachment_id)s,
            %(user_id)s,
            %(chat_id)s,
            %(message_id)s,
            %(type)s,
            %(url)s
        )
    """, attachment_id=str(attachment_id), user_id=str(user_id), chat_id=str(chat_id), message_id=str(message_id), type=type, url=url)