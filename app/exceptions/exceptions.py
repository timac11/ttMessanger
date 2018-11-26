class UserNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, "User is not found")


class ChatNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, "Chat is not found")


class MessageNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, "Message is not found")


class MemberNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, "Member is is not found")

