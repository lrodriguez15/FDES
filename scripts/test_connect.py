from dronekit import connect #, VehicleMode, LocationGlobal, GPSInfo, Vehicle, MAVConnection
import time

class UAS(object):
    def __init__(self):
        self.vehicle = self.get_vehicle()
        self.initialize = False

    def get_vehicle(self):
        print "connecting to vehicle.."
        return connect('/dev/ttyUSB0', baud=57600)

    def initialize_vehicle(self):
        if self.vehicle is None:
            self.vehicle = self.get_vehicle()
            return True;

    def run(self):
        while True:
            if self.initialize is False:
                self.initialize = self.initialize_vehicle()
                print "Autopilot Firmware version: %s" % self.vehicle.version
                print "Is Armable?: %s" % self.vehicle.is_armable
                print "System status: %s" % self.vehicle.system_status.state
                print "Mode: %s" % self.vehicle.mode.name  # settable
                print "Armed: %s" % self.vehicle.armed  # settable
            time.sleep(0.05)

uas = UAS()
uas.run()




