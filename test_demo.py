class Test_DemoClass:
    def test_demoFunc(self):
        print("demo test")
    def demoFunc(self):#test_ ön eki olmadığı için test olarak sayılmıyor
        print("demo function test") 

class DemoClass:#test_ ön eki olmadığı için test olarak sayılmıyor
    def deneme(self):
        print("deneme")