from app import db
from sqlalchemy.dialects.postgresql import UUID


class Member(db.Model):
    member_id = db.Column(UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), nullable=False)
    chat_id = db.Column(UUID(as_uuid=True), nullable=False)
    last_read_message_id = db.Column(UUID(as_uuid=True), nullable=True)

    # Full constructor
    def __init__(self, user_id, chat_id, last_read_message_id):
        self.user_id = user_id
        self.chat_id = chat_id
        self.last_read_message_id = last_read_message_id