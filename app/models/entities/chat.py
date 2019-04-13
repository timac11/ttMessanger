from app import db
from sqlalchemy.dialects.postgresql import UUID


class Chat(db.Model):
    chat_id = db.Column(UUID(as_uuid=True), primary_key=True)
    is_group_chat = db.Column(db.Boolean(), default=False)
    topic = db.Column(db.String(80), nullable=False)
    last_message = db.Column(UUID(as_uuid=True), nullable=True)
    messages = db.relationship('Message', backref='chat', lazy=True)

    # Full constructor
    def __init__(self, is_group_chat, topic, last_message):
        self.is_group_chat = is_group_chat
        self.topic = topic
        self.last_message = last_message
