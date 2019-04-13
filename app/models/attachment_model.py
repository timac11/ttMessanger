from app import db as sql_alchemy_db
from app.models.entities import attachment


def create_attachment(user_id, chat_id, message_id, type, url):
    attachment_add = attachment.Attachment(user_id, chat_id, message_id, type, url)
    sql_alchemy_db.session.add(attachment_add)
    sql_alchemy_db.session.commit()
    return attachment_add
