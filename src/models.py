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
    id = column(Integer, primary_key=True)
    author_id = column(Integer, ForeignKey('user.id'))
    post_id = column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post = relationship(Post)





class Follower(Base):
    __tablename__ = 'follower'
    id = column(Integer, primary_key=True)
    user_from_id = column(Integer, ForeignKey('user.id'))
    user_to_id = column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class User(Base):
    __tablename__ = 'user'
    id = column(Integer, primary_key=True)
    username = column(String(250),index= True, nullable=False)  
    firstname = column(String(250), nullable=False)
    lastname = column(String(250), nullable=False)
    email = column(String(250),unique=True, nullable =False)
   

class Post(Base):
    __tablename__ = 'post'
    id = column(Integer, primary_key=True)
    user_to_id = column(String(250), ForeignKey('user.id'), nullable=False)
    user = relationship(User)
    url = column(String(250),nullable=False)
    post_id = column(Integer, ForeignKey('post.id'))

  
## Draw from SQLAlchemy base
render_er(Base,'DIAGRAM.png')