import unittest


class NumbersTest(unittest.TestCase):
    def test_even(self):
        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i%2,0)



# class MytestCase(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def test_nothing(self):
#         self.fail("shouldn't happen")
#
#     @unittest.skipIf(mylib.__version__ < (1, 3),
#                      "not supported in this library version")
#     def test_format(self):
#         pass
#
#     @unittest.skipUnless(sys.platform.startswith("win"),"requires Windows")
#     def test_windows_support(self):
#         pass



    # @unittest.skip（原因）
    # 无条件地跳过装饰测试。 理由应该描述为什么跳过测试。
    #
    # @unittest.skipIf（条件，原因）
    # 如果条件为真，则跳过修饰的测试。
    #
    # @unittest.skipUnless条件，原因）
    # 除非条件为真，否则跳过修饰的测试。
    #
    # @unittest.expectedFailure
    #
    # 将测试标记为预期的失败。如果测试在运行时失败，则测试不计为失败。
    #
    # 异常unittest.SkipTest（原因）
    # 引发此异常以跳过测试。
    #
    # 通常你可以使用TestCase.skipTest()
    # 或者一个跳过装饰器而不是直接提升它。