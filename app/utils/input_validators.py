import re

class Validate:
    """ class for validating data input """
    
    @staticmethod
    def validate_empty_string(data_inputed):
        """ check if data is present """
        
        if data_inputed.strip() == "":
            return True
        
        return False
    
    