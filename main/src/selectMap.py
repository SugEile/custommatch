import random

class selectMap:
    @classmethod
    def selectMap():
        maps = [
            'マップ1',
            'マップ2',
            'マップ3',
            'マップ4']
        index = random.randint(0, len(maps) - 1)
        map = maps[index]
        return map