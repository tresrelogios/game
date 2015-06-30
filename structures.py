from GLOBS import *

class Building(object):
    """Building class"""
    def __init__(self, name, level, cost, increment):
        """Initializes the building; Does type checking"""

        if name in BUILDING_NAMES:
            self.name = name
        else:
            if type(name) != str:
                raise TypeError("Building name should be a string")
            else:
                raise ValueError("Unknown building name {}".format(name))

        if type(level) == int:
            if level > -1:
                self.level = level
            else:
                raise ValueError("Building level should be a non-negative int")
        else:
            raise TypeError("Building level should be of type int")
    
        if type(cost) == dict:
            if len(cost) != len(RESOURCES):
                raise ValueError("Cost dict of wrong size", len(cost),
                                "should be", len(RESOURCES))
            for r in RESOURCES:
                val = cost.get(r, None)
                if type(val) != int:
                    if val is None:
                        raise KeyError(r, "cost missing")
                    else:
                        raise TypeError("Cost value should be an int")
                elif val < 0:
                    raise ValueError("Cost value should not be negative")
            self.cost = cost
        else:
            raise TypeError("Resource costs should be a dictionary")

        if type(increment) == float and 1 <= increment <= 2:
            self.increment = increment
        else:
            if type(increment) != float:
                raise TypeError("Increment value should be a float")
            else:
                raise ValueError("Increment value should be bounded by 1 and 2")

    def level_up(self):
        self.level += 1
        for resource in self.cost:
            self.cost[resource] = int(self.cost[resource]*increment)
