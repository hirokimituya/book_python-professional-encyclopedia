import yaml

with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data)
    print(type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])
