from database import db_session
from models import Post

def getTrendingPosts():
    trending = []

    for i in range(5):
        posts = {
        'title' : 'Title_' + str(i+1),
        'description' : 'blah blah blah blah blah blah blah blah blah blah blah_' + str(i+1),
        'date' : 'date_' + str(i+1)
        }
        trending.append(posts)
    return trending

def updatePostDB(name, email):
    if name is not '':
        if email is not '':
            db_session.add(Post(name, email))
            db_session.commit()
            print('Data Pushed to DB Successfully')
        else: print('Email is null')
    else: print('Name is null')