class Stat(object):
    """
    represents a single statistical value for characters
    stats determine what moves will be performed and how effective they will be
    """
    name = "New Stat"
    value = 10
    regen = 0

    @classmethod
    def from_data(cls, data):
        stat = stat()
        stat.name = data['name']

        if 'value' in data:
            stat.value = data['power']

        if 'regen' in data:
            stat.regen = data['regen']
        return stat


    def as_data(self):
        data = {
            'name' = self.name,
            'value' = self.value,
            'regen' = self.regen
        }
        return data
