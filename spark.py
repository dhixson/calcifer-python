import os
import subprocess
import sys
import time
import re


# Class: Test
# Purpose: Create and Run unit tests
# Created By: Dane Hixson
# Last Updated By: Dane Hixson
# Last Updated: 02/11/2016
class Test(object):
    """Run unit tests in the tests directory"""

    def __init__(self, command):
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/tests/'
        """Gather command and execute the proper test function"""
        if command is None:
            print "Error: no test name given"
            return None
        elif command == "all":
            self.all()
        elif command == "create":
            try:
                self.create(sys.argv[2])
            except IndexError:
                print "Error: no new test name given"
                return None
        else:
            try:
                self.single(sys.argv[2])
            except IndexError:
                print "Error: no test name given"
                return None

    def all(self):
        """Iterate through all tests in the tests directory"""
        tests = os.listdir(self.path)
        for i in tests:
            subprocess.call(['python', self.path + i])

    def create(self, name):
        """Create a new unittest file in the tests directory"""
        file_bin = os.path.dirname(os.path.realpath(__file__)) + '/assets/templates/'
        with open(file_bin + 'test.py') as f:
            template = f.read().replace('<_name_>', name)
        if template == "":
            print "File does not exist"
            return None
        timestamp = int(time.time())
        with open(self.path + str(timestamp) + "_" + name + '.py', 'w') as w:
            w.write(template)
        print "Test %s created" % name

    def single(self, name):
        # make sure .py is added to the file
        tests = {re.sub('[\d]+_', '', x): x for x in os.listdir(self.path)}
        print tests
        test_file = name.strip('.py') + '.py'
        subprocess.call(['python', self.path + tests[test_file]])


# Class: Spark
# Purpose: The main spark driver
# Written By: Dane Hixson
# Last updated By: Dane Hixson
# Last updated: 02/11/2016
class Spark(object):
    """Run commands to aid in development"""

    def __init__(self, command):
        """Initialize options and execute command"""
        options = {
            'test': Test
        }

        comm = command.split(':')
        if len(comm) > 2:
            print "Error: too many arguments provided"
            return None
        elif len(comm) is 0:
            print options
            return None
        elif len(comm) is 1:
            comm.append(None)
        options[comm[0]](comm[1])

if __name__ == '__main__':
    Spark(sys.argv[1])
