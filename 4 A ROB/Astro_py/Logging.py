from logzero import logger, logfile
from time import sleep

logfile("events.log")

for i in range(10):
    logger.info(f"Loop number {i+1} started")
    logger.warning(f"Warning all'iterazione {i+1}")
    logger.error(f"Errore all'iterazione {i+1}")
    logger.debug(f"Debug all'iterazione {i+1}")
    sleep(60)