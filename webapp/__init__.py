from flask import Flask,render_template, redirect, url_for
from webapp.config import DevConfig,Config
from webapp.model import db,User,Post,Comment,Tag
from webapp.controllers.blog import bp,siderbar_data
from webapp.forms import CommentForm
import re
import wtforms
import datetime
from flask import g,session,abort
from flask.views import View

app = Flask(__name__)
app.config.from_object(DevConfig)
app.config.from_object(Config)
db.init_app(app)

def custom_email(form,field):
    if not re.match(r"[^@]+@[^@]+\.[^@]+",field.data):
        raise wtforms.ValidationError('Field must be a valid email address.')#自定义检验器

def count_substring(string,sub):
    return string.count(sub)
app.jinja_env.filters['count_substring']=count_substring   #自定义过滤器




@app.before_request
def befor_request():
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.route('/restricted')
def admin():
    if g.user is None:
        abort(403)
    return render_template('admin.html')
@app.errorhandler(404)
def page_not_ound(error):
    return render_template('page_not_found.html'), 404
class GenericView(View):
    def __init__(self,template):
        self.template = template
        super(GenericView,self).__init__()

    def dispatch_request(self):
        return  render_template(self.template)

# app.add_url_rule(
#     '/',view_func=GenericView.as_view(
#         'home',template='home.html'
#     )**********************************************还要编写  路由重复
# )
@app.route('/')
@app.route('/<int:page>')
def home(page=1):
    print('this is home')
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page,10)
    recent, top_tags = siderbar_data()
    return render_template(
        'index.html',
        posts=posts,
        top_tags=top_tags,
        recent=recent
    )


@app.route('/post/<int:post_id>',methods=('GET','POST'))
def post(post_id):
    print('************************************8')
    form = CommentForm()
    print(post_id)
    print(form.name.data)
    new_comment = None
    if form.validate_on_submit():
        new_comment = Comment()
        new_comment.name = form.name.data
        new_comment.text = form.text.data
        new_comment.post_id = post_id
        new_comment.date = datetime.datetime.now()
        db.session.add(new_comment)
        db.session.commit()
    print(new_comment)
    print('到这里了吗')
    print('************************************8')
    post = Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = siderbar_data()
    return render_template(
        'post.html',
        post=post,
        tags=tags,
        comments=comments,
        recent=recent,
        top_tags=top_tags,
        form=form
    )
@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(title=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = siderbar_data()
    return render_template(
        'tag',
        tag=tag,
        posts=posts,
        recent=recent,
        top_tags=top_tags
    )
@app.route('/user/<string:username>')
def user(username):
    user = User.query.filter(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = siderbar_data()
    return render_template(
        'user',
        user=user,
        posts=posts,
        recent=recent,
        top_tags=top_tags
    )
@app.route('/')
def index():
    print('This is home')
    return redirect(url_for('blog.home'))
@bp.route('/c')
def homework():
    return '<h1>Hello C!</h1>'



if __name__ == '__main__':
    app.run()
