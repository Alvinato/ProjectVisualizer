from json import load

PLUMBUM_LOCATION = ""
PATTERN_LOCATION = ""
CONFIG_LOCATION = "config.json"


def load_project_properties():
    try:
        config_file = open(CONFIG_LOCATION, 'r')
        config = load(config_file)
        return config
    except Exception:
        raise Exception("ERROR: Could not load project properties")


if __name__ == '__main__':
    #Test
    dict = load_project_properties()
    print dict