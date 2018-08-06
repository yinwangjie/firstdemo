class Config(object):
    pass

class ProdConfig(Config):
    pass

class Home(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True                  #打印查询语句
    SQLALCHEMY_TRACK_MODIFICATIONS = True   #
    SQLALCHEMY_COMMIT_TEARDOWN = True       #

    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost:3306/flask"

