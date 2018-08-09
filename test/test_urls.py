import unittest
from main import  db
class TestURLs(unittest.TestCase):
    print("11111")
    def setUp(self):

        admin._views=[]
        rest_api.resources = []

        app = create_app('webapp.config.TestConfig')
        self.client = app.test_client()

        db.app = app

        db.create_all

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_root_redirect(self):
        """检测根路径是否返回了302"""
        result = self.client.get('/')
        assert result.status_code == 302
        assert "/blog/" in result.headers['Location']



if __name__ == "main":
    unittest.main()