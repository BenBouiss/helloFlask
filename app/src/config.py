from configparser import ConfigParser
import os
import pathlib

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    print('Loading config')
    Cur_path = pathlib.Path(__file__).parent.absolute()
    Target_file = os.path.join(Cur_path , filename)
    parser.read(Target_file)
    # get section, default to postgresql
    config = {} 
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        print('Ben')
        print(os.getcwd())
        print(Target_file)
        print(os.path.isfile(Target_file))
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)
