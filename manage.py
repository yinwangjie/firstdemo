from flask_script import Manager,Server
from webapp.model import db,User,Post,Comment,Tag
from flask_migrate import Migrate,MigrateCommand
from webapp import app

migrate = Migrate(app,db)

manager = Manager(app)

manager.add_command("Server",Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Post=Post,Comment=Comment,Tag=Tag)

if __name__ == "__main__":
    app.run()
    manager.run()