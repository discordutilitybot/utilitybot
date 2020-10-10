import os

class OptionConfigErorr(Exception):
    def __init__(self, *args):
        self.config = args[0]

    def __str__(self):
        return f'{self.config} has an invalid config'

# Used when a module/cog is not found in local directores
class InvalidModuleErorr(Exception):
    def __init__(self, *args):
        self.module = args[0]

    def __str__(self):
        return f'{self.module} is invalid. and or does not exist'