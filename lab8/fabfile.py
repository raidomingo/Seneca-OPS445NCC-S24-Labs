# This is fabfile is created for an ubuntu vm machine. It will not work with centos.
# Central machine is fedora and remote is ubuntu.
# Author: rdomingo6


from fabric.api import *

# Set the name of the user login to the remote host
env.user = 'rdomingo6'
env.port = '22' # <-- please replace with the actual value of your VM's port number
env.hosts = ['192.168.2.72']
env.password = 'P@ssw0rd'
# Define the task to get the hostname of remote machines:
def getHostname():
    name = run("hostname")
    print("The host name is:",name)

def installPackage(pkg='dummy'):
    cmd = 'apt install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def removePackage(pkg=''):
    if pkg == '':
       cmd = 'apt remove dummy -y'
    else:
       cmd = 'apt remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def updatePackage(pkg=''):
    if pkg == '':
       cmd = 'apt update && apt upgrade -y'
    else:
       cmd = 'apt update && apt upgrade ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def makeUser():
    # Create a new user with a home directory
    cmd = 'useradd -m -d /home/ops445p ops445p'
    status = sudo(cmd)
    print("Creating user:", status)
    
    # Add the new user to the 'wheel' group for sudo access
    cmd = 'usermod -aG sudo ops445p'
    status = sudo(cmd)
    print(status)

    # Set password
    cmd = 'echo "ops445p:P@ssw0rd" | chpasswd'
    status = sudo(cmd)
    print(status)

    # Create SSH directory and setting permission
    cmd = 'mkdir -p /home/ops445p/.ssh'
    status = sudo(cmd)
    print(status)
    cmd = 'touch /home/ops445p/.ssh/authorized_keys'
    status = sudo(cmd)
    print(status)
    cmd = 'chmod 700 /home/ops445p/.ssh'
    status = sudo(cmd)
    print(status)
    cmd = 'chown -R ops445p:ops445p /home/ops445p/.ssh'
    status = sudo(cmd)
    print(status)

    # Add the SSH public key to the authorized_keys file
    put('id_rsa.pub', '/home/ops445p/.ssh/authorized_keys', use_sudo=True)
    cmd = 'chmod 600 /home/ops445p/.ssh/authorized_keys'
    status = sudo(cmd)
    print(status)
    cmd = 'chown ops445p:ops445p /home/ops445p/.ssh/authorized_keys'
    status = sudo(cmd)
    print(status)



def removeUser():
    cmd = 'userdel -r ops445p'
    status =sudo(cmd)
    print(status)