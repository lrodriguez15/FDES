"""
Flight Duration Enhancement System Start
"""

import sys
import os
sys.path.insert(1,os.getcwd())

import time
import math
from pymavlink import mavutil
from dronekit import connect, VehicleMode, LocationGlobal, GPSInfo, Vehicle, MAVConnection

class UAS(object)

    #Connect to the vehicle with dronekit
    self.vehicle = self.get_vehicle_with_dronekit()

def get_vehicle_with_dronekit(self):
    connection_str = uas_config.config.get_string('dronekit','connection_string','/dev/ttyUSB0')
    connection_baud = uas_config.config.get_integer('dronekit','baud',921600)
    print "connecting to vehicle on %s, baud=%d" % (connection_str, connection_baud)
    return connect(connection_str, baud=connection_baud)
    print "connected to vehicle"