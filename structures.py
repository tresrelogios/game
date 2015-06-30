from global_vars import *

class Building(object):
    """Building class"""
    def __init__(self, name, level, cost, increment):
        """Initializes the building; Does type checking"""

        if type(name) == str and name:
            self.name = name
        else:
            raise TypeError("Building name should be a non-empty string")

        if type(level) == int:
            if level > -1:
                self.level = level
            else:
                raise ValueError("Building level should be a non-negative int")
        else:
            raise TypeError("Building level should be of type int")
    
        if type(cost) == dict:
            for r in RESOURCES:
                pass
        else:
            raise TypeError("Resource costs should be a dictionary")
        self.increment = increment

    def level_up(self):
        self.level += 1
        for resource in self.cost:
            self.cost[resource] = int(self.cost[resource]*increment)

def outronome():
    return "fuck you"
