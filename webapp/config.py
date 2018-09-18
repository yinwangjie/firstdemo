import tempfile

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = "623f3768bfebbe1ea2cc03ea2aa5baef"
    #cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32在Bush中生成秘钥的指令

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

class TestConfig(Config):
    db_file = tempfile.NamedTemporaryFile()

    DEBUG = True
    DEBUG_TB_ENABLED=False

    SQLALCHEMY_DATABASE_URI = "mysql://root:1234@localhost:3306/flask"

    CACHE_TYPE = 'null'
    WTF_CSRF_ENALBED = False

    CELERY_BROKER_URL = ""
    CELERY_BACKEND_URL = ""

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = "username"
    MAIL_PASSWORD = "password"