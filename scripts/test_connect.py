from dronekit import connect #, VehicleMode, LocationGlobal, GPSInfo, Vehicle, MAVConnection
import time

class UAS(object):
    def __init__(self):
        self.vehicle = self.get_vehicle()


        self.initialize = False

    def get_vehicle(self):
        print "connecting to vehicle.."
        return connect('/dev/ttyUSB0', wait_ready=True, baud=921600)

    def initialize_vehicle(self):
        if self.vehicle is None:
            self.vehicle = self.get_vehicle()
            print "vehicle connected.."
            return True;

    def run(self):
        while True:
            if self.initialize is False:
                self.initialize = self.initialize_vehicle()
            else:
                print "Vehicle OK"

            time.sleep(0.05)

uas = UAS()
uas.run()




