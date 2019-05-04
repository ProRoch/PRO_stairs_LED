from LED_program import *



class ClassHolder(object):
    def __init__(self):
        self.classes = {}

    def add_class(self, c):
        self.classes[c.__name__] = c

    def __getitem__(self, n):
        return self.classes[n]

class Foo(object):
    def __init__(self):
        self.a = 0

    def bar(self):
        return self.a + 1

class Spam(Foo):
    def __init__(self):
        self.a = 2

    def bar(self):
        return self.a + 4

class SomethingDifferent(object):
    def __init__(self):
        self.a = "Hello"

    def add_world(self):
        self.a += " World"

    def add_word(self, w):
        self.a += " " + w

    def finish(self):
        self.a += "!"
        return self.a



aclasses = ClassHolder()
aclasses.add_class(prog02)

print( aclasses)

print( "=======")
print( aclasses["prog02"])

print( "=======")
g = aclasses["prog02"]()
g.execute()

print( "Done experiment!")