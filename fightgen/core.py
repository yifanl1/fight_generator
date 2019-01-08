from ruamel.yaml import YAML

def main():
    yaml = YAML(typ='safe')

    with open("../data/characters.yaml", 'r') as characters_in, \
        open("../data/rulesets.yaml", "r") as rulesets_in:
        characters_data = yaml.load(characters_in)

        rulesets_data = yaml.load(rulesets_in)


if __name__ == "__main__":
    main()