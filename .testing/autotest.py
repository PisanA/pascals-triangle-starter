#!/usr/bin/env python3

import os
import sys

if not sys.version_info >= (3, 5):
    print("%s needs python 3.5 or later" % __file__)
    sys.exit(-1)

def checkFileAndExit(fname):
    if not os.path.exists(fname):
        print(fname + " does not exist, exiting")
        sys.exit(1)

def checkFileAndRemove(fname):
    if os.path.exists(fname):
        os.remove(fname)

def execCmd(cmd, quiet = False):
    if not quiet:
        print("Executing: " + cmd)
    return os.system(cmd)

def tryIO(num):
    checkFileAndRemove("result.txt")
    print("Running Test, Input: " + str(num), flush = True)
    cmd = "java Solution " + str(num) + " > result.txt"
    expected_file = "./.testing/out-" + str(num) + ".txt"
    execCmd(cmd, True)
    diff_cmd = "diff result.txt " + expected_file
    diff_result = execCmd(diff_cmd, True)
    if diff_result == 0:
        print("Passed Test, Input: " + str(num))
    else:
        print("Expected:", flush = True)
        execCmd("cat " + expected_file, True)
        print("Got:", flush = True)
        execCmd("cat result.txt", True)
        print("Failed Test, Input: " + str(num))

def run_tests():
    checkFileAndExit("Solution.java")
    checkFileAndRemove("Solution.class")
    cmd = "javac Solution.java"
    execCmd(cmd)
    checkFileAndExit("Solution.class")
    for i in (1, 2, 3, 10):
        tryIO(i)

if __name__ == "__main__":
    run_tests()


