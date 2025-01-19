import logging

logging.basicConfig(
    level=logging.DEBUG,
     format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("arithmetic operations")


def add(a,b):
    result=a+b
    logger.debug(f"this is a additon of {a}+{b}={result}")

add(10,15)