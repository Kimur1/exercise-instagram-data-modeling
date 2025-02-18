import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Enum , UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    url = Column(String(250),nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment = relationship(Comment)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250),index= True, nullable=False)  
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250),unique=True, nullable =False)
    comment = relationship(Comment)
    post = relationship(Post)
    follower = relationship(Follower)

## Draw from SQLAlchemy base
render_er(Base,'DIAGRAM.png')