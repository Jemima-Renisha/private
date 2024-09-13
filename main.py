class x:
    __privatevar = 8
    def __privmeth(self):
        print("It is protected function!")
    def hello():
        print("private variable ", x.__privatevar)

#object creation
obj = x()
x.hello()
x.__privmeth