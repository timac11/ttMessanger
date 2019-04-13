from app import db
from sqlalchemy.dialects.postgresql import UUID


class Message(db.Model):
    message_id = db.Column(UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), nullable=False)
    chat_id = db.Column(UUID(as_uuid=True), nullable=False)
    content = db.Column(db.String(), nullable=True)
    added_at = db.Column(db.TIMESTAMP(), nullable=True)

    # Full constructor
    def __init__(self, user_id, chat_id, content, added_at):
        self.user_id = user_id
        self.chat_id = chat_id
        self.content = content
        self.added_at = added_at