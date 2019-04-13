from app import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    user_id = db.Column(UUID(as_uuid=True), primary_key=True)
    nick = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    avatar = db.Column(db.String(), nullable=True)
    mail = db.Column(db.String(32), unique=True, nullable=False)

    # Full constructor
    def __init__(self, nick, name, avatar, mail):
        self.nick = nick
        self.name = name
        self.avatar = avatar
        self.mail = mail

