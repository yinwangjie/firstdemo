# def fab(max):
#    n, a, b = 0, 0, 1
#
#    while n < max:
#        print (b)
#        a, b = b, a + b
#        n = n + 1
#
# fab(5)

# class Fab(object):
#
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
#
# if __name__ == "__main__":
#     for n in Fab(5):
#         print(n)




# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print b
#         a, b = b, a + b
#         n = n + 1
# for n in fab(5):
#     print (n)
#
# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
#
# mygenerator = createGenerator()
# print(mygenerator)
#
# for i in mygenerator:
#     print(i)