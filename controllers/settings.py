from json import load

CONFIG_LOCATION = "config.json"

def load_project_properties():
    try:
        config_file = open(CONFIG_LOCATION, 'r')
        config = load(config_file)
        return config
    except Exception:
        raise Exception("ERROR: Could not load project properties")

if __name__ == '__main__':
    # Test
    properties = load_project_properties()
    print "config.json\n", properties
