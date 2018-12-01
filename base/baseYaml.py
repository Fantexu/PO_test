import yaml


def get_yaml(yaml_path):
    with open(yaml_path, 'rb') as file:
        data = yaml.load(file.read())
    return data


def set_yaml(yaml_path, data):
    with open(yaml_path, 'wb') as file:
        yaml.dump(data, file)


