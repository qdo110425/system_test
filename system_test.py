# Name: Quyen Do
# OSU email: doq@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:
# Due Date: *
# Description: *

import sys
cur_version = sys.version_info
if cur_version >= (3, 10):
    print("This is an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is too low, it needs to be 3.10 or greater and this is " + str(cur_version[0]) + '.' +
          str(cur_version[1]) + '.')
