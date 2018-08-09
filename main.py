from flask import Flask
from config import DevConfig
from  flask_sqlalchemy import SQLAlchemy
from  sqlalchemy import Column,Integer,String,ForeignKey
app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

tags = db.Table('post_tags',db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
                db.Column('tag_id',db.Integer,db.ForeignKey('tag.id')))
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'

    )

    def __init__(self,username):
        self.username = username
    def __repr__(self):
        return "<User '{}'>".format(self.username)
class Post(db.Model):

    id = db .Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts',lazy='dynamic')
    )
    def __init__(self,title):
        self.title=title
    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.DateTime(db.DateTime())
    post_id = db.Column(db.Integer(),db.ForeignKey('post.id'))
    def __repr__(self):
        return "<Comment '{ }'>".format(self.text[:15])
class Tag(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    def __init__(self,title):
        self.title=title
    def __repr__(self):
        return "<Tag '{}'>".format(self.title)
@app.route('/')
def htmo():
    return '<h1>Hello World!</h1>'
@app.route('/c')
def home():
    return '<h1>Hello C!</h1>'

if __name__ == '__main__':
    app.run()