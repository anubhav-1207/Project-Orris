from authentication.auth import auth
from core.engine import *
from core.commands import *
from core.parser import parser 

auth()
kernel()
parser()