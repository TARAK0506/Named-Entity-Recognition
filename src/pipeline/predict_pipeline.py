from imports import *

class CustomData:
    def __init__(self,input_file):
        self.input_file=input_file
        pass

    def save_data(self):
        self.input_file.save(os.path.join('artifacts',self.input_file.filename))
        return self.input_file.filename

    def delete_data(self):
        pass

