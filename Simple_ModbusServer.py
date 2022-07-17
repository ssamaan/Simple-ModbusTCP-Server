#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import logging
logger = logging.getLogger('ftpuploader')
# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 4196, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [1]
    while True:
        server.data_bank.set_holding_registers(1, [int(uniform(0, 100))])
        if state != server.data_bank.get_holding_registers(1):
            state = server.data_bank.get_holding_registers(1)
            print("Value of Register 1 has changed to " +str(state))
        sleep(0.5)

except  Exception as e:
    logger.error('Failed to upload to ftp: '+ str(e))
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")

