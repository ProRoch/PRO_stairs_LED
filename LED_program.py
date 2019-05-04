import os


program_List = []
program = {"name":"running light", "description": "one led moving from begin to end", "progName": "prog_1"}
program_List.append(program)
program = {"name":"step by step: UP", "description": "single step lighting one by one in UP direction", "progName": "prog_2"}
program_List.append(program)
program = {"name":"step by step: DOWN", "description": "single step lighting one by one in DOWN direction", "progName": "prog_3"}
program_List.append(program)


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