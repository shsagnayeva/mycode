#!/usr/bin/env python3

import shutil
import os

def main():
    
    # move into working directory
    os.chdir('/home/student/mycode/')
    
    # move file
    shutil.move('raynor.obj', 'ceph_storage/')

    # input
    xname = input('What is the new name for kerrigan.obj? ')

    # move file with new name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()


