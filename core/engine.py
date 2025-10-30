from core.parser import parser
def kernel():
    
    while True:
        try:
            line = input('>>> ~$ ')
            command = line.strip().split()
            parser(command,line)

        except KeyError:
            print("Error: Unrecognised Command")

    
    
    
    
        
        

