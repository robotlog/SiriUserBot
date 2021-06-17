from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric
from userbot.modules.sql_helper import SESSION, BASE


class ChatBot(BASE):
    __tablename__ = "chatbot_ai"
    user_id = Column(Numeric, primary_key=True)
    chat_id = Column(Numeric, primary_key=True)
    session_id = Column(UnicodeText)
    session_expires = Column(Numeric)

    def __init__(
        self,
        user_id,
        chat_id,
        session_id,
        session_expires
    ):
        self.user_id = user_id
        self.chat_id = chat_id
        self.session_id = session_id
        self.session_expires = session_expires


ChatBot.__table__.create(checkfirst=True)


def get_ch(user_id, chat_id):
    try:
        return SESSION.query(ChatBot).get((user_id, chat_id))
    except:
        return None
    finally:
        SESSION.close()


def get_all_ch():
    try:
        return SESSION.query(ChatBot).all()
    except:
        return None
    finally:
        SESSION.close()


def add_ch(
    user_id,
    chat_id,
    session_id,
    session_expires
):
    adder = SESSION.query(ChatBot).get((user_id, chat_id))
    if adder:
        adder.session_id = session_id
        adder.session_expires = session_expires
    else:
        adder = ChatBot(
            user_id,
            chat_id,
            session_id,
            session_expires
        )
    SESSION.add(adder)
    SESSION.commit()


def remove_ch(
    user_id,
    chat_id
):
    note = SESSION.query(ChatBot).get((user_id, chat_id))
    if note:
        SESSION.delete(note)
        SESSION.commit()
