class Test_DemoClass:
    # her testeten önce çağrılır
    def setup_method(self):
        print("1")

    # her testen sonra çağırılır
    def teardown_method(self):
        print("2")

    # setup -> test_demoFunc -> teardown
    def test_demoFunc(self):
        #3A Act Arrange Assert
        text="Hello"
        assert text=="Hello"
    
    def demoFunc(self):#test_ ön eki olmadığı için test olarak sayılmıyor
        print("demo function test") 
    
    #setup -> test_demo2 -> teardown
    def test_demo2(self):
        assert True

class DemoClass:#test_ ön eki olmadığı için test olarak sayılmıyor
    def deneme(self):
        print("deneme")