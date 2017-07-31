"""
Flight Duration Enhancement System Start
"""

import sys
import os
sys.path.insert(1,os.getcwd())

import time
# import math
from pymavlink import mavutil
from dronekit import connect #, VehicleMode, LocationGlobal, GPSInfo, Vehicle, MAVConnection
import uas_config
# import fdes_fwk_start


class UAS(object)
    def __init__(self):
    #Connect to the vehicle with dronekit
        self.vehicle = self.get_vehicle_with_dronekit()

        self.vehicle_cmds = None

        self.vehicle_pos = None
        self.home_initialised = False
        self.last_home_check = time.time()
        self.mission_cmds = None


     #Definition of function to connect with the vehicle
    def get_vehicle_with_dronekit(self):
        connection_str = uas_config.UASConfig.get_string('dronekit','connection_string','/dev/ttyUSB0')
        connection_baud = uas_config.UASConfig.get_integer('dronekit','baud',921600)
        print "connecting to vehicle on %s, baud=%d" % (connection_str, connection_baud)
        return connect(connection_str, baud=connection_baud)

    def fetch_mission(self):
        print "fetching mission.."
        self.mission_cmds = self.vehicle.commands
        self.mission_cmds.download()
        self.mission_cmds.wait_ready()
        if not self.mission_cmds is None:
            print "mission with %d commands" % self.mission_cmds.count
        else
            print "failed to retrieve mission"

   #Start Vehicle at Home position and check for home within a period of time
    def check_home(self):
        if self.home_initialised:
            return True

        #check if a vehicle is connected
        if self.vehicle is None
            self.vehicle = self.get_vehicle_with_dronekit()
            return False

        if self.mission_cmds is None:
            self.fetch_mission()
            return False

        #check vehicle global position
        if self.vehicle.location.global_relative_frame = is None:
            print "waiting for vehicle position.."
            return False
        if self.vehicle.location.global_relative_frame.lat is None or self.vehicle.location.global_relative_frame.lon is None or self.vehicle.location.global_relative_frame.alt is None:
            print "waiting for vehicle position.."
            return False

        #check vheicle
        if self.vehicle.home_location is None:
            print "waiting for home location.."
            self.fetch_mission()
            return False

    def run(self):
        while True:
            self.check_home()
            print  "Latitude Test is %d" self.vehicle.location.global_frame.alt
            


strat = UAS()
strat.run()