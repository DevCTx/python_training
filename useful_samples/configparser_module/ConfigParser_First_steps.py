import configparser

def display_info_config(config):
    print('\nSection', config.sections())       # List all the sections except the DEFAULT section

    # DEFAULT values are however accessible in global and are accessible through all sections ('host')
    for section in config.sections():
        print(f'\n[{section}]')
        for option in config[section]:
            print(f'{option} :', config[section][option] )


# 1ST READING : from a file
config = configparser.ConfigParser()
print("\n", config)   # Returns a <configparser.ConfigParser object>

print('\n', config.read('config.ini'))
display_info_config(config)


# 2ND READING : from a dictionary
config = configparser.ConfigParser()
print("\n", config)   # Returns a <configparser.ConfigParser object>

dictionary = {
    'DEFAULT' : { 'host' : 'localhost'},
    'mariadb' : { 'name' : 'new', 'user' : 'root', 'password' : 'pswd' },
    'redis' : { 'port' : 1234, 'db' : 'sqlite', 'dns' : 'redis://%(host)s' },   # Use of an inside variable
}

print('\n', config.read_dict(dictionary), ':', dictionary)
display_info_config(config)                                                     # The correct variable can be printed


# 3RD WRITING : simple values
for (key,value) in dictionary.items() :         # "config = dictionary" won't work !
    config[ key ] = value                                                       # But is not correctly copied
with open('config2.ini','w') as configfile:
    config.write(configfile)


# 4RD WRITING : values with variables
for (key,value) in dictionary.items() :
    for (k,v) in config[ key ].items():                                         # And should be copied going deeply
        if config[key][k] not in config['DEFAULT'].values():                    # looking at DEFAULT as well
            config[key][k]= v
with open('config3.ini','w') as configfile:
    config.write(configfile)