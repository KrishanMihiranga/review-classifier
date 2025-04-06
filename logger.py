import logging
import sys
# https://docs.python.org/3/library/logging.html

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    
    handlers=[
        logging.FileHandler(filename='logs.log', mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)