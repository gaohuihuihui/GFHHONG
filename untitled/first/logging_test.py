import logging

logger=logging.getLogger("mylog")
logger.setLevel(logging.DEBUG)

#创建一个handler
fh=logging.FileHandler("log.txt")
ch=logging.StreamHandler()

logger.addHandler(ch)
logger.addHandler(fh)

formatter=logging.Formatter('%(lineno)d[%(asctime)s][%(levelname)s]:%(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.debug("nihao")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")