import os
import subprocess
import sys
import time


class Test(object):
    """Run unit tests in the tests directory"""

    def __init__(self, command):
        print command
        filename = os.path.basename(__file__)
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/tests/'
        """Gather command and execute the proper test function"""
        if command is None:
            print "Error: no test name given"
            return None
        elif command == "all":
            self.all()
        elif command == "create":
            print sys.argv
            try:
                self.create(sys.argv[2])
            except IndexError:
                print "Error: no new test name given"
                return None
        else:
            try:
                self.single(sys.argv[2])
            except IndexError:
                print "Error: no test name gidsfven"
                return None
            except:
                print "Error: an unknown error has occured during test"

    def all(self):
        """Iterate through all tests in the tests directory"""
        tests = os.listdir(self.path)
        for i in tests:
            subprocess.call(['python', self.path + i])

    def create(self, name):
        """Create a new unittest file in the tests directory"""
        file_bin = os.path.dirname(os.path.realpath(__file__)) + '/bin/templates/'
        print file_bin
        with open(file_bin + 'test.py') as f:
            template = f.read().replace('<_name_>', name)
        if template == "":
            print "File does not exist"
            return None
        timestamp = int(time.time())
        with open(self.path + str(timestamp) + "_" + name + '.py', 'w') as w:
            w.write(template)

    def single(self, name):
        # make sure .py is added to the file
        test_file = self.path + name.strip('.py') + '.py'
        print test_file
        subprocess.call(['python', test_file])


class Spark(object):
    """Run commands to aid in development"""

    def __init__(self, command):
        """Initialize options and execute command"""
        options = {
            'test': Test
        }

        comm = command.split(':')
        print comm
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
