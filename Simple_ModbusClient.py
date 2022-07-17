#!/bin/python

from pyModbusTCP.client import ModbusClient #, DataBank
from time import sleep


# Create an instance of ModbusServer
client = ModbusClient("127.0.0.1", 4196)
client.open()

print(client.read_holding_registers(1))
sleep(1)
print(client.read_holding_registers(1))

sleep(1)
print(client.read_holding_registers(1))
sleep(1)
client.write_single_register(1,100)
