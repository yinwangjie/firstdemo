import datetime
from os import path
from sqlalchemy import func
from flask import render_template,Blueprint
from webapp.model import db,User,Post,Comment,Tag,tags
from webapp.forms import CommentForm


bp = Blueprint(
    'blog',
    __name__,
    template_folder='templates/blog',
    url_prefix='/blog'
)

def siderbar_data():
    recent = Post.query.order_by(
        Post.publish_date.desc()
    ).limit(5).all()
    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')).join(
            tags
        ).group_by(Tag).order_by('total DESC').limit(5).all()
    for key in top_tags:
        print(key)
        print('**********************************8888')

    return recent, top_tags