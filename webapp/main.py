# from flask import Flask,render_template
# from webapp.config import DevConfig,Config
# from sqlalchemy import func
# from  flask_wtf import Form
# from wtforms import StringField,TextAreaField
# from wtforms.validators import DataRequired,Length
# import re
# import wtforms
# import datetime
# from flask import g,session,abort,Blueprint
# from flask.views import View
#
# app = Flask(__name__)
# app.config.from_object(DevConfig)
# app.config.from_object(Config)
# bp = Blueprint(
#     'blog',
#     __name__,
#     template_folder='templates/blog',
#     url_prefix='/blog'
# )
# def custom_email(form,field):
#     if not re.match(r"[^@]+@[^@]+\.[^@]+",field.data):
#         raise wtforms.ValidationError('Field must be a valid email address.')#自定义检验器
# class CommentForm(Form):    #字段、检验器、表单组成flask_wtf
#     name = StringField(
#         'Name',
#         validators=[DataRequired(),Length(max=255)]
#     )
#     text = TextAreaField(u'Comment', validators=[DataRequired()])
# def count_substring(string,sub):
#     return string.count(sub)
# app.jinja_env.filters['count_substring']=count_substring   #自定义过滤器
#
#
#
#
# @app.before_request
# def befor_request():
#     if 'user_id' in session:
#         g.user = User.query.get(session['user_id'])
#
# @app.route('/restricted')
# def admin():
#     if g.user is None:
#         abort(403)
#     return render_template('admin.html')
# @app.errorhandler(404)
# def page_not_ound(error):
#     return render_template('page_not_found.html'), 404
# class GenericView(View):
#     def __init__(self,template):
#         self.template = template
#         super(GenericView,self).__init__()
#
#     def dispatch_request(self):
#         return  render_template(self.template)
#
# app.add_url_rule(
#     '/',view_func=GenericView.as_view(
#         'home',template='home.html'
#     )
# )
# class User(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer(),primary_key=True)
#     username = db.Column(db.String(255))
#     password = db.Column(db.String(255))
#     sex = db.Column(db.String(255))
#     posts = db.relationship(
#         'Post',
#         backref='user',
#         lazy='dynamic'
#
#     )
#
#     def __init__(self,username):
#         self.username = username
#     def __repr__(self):
#         return "<User '{}'>".format(self.username)
#
# class Post(db.Model):
#
#     id = db .Column(db.Integer(),primary_key=True)
#     title = db.Column(db.String(255))
#     text = db.Column(db.Text())
#     publish_date = db.Column(db.DateTime())
#     comments = db.relationship(
#         'Comment',
#         backref='post',
#         lazy='dynamic'
#     )
#     user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
#     tags = db.relationship(
#         'Tag',
#         secondary=tags,
#         backref=db.backref('posts',lazy='dynamic')
#     )
#     def __init__(self,title):
#         self.title=title
#     def __repr__(self):
#         return "<Post '{}'>".format(self.title)
#
#
# class Comment(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(255))
#     text = db.Column(db.Text())
#     date = db.Column(db.DateTime())
#     post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
#     # def __repr__(self):
#     #     return "<Comment '{ }'>".format(self.text[:15])
# class Tag(db.Model):
#     id = db.Column(db.Integer(),primary_key=True)
#     title = db.Column(db.String(255))
#     def __init__(self,title):
#         self.title=title
#     def __repr__(self):
#         return "<Tag '{}'>".format(self.title)
#
#
# def siderbar_data():
#     recent = Post.query.order_by(
#         Post.publish_date.desc()
#     ).limit(5).all()
#     top_tags = db.session.query(
#         Tag, func.count(tags.c.post_id).label('total')).join(
#             tags
#         ).group_by(Tag).order_by('total DESC').limit(5).all()
#     for key in top_tags:
#         print(key)
#         print('**********************************8888')
#
#     return recent, top_tags
# @bp.route('/')
# @bp.route('/<int:page>')
# def home(page=1):
#     posts = Post.query.order_by(Post.publish_date.desc()).paginate(page,10)
#     recent, top_tags = siderbar_data()
#     return render_template(
#         'index.html',
#         posts=posts,
#         top_tags=top_tags,
#         recent=recent
#     )
#
#
# @bp.route('/post/<int:post_id>',methods=('GET','POST'))
# def post(post_id):
#     print('************************************8')
#     form = CommentForm()
#     print(post_id)
#     print(form.name.data)
#     new_comment = None
#     if form.validate_on_submit():
#         new_comment = Comment()
#         new_comment.name = form.name.data
#         new_comment.text = form.text.data
#         new_comment.post_id = post_id
#         new_comment.date = datetime.datetime.now()
#         db.session.add(new_comment)
#         db.session.commit()
#     print(new_comment)
#     print('到这里了吗')
#     print('************************************8')
#     post = Post.query.get_or_404(post_id)
#     tags = post.tags
#     comments = post.comments.order_by(Comment.date.desc()).all()
#     recent, top_tags = siderbar_data()
#     return render_template(
#         'post.html',
#         post=post,
#         tags=tags,
#         comments=comments,
#         recent=recent,
#         top_tags=top_tags,
#         form=form
#     )
# @bp.route('/tag/<string:tag_name>')
# def tag(tag_name):
#     tag = Tag.query.filter_by(title=tag_name).first_or_404()
#     posts = tag.posts.order_by(Post.publish_date.desc()).all()
#     recent, top_tags = siderbar_data()
#     return render_template(
#         'tag',
#         tag=tag,
#         posts=posts,
#         recent=recent,
#         top_tags=top_tags
#     )
# @bp.route('/user/<string:username>')
# def user(username):
#     user = User.query.filter(username=username).first_or_404()
#     posts = user.posts.order_by(Post.publish_date.desc()).all()
#     recent, top_tags = siderbar_data()
#     return render_template(
#         'user',
#         user=user,
#         posts=posts,
#         recent=recent,
#         top_tags=top_tags
#     )
# # @app.route('/')
# # def index():
# #     return redirect(url_for('blog.home'))
# @bp.route('/c')
# def homework():
#     return '<h1>Hello C!</h1>'
#
#     db.session.commit()
#
# if __name__ == '__main__':
#     app.register_blueprint(bp)
#     app.run()
