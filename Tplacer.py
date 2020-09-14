'''
This Program is a 
'''



class pin ():
    "every pin on a transistor"
    def __init__ (self, name , np , gd):
        #pin name
        self.name = name
        #this pin is belong to which type of transistor.
        #N = 0, P = 1
        self.np = np
        #this pin is a gate or diffusion.
        self.gd = gd
        self.path = {}
        self.branch = 0

    def connect (self,target):
        try:
            self.path[target] += 1
        except KeyError:
            self.path[target] = 1
        self.branch += 1



script_dir = os.path.dirname(__file__) 
file_name = input_file_name
rel_path = file_name                               
abs_file_path = os.path.join(script_dir, rel_path)      #trans local file path to system path
with open(abs_file_path ,'rU') as f:
    line_count = len(f.readlines())

while input_line<=line_count:
    
    
