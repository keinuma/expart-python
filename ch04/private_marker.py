class UnforgivingElephant(object):
    def __init__(self, name):
        self.name = name
        self._people_to_stomp_on = []

    def get_slapped_by(self, name):
        self._people_to_stomp_on.append(name)
        print('痛い!')

    def revenge(self):
        print('10年後...')
        for person in self._people_to_stomp_on:
            print('%s は %s を踏みつける' % (self.name, person))
