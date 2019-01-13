"""
Main functionality handled here.
"""

from ruamel.yaml import YAML
from .models import Character, Ruleset


def main():
    yaml = YAML(typ='safe')

    with open("../data/characters.yaml", 'r') as characters_in, \
        open("../data/rulesets.yaml", "r") as rulesets_in:
        characters_data = yaml.load(characters_in)
        characters = [Character(_) for _ in characters_data]
        print(characters)

        rulesets_data = yaml.load(rulesets_in)
        rulesets = [Ruleset(_) for _ in rulesets_data]
        print(rulesets)


if __name__ == "__main__":
    main()
