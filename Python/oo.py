
class Hello:
    def __init__(self,name):
        self._name = name;
    def sayHello(self):
        print("Hello {0}".format(self._name))

class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print("Hi {0}".format(self._name))
    def sayYes(self,Yes,no):
        print("Hi {0}{1}".format(Yes,no))
h = Hello("jikexueyuan")
h.sayHello()

h1 = Hi("jikexueyuan")
h1.sayHi()
h1.sayYes(234,456)