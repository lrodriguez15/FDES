#Config file of the UAS

from os.path import expanduser
import ConfigParser

class UASConfig(object):

    def __init__(self):
        # Define Configuration file
        self.config_file = expanduser("~/uas_finder.cnf")
        # create a global object "parser"
        self.parser = ConfigParser.SafeConfigParser()
        # Read the file into memory
        self.read()

    # read - reads the contents of the file into the dictionary in RAM
    def read(self):
        try:
            self.parser.read(self.config_file)
        except IOError as e:
            print 'Error {0} reading config file: {1}: '.format(e.errno, e.strerror)
        return

    def save(self):
        try:
            with open(self.config_file, 'wb') as configfile:
                self.parser.write(configfile)
                except IOError as e:
                print 'Error {0} writing config file: {1}: '.format(e.errno, e.strerror)
                return

    def get_integer(self, section, option, default):
        try:
            return self.parser.getint(section, option)
        except ConfigParser.Error:
            return default

    def get_string(self, section, option, default):
            try:
                return self.parser.get(section, option)
            except ConfigParser.Error:
                return default
