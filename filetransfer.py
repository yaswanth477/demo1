

#installation === python PKGs

# this is the way to Upload File, Similarlly u can Download by using sftp.get(localpath, path) check in Google for that
# pip install sftp
# pip install pysftp
# pip install paramiko

import paramiko
import sys


host = "THEHOST.com"  # Enter Ip or Host Name
port = 22
transport = paramiko.Transport((host, port))

password = "THEPASSWORD"  # hard-coded
username = "THEUSERNAME"  # hard-coded
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)


path = './THETARGETDIRECTORY/' + sys.argv[1]  # hard-coded
localpath = sys.argv[1]
sftp.put(localpath, path)

sftp.close()
transport.close()
print('Upload done.')

# Another Way of doing  using Different pythom Module

import pysftp
import sys

path = './THETARGETDIRECTORY/' + sys.argv[1]    #Path in destination  server
localpath = sys.argv[1]    #Path in source  server

# we are Moving file from Source Place to Destination

host = "THEHOST.com"                    #hard-coded
password = "THEPASSWORD"                #hard-coded
username = "THEUSERNAME"                #hard-coded

with pysftp.Connection(host, username=username, password=password) as sftp:
    sftp.put(localpath, path)

print ('Upload done.')
