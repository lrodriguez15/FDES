from dronekit import connect, VehicleMode #, LocationGlobal, GPSInfo, Vehicle, MAVConnection
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

    def arm_vehicle(self):
        print "Basic pre-arm checks"
        # Don't try to arm until autopilot is ready
        while not self.vehicle.is_armable:
            print " Waiting for vehicle to initialise..."
            time.sleep(1)

        print "Arming motors"
        # Copter should arm in GUIDED mode
        self.vehicle.mode = VehicleMode("AUTO")
        self.vehicle.armed = True

        # Confirm vehicle armed before attempting to take off
        while not self.vehicle.armed:
            print " Waiting for arming..."
            time.sleep(1)

    def run(self):
        while True:
            if self.initialize is False:
                self.initialize = self.initialize_vehicle()
                print "Autopilot Firmware version: %s" % self.vehicle.version
                print "Is Armable?: %s" % self.vehicle.is_armable
                print "System status: %s" % self.vehicle.system_status.state
                print "Mode: %s" % self.vehicle.mode.name  # settable
                print "Armed: %s" % self.vehicle.armed  # settable
                self.arm_vehicle()
            time.sleep(1)
            print "Vehicle OK"




uas = UAS()
uas.run()




