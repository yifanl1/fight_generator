class Stat(object):
    """
    represents a single statistical value for characters
    stats determine what moves will be performed and how effective they will be
    """
    def __init__(self, name="New Stat", default_value=10):
        super(Stat, self).__init__()
        self.name = name
        self.default_value = None
        self.current_value = default_value
        self.recovery_per_turn = 0


class PersistantStat(Stat):
    """
    A persistant stat is a stat that will generally stay static throughout a fight
    For instance, strength or intelligence in classical RPG terms
    """
    def __init__(self, name="New Persistant Stat", default_value=10):
        super(PersistantStat, self).__init__(name, default_value)


class ResourceStat(Stat):
    """
    A resource stat is a stat that will generally be spent throughout a fight
    For instance, health or mana in classical RPG terms
    They may recover a certain amount each round
    """
    def __init__(self, name="New Resource Stat", default_value=10, recovery_per_turn=0):
        super(ResourceStat, self).__init__(name, default_value)
        self.recovery_per_turn = recovery_per_turn


class UnmodifiableStat(Stat):
    """
    An unmodifiable stat is a stat that is not modified by moves
    For instance, gender or hair colour in classical RPG terms
    """

    def __init__(self, name="New Unmodifiable Stat", default_value=""):
        super(UnmodifiableStat, self).__init__(name, default_value)