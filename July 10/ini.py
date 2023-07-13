def parse(file_name):
    config = {}

    with open(file_name) as file_config:
        config_list = file_config.readlines()

    print(config_list)

    current_section = ''
    for element in config_list:
        element = element.strip()
        if element.count("=") == 1:
            key, value = element.split('=')
            key, value = key.strip(), value.strip()
            if "#" in key or ";" in key:
                continue
            if value.lower() in 'yes, on, true':
                value = 'true'
            elif value.lower() == 'no, of, false':
                value = 'false'
            elif value.isdigit():
                value = int(value)
            if current_section:
                config[current_section][key] = value
            else:
                config[key] = value
        elif element.startswith("[") and element.endswith("]"):
            current_section = element[1:-1]
            config[current_section] = {}
    return config