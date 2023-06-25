from database.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime




class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    posts = relationship("Post", back_populates="creator")




class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="posts")

    @hybrid_property
    def formatted_date(self):
        return self.date.strftime('%B %e, %Y')