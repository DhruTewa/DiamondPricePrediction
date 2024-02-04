# Create our own cutsom exception class
import sys # to get the system error detail
from src.logger import logging

#this function takes an exception (error) and its details (error_detail from the sys module), 
# extracts relevant information such as the filename and line number where the exception occurred, and then 
# creates and returns a formatted error message containing this information along with the original error message. 
# This kind of function can be useful for logging detailed error information 
# or providing more informative error messages to users.
def error_message_detail(error,error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() # coming from the sys module
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message    

#this CustomException class extends the functionality of the built-in Exception class by providing a detailed error message 
# along with the original error message. The details are captured during the initialization of the exception object, 
# and the __str__ method is implemented to return the detailed error message when the exception object is converted to a string. 
# This can be useful for providing more informative error messages when handling exceptions in your code.

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message) # inherit the error message from the parent class Exception
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
   