class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if self.values:
            return min(self.values)
        return None


class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if self.values:
            return max(self.values)
        return None


class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, number):
        self.values.append(number)

    def result(self):
        if self.values:
            return sum(self.values) / len(self.values)
        return None
values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))