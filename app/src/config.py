from configparser import ConfigParser
import os
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(os.path.join(os.getcwd() , filename))
    #parser.read(os.path.join(filename))
    print(os.path.join(os.getcwd() , filename))
    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        
        print(os.getcwd())
        print(os.path.isfile(filename))

        print(os.path.join(os.getcwd(), filename))
        print(os.path.isfile(os.path.join(os.getcwd(), filename)))
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)