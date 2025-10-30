import sys
from core import commands
from data.system.system_info import osinfo,cpuinfo,raminfo

def parser(command,line):
    func = command[0]
    
    if line == 'exit':
        sys.exit()
    
    elif line == 'who am i':
        commands.user_show()

    elif line == 'osinfo':
        osinfo()

    elif line == 'cpuinfo':
        cpuinfo()

    elif line == 'raminfo':
        raminfo()

    
