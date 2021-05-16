import logging

logging.basicConfig(filename="newfile.log", format='%(asctime)s : %(name)s :  %(levelname)s:  %(message)s',
                    filemode='a')
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

logger.debug("this is debug level")
logger.info("hi this is info level")
logger.warning("this is warning level")
logger.error("this is error level")
logger.critical("this is critical level")
