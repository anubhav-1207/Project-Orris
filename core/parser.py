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
    
    elif func == 'mkdir' :
        try:
            dir_name = command[1]
            commands.mkdir(dir_name)
        except KeyError:
            print("Error: Invalid DIR Arguement")
    
    elif func == 'init':
        try:
            file_namepath = command[1]
            commands.init(file_namepath)
        except KeyError:
            print("Error: Invalid File Name/Path")

    elif func == 'rid' and command[1] == 'f':
        try:
            file_namepath = command[2]
            commands.rid(file_namepath)
        except KeyError:
            print("Error: Invalid File Name/Path")