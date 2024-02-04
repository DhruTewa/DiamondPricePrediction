#import logging
#import os
#from datetime import datetime as dt


#this line of code is creating a log file name based on the current date and time, 
# and the resulting name is stored in the variable LOG_FILE. 
# The format of the log file name includes month, day, year, 
# hour, minute, and second, separated by underscores, and ends with the ".log" extension. 
# This ensures that each log file has a unique and identifiable name based on when it was created.

#LOG_FILE = f"{dt.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#this line of code is creating a full file path for a log file, considering the current working directory, a folder named "logs," 
# and a specific log file name stored in the variable LOG_FILE. 
# This logs_path can then be used to reference the log file in the program.

#logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

#make sure the logs directory exists, and if it doesn't, create it using the os.makedirs() function.
# This function creates a directory and all its parent directories if they don't exist.
#os.makedirs(logs_path, exist_ok=True)

#
#LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)   # logs/09_15_2021_12_00_00.log

#this code configures the logging system to write log messages to a specified log file (LOG_FILE_PATH), 
# with a logging level of INFO or higher, and a specific format for each log entry that includes a timestamp, line number, 
# logger name, log level, and the log message itself. 
# This configuration is commonly used to create structured and informative log entries for debugging and monitoring purposes.

import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)