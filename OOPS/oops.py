class Test:
    x=6
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        
    def f1(self):
        print('hello world')
    @staticmethod
    def f2():
        pass
    @classmethod
    def f3(cls):
        print(cls.x)
        
        
        
t1 = Test(1,2)
t1.f1()
Test.f3()
# To create Instance Variable we create init method....