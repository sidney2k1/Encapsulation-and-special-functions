class myclass:
    __privatevar=27
    def __privmeth(self):
        print("Im inside class myclass")
    def hello(self):
        print("The private variable is:",myclass.__privatevar)
foo=myclass()
foo.hello()
foo.__privmeth