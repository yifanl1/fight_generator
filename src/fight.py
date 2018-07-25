from character import Character

class Fight(object):
    """
    Models the simulation of a fight
    Every fight will have a common pool of moves that all characters can use, in addition to character specific moves
    Every fight will have some set of conditions to determine victory, such as running out of stamina, tapping out, etc
    """
    def __init__(self, name="New Fight", standard_moves=[], common_stats=[], win_conditions=[]):
        super(Fight, self).__init__()
        self.name = name
        self.standard_moves = standard_moves
        self.common_stats = common_stats
        self.win_conditions = win_conditions

    """
    Simulate one round of combat between two characters
    FLow of a round is as follows:
        1. determine who makes the move
        2. determine what move the character decided in step 1 makes
        3. determine if the move succeeds or not
        4a. if the move succeeds, apply any damage and other modifiers to characters
        4b. if the move fails, determine what counter attack,
               if any, the other character makes, and apply the results to characters
        5. determine if the fight is won

    """
    def one_round(self, character_1, character_2):
        pass