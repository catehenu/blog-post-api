from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    articles = relationship('DbArticle', back_populates='user')  # Corrected here

class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)  # Fixed typo
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DbUser', back_populates='articles')  # Corrected here