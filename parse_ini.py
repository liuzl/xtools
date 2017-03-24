'''
parse the ini file for xtools
'''

import ConfigParser
import os

CONFIG_FILE_NAME = 'xtools.ini'
COMMON_SECTION_NAME = 'default'

def parse_config_file():
    ''' parsing xtools config file.
    config file is a INI format text file.
    the DEFAULT section will be inheritted by other section

    ----------------------------------
    [default]
    user = soso
    password = test
    port = 36000

    [wap0]
    host = 192.168.1.100
    -----------------------------------

    '''

    # read config file
    safecfg = ConfigParser.SafeConfigParser()
    config_dir = os.path.dirname(os.path.abspath(__file__))
    safecfg.read(config_dir + '/' + CONFIG_FILE_NAME)
    # parse the config file
    config = {}
    for sec in safecfg.sections():
        config[sec] = safecfg.items(sec)

    common = config.get(COMMON_SECTION_NAME, [])
    # build the dict from config
    xtools_config = {}
    for sec, option_list in config.items():
        option_dict = dict(option_list)
        for key, val in common:
            if key not in option_dict:
                option_dict[key] = val
        xtools_config[sec] = option_dict
    return xtools_config

def record_password(host_info, xtools_config):
    ''' record username and password '''
    if host_info['host'] in xtools_config:
        print host_info['host'], 'config error, please reconfig it'
        return

    config_dir = os.path.dirname(os.path.abspath(__file__))
    fd = file(config_dir + '/' + CONFIG_FILE_NAME, 'a+')

    fd.write('\n')    
    fd.write('[%s]\n' % host_info['host'])    
    default_info = xtools_config.get(COMMON_SECTION_NAME, {})
    for key in ('host', 'username', 'password', 'port'):
        if host_info[key] != default_info.get(key):
            fd.write('%s = %s\n' % (key, host_info[key]))
    fd.close()


def show_available_hosts(xtools_hosts):
    ''' show all hosts '''
    hosts = []
    for name, info in xtools_hosts.items():
        if name == COMMON_SECTION_NAME:
            continue
        hosts.append((name, info['host']))

    print '%-16s %s' % ('name', 'host')
    print '-' * 32
    print '\n'.join(['%-16s %s' % (k, v) for k,v in hosts])    
    print '-' * 32

   
if __name__ == '__main__':
    print parse_config_file()
