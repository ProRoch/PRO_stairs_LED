import os


program_List = []
program = {"name":"running light", "description": "one led moving from begin to end"}
program_List.append(program)
program = {"name":"step by step: UP", "description": "single step lighting one by one in UP direction"}
program_List.append(program)
program = {"name":"step by step: DOWN", "description": "single step lighting one by one in DOWN direction"}
program_List.append(program)


class LedProgram:
    time = 60

    def __init__(self, time, *args, **kwargs):

        self.time = time
