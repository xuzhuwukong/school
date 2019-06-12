from cfgs import settings
import logging
import traceback

def loggerInFile(filename):  # 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
    def decorator(func):
        def inner(*args, **kwargs):  # 1
            logFilePath = settings.LOG_PATH + filename
            logger = logging.getLogger()
            logger.setLevel(settings.LOG_LEVEL)
            # sh = logging.StreamHandler()
            handler = logging.FileHandler(logFilePath)
            handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))
            logger.addHandler(handler)
            try:
                #print("Arguments were: %s, %s" % (args, kwargs))
                # logger.info(args)
                logger.info(args)
                result = func(*args, **kwargs)  # 2
            except:
                logger.error(traceback.format_exc())

        return inner

    return decorator