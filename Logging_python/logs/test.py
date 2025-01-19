import logging
#configure logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
                    )

def add(a,b):
    logging.debug("this is a addition of two numbers")
    return a + b
logging.debug("this is a addition function")
add(10,5)