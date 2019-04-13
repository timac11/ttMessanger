from app import db
from sqlalchemy.dialects.postgresql import UUID


class Attachment(db.Model):
    attachment_id = db.Column(UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), unique=False, nullable=False)
    message_id = db.Column(UUID(as_uuid=True), unique=False, nullable=False)
    chat_id = db.Column(UUID(as_uuid=True), unique=False, nullable=False)
    type = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)

    # Full constructor
    def __init__(self, user_id, chat_id, message_id, type, url):
        self.user_id = user_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.type = type
        self.url = url