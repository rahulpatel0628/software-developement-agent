from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User({self.username})'

    def save_to_db(self):
        try:
            session.add(self)
            session.commit()
        except SQLAlchemyError as e:
            logging.error(e)
            session.rollback()