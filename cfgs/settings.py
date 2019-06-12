import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = "%s\\dbs\\" % BASE_DIR
sys.path.append(BASE_DIR)

LOG_LEVEL = logging.DEBUG  # 设置日志级别
LOG_PATH = os.path.join(BASE_DIR, "logs\\")
LOG_FORMAT = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT, datefmt='%Y-%m-%d %I:%M:%S %p')

formatter = logging.Formatter('%(levelname)s : %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)




if __name__ == "__main__":
    logging.debug(DB_PATH)
    # print(LOG_PATH)
