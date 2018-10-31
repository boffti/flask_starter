from sqlalchemy import Column, Integer, String
from database import Base

# Create model classes
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    post = Column(String(), nullable=False)
    # Maybe author, posted date etc

    # Constructor
    def __init__(self, title=None, post=None):
        self.title = title
        self.post = post

    # Print object
    def __repr__(self):
        return '<Post %r>' % (self.title)