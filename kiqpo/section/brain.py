import sys

def brain(command):
    """
    ### Brain of Kiqpo CLI
    ##### Validated give command and run it.
    @command : user entered command.\n
    """
    if(command==None):
        sys.exit()
    else:
        if(command=="cerate"):
            print('cerate')
        elif(command=="run-web"):
            print('run-web')
        elif(command=="run-desktop"):
            print('run-desktop')