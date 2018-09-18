from webapp.main import User,Tag,Post,db
import random
import datetime

def add():
    user = User.query.get(1)
    tag_one = Tag('Python')
    tag_two = Tag('Flask')
    tag_three = Tag('SQLAlechemy')
    tag_four = Tag('Jinja')
    tag_list = [tag_one,tag_two,tag_three,tag_four]
    s = "Example text"
    for i in range(100):
        new_post = Post("Post "+str(i))
        new_post.user = user
        new_post.publish_date = datetime.datetime.now()
        new_post.text = s
        new_post.tags = random.sample(tag_list,random.randint(1,3))
        db.session.add(new_post)
    db.session.commit()

if __name__ =="__main__":
    add()