#!/usr/bin/env python3

# Import module statements

import shutil
import os

# move to the home user directory
os.chdir('/home/student/mycode/')

# move the file 
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
