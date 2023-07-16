import os
import time

from logging_service import LoggingService

logs: LoggingService = LoggingService()
if logs.log_file == None:
    folder = 'logs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    logs.log_file = os.path.join(folder, f'{time.strftime("%Y%m%d_%H%M%S")}.txt')
