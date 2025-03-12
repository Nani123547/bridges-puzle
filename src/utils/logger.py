# logger.py

import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    setup_logger()
    logging.debug("Logger is set up.")
