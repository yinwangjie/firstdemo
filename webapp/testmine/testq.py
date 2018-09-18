import unittest

from webapp.hellotest import mydict


class TestDict(unittest.TestCase):
    def test_init(self):
        """初始化"""
        d = mydict.Dict(a=1, b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        """测试1"""
        d = mydict.Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        """测试2"""
        d = mydict.Dict()
        d['key'] = 'value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        """测试3"""
        d = mydict.Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        """测试4"""
        d = mydict.Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
suite = unittest.TestLoader().loadTestsFromTestCase(TestDict)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
#     unittest.main()