import os
# from os import path
from eakApi import settings
from crequest.middleware import CrequestMiddleware
import json
import datetime
import logging


class Logger(object):
    def __init__(self, moduleName):
        self.moduleName = moduleName.replace('.log','')
    
    def logger(self):
        logger = logging.getLogger('moduleName: %s' % self.moduleName)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_path = settings.LOGGING_DIR
            if not os.path.exists(file_path):
                os.mkdir(file_path)

            date = datetime.datetime.date(datetime.datetime.now())
            day = datetime.datetime.date(datetime.datetime.now()).strftime('%a')
            f = file_path + str(date) +"_" + day
            if os.path.exists(str(f)):
                file_name = os.path.join(f,'%s.log' % self.moduleName)
                handler = logging.FileHandler(file_name)
                formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
                handler.setFormatter(formatter)
                handler.setLevel(logging.DEBUG)
                logger.addHandler(handler)
            else:
                date_folder = file_path +str(date)+ "_" + day +settings.DIR_SLASHES
                os.mkdir(date_folder)

                file_name = os.path.join(date_folder,'%s.log' %self.moduleName)
                handler = logging.FileHandler(file_name)
                formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
                handler.setFormatter(formatter)
                handler.setLevel(logging.DEBUG)
                logger.addHandler(handler)
        self._logger = logger
        return logger
    
    def get(self):
        return self
    
    def concat_msg(self, msg):
        final_msg =''
        try:
            request=CrequestMiddleware.get_request()
            path=''
            params=''
            try:
                path = request.path
            except Exception as e:
                print(e)
            try:
                params= json.dumps(request.data['params'])
            except Exception as e:
                try:
                    params = json.dumps(request.data)
                except Exception as e:
                    params =''
            
            if path != '':
                final_msg = '\nAPI Service: ' + path
            if params != '':
                final_msg = final_msg + '\nAPI Service Params: ' + "\n" + params

            final_msg = final_msg + '\nLog Message: ' + "\n" + msg+ "\n\n"
        except Exception as e:
            final_msg = '\nLog Message: ' + "\n" + msg+ "\n\n"

        return final_msg

    def info(self,msg):
        msg = self.concat_msg(msg)
        self._logger.info(msg)
        print(msg)

    def debug(self,msg):
        self._logger.debug(self.concat_msg(msg))
        print(msg)

    def error(self,msg):
        self._logger.error(self.concat_msg(msg))
        print(msg)

    def critical(self,msg):
        self._logger.critical(self.concat_msg(msg))
        print(msg)

    def warning(self,msg):
        self._logger.warning(self.concat_msg(msg))
        print(msg)



