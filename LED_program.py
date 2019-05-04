import os


program_List = []
program = {"name":"running light", "description": "one led moving from begin to end", "progName": "prog_01"}
program_List.append(program)
program = {"name":"step by step: UP", "description": "single step lighting one by one in UP direction", "progName": "prog_02"}
program_List.append(program)
program = {"name":"step by step: DOWN", "description": "single step lighting one by one in DOWN direction", "progName": "prog_03"}
program_List.append(program)



class ClassHolder(object):
    def __init__(self):
        self.classes = {}

    def add_class(self, c):
        self.classes[c.__name__] = c

    def __getitem__(self, n):
        return self.classes[n]

def initClassHolder():
    list_Classes = ClassHolder()
    list_Classes.add_class(prog_01)
    list_Classes.add_class(prog_02)
    list_Classes.add_class(prog_03)
    return list_Classes


class LedProgram:
    deltaTime = 60
    strip_lenght = 1

    def __init__(self, strip_lenght, deltaTime, *args, **kwargs):

        self.time = deltaTime
        self.strip_lenght = strip_lenght

class prog_01(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_01, self).__init__(lenght, deltaTime)

    def execute(self):
        print("Prog_1 just started.")

class prog_02(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_01, self).__init__(lenght, deltaTime)
        print("se jestem prog-02")
    def execute(self):
        print("Prog_2 just started.")


class prog_03(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_01, self).__init__(lenght, deltaTime)
        print("se jestem prog-03")
    def execute(self):
        print("Prog_3 just started.")
