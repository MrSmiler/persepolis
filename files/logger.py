import logging, platform, os

os_type = platform.system()

home_address = os.path.expanduser("~")

if os_type == 'Linux' or os_type == 'FreeBSD' :
    config_folder = os.path.join(str(home_address) , ".config/persepolis_download_manager" )
elif os_type == 'Darwin':
    config_folder = os.path.join(str(home_address) , "Library/Application Support/persepolis_download_manager")
elif os_type == 'Windows' :
    config_folder = os.path.join(str(home_address) , 'AppData\Local\persepolis_download_manager')

#log file address
log_file = os.path.join(str(config_folder), 'persepolisdm.log')

# define logging object
logObj = logging.getLogger(__name__)
logObj.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler(log_file)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logObj.addHandler(handler)

def sendToLog(text="", type="INFO"):
    if type == "INFO":
        logObj.info(text)
    elif type == "ERROR":
        logObj.error(text)
    else:
        logObj.warning(text)