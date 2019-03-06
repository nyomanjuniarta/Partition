class PatternConfig:
    def __init__(self, theta=1):
        self.theta = theta


class Pattern:
    def __init__(self, instance=None, dirty=True, config=None, object=-1):
        self.objects = []
        self.partition = set()
        if not config:
            self.cfg = PatternConfig(1)
        else:
            self.cfg = config

        if dirty:
            self.partition = self.pattern_parser(instance)
            self.objects.append(object)

    def pattern_parser(self, line):
        attribute_index = 0
        attribute_list = list()
        numbers = line.split()
        partition = set()
        for n in numbers:
            attribute_list.append((attribute_index, n))
            attribute_index += 1
        attribute_list.sort(key=lambda tup: tup[1])

        partition_element = set()
        before = '?'
        for attribute in attribute_list:
            if attribute[1] != before and before != '?':
                partition.add(frozenset(partition_element))
                partition_element = set()
            partition_element.add(attribute[0])
            before = attribute[1]
        partition.add(frozenset(partition_element))
        return partition

    def intersect(self, other):
        pi = Pattern(instance=None, config=self.cfg, dirty=False)
        for element1 in self.partition:
            for element2 in other.partition:
                common = element1.intersection(element2)
                if len(common) > 0:
                    pi.partition.add(frozenset(common))
        return pi

    def __eq__(self, other):
        if self.partition == other.partition:
            return True
        return False

    def __le__(self, other):
        pi = self.intersect(other)
        if pi == self:
            return True
        return False

    def size(self):
        return len(self.objects)

    def __repr__(self):
        output = ''
        for partition_element in self.partition:
            for item in partition_element:
                output += str(item) + ' '
            output += '|'
        return output[:-1]
