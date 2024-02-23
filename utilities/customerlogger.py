import logging

# creating class for logs handling
class LogGen:
        @staticmethod
        def loggen():
            logger = logging.getLogger()
            fhandler = logging.FileHandler(filename=r"C:\Users\USER\PycharmProjects\ArnabNew\Logs\automation.log",
                                           mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
            return logger