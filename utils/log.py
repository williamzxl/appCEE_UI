import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH, Config


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        cfgs = Config().get('log-Cfg')
        for cfg in cfgs:
            self.log_file_name = cfg.get('file_name') if cfg and cfg.get('file_name') else 'test.log'
            self.backup_count = cfg.get('backup') if cfg and cfg.get('backup') else 10
            self.console_output_level = cfg.get('console_level') if cfg and cfg.get('console_level') else 'WARNING'
            self.file_output_level = cfg.get('file_level') if cfg and cfg.get('file_level') else 'DEBUG'
            pattern = cfg.get('pattern') if cfg and cfg.get('pattern') else \
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            self.formatter = logging.Formatter(pattern)
            self.filename = LOG_PATH + "\\" + self.log_file_name

    # @classmethod
    # def get_cfg(cls):
    #     cfgs = Config().get('log-Cfg')
    #     for cfg in cfgs:
    #         cls.log_file_name = cfg.get('file_name') if cfg and cfg.get('file_name') else 'test.log'
    #         cls.backup_count = cfg.get('backup') if cfg and cfg.get('backup') else 10
    #         cls.console_output_level = cfg.get('console_level') if cfg and cfg.get('console_level') else 'WARNING'
    #         cls.file_output_level = cfg.get('file_level') if cfg and cfg.get('file_level') else 'DEBUG'
    #         pattern = cfg.get('pattern') if cfg and cfg.get('pattern') else \
    #             '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    #         cls.formatter = logging.Formatter(pattern)
    #         cls.filename = LOG_PATH + "\\" + cls.log_file_name

    def get_logger(self):
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=self.filename,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)

        return self.logger


logger = Logger().get_logger()
