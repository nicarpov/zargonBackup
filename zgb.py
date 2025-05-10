#!/usr/bin/env python
import sys
import os
import time

def getArg(indx):
    try:
        return sys.argv[indx]
    except IndexError:
        return None

def create_backup(src_path, backup_dir, **kwargs):
    """Creates backup with rsync utility.\n
    Arguments\n
    link - specifies path to link to"""
    cmd_template = "rsync -aAXv {src_path} {backup_dir}"
    if not os.path.exists(src_path):
        return False
    if not os.path.exists(backup_dir):
        return False
    if 'link' in kwargs and kwargs['link'] and os.path.exists(kwargs['link']):
        cmd_template += " --link-dest={link}"
    

    backup_dir = os.path.join(backup_dir, time.strftime('%Y%m%d_%H%M%S'))
    cmd = cmd_template.format(src_path=src_path, backup_dir=backup_dir, **kwargs)
    yes = input("Backup command is: {} \nAre you ready?".format(cmd))
    if not yes in ['', 'y', 'yes']:
        return

    if os.system('mkdir {}'.format(backup_dir)) != 0:
        print("fail creating directory: {}".format(backup_dir))
	
    if os.system(cmd) == 0:
        print("Backup success!")
    else:
        print("Backup failed")

if __name__ == "__main__":
    src_path = getArg(1)
    backup_dir = getArg(2)
    link = getArg(3)
    
    create_backup(src_path, backup_dir, link=link)

	
