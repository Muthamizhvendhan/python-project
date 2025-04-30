manage.py


#!/usr/bin/python3

#Deploy and manage Redis Database Server using python script [To check if it is working]

#print('First Use case driven Python Script.')

# Import custom module
import os
import sys
import subprocess

#print(os.getcwd())

#access control checking

#Only allow sudoer or not root user to execute this script.
if os.getuid()==0:
  print('Allow execution of the Script.')
else:
  print('Your are not the root user or Sudoer')
  sys.exit(1)
  print('Code still executed')

# Defining Global Variables
packages = ['redis-server','redis-tools']

# Defining functions.

# Install Reddis databases server and tools.
def install_redis():
  print('Installing Redis Database server & tools...')
  for package in packages:
    print('Installing '+package+'...')
    exit_code = subprocess.call(["apt","install","-y",package])
    if exit_code==0:
      print('Installing '+package+' done.')
    else:
      print('Installing '+package+' failed')
# Stop Redis Databases server
def stop_redis():
  print('Stopping Redis database server...')
  exit_code = subprocess.call(["systemctl","stop","redis.service"])
  if exit_code==0:
      print('Stopping Redis Database server'+package+' done.')
  else:
      print('Stopping Redis Database server'+package+' failed')

# Start Redis database server
def start_redis():
  print('Starting Redis databaseserver...')
  exit_code = subprocess.call(["systemctl","start","redis.service"])
  if exit_code==0:
      print('Starting Redis database server'+package+' done.')
  else:
      print('Starting Redis database server'+package+' failed')


# Calling functions and handling CLI arguments.
if sys.argv[1]=='install':
  install_redis()
elif sys.argv[1]=='stop':
  stop_redis()
elif sys.argv[1]=='start':
  start_redis()
else :
  print('Script usage: sudo ./manage-redis.py [install | stop | start]')