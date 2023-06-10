import logging
import os

logger = logging.getLogger(__name__)
logger.debug("This message should go to the log file")
logger.debug(f'{os.getcwd()=}')
logger.info("So should this")
logger.warning("And this, too")
logger.error("And non-ASCII stuff, too, like Øresund and Malmö")
