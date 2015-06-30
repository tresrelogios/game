class Building(object):
    """Building class"""
    def __init__(self, name, level, cost, increment):
        self.name = name
        self.level = level
        self.cost = cost
        self.increment = increment

    def level_up(self):
        self.level += 1
        for resource in self.cost:
            self.cost[resource] = int(self.cost[resource]*increment)

def outronome():
    return "fuck you"
