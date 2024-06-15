# import os
# os.popen('ls')
# os.popen('whoami')
# os.popen('ifconfig')

# import os
# ls_return = os.popen('ls')
# print('The contents of ls_return:',ls_return)
# whoami_return = os.popen('whoami')
# print('The contents of whoami_return:',whoami_return)
# ifconfig_return = os.popen('ifconfig')
# print('The contents of ifconfig_return:',ifconfig_return)

# import os
# whoami_return=os.popen('whoami')
# whoami_contents = whoami_return.read()
# print('whoami_contents:',whoami_contents)


# ipconfig_return = os.popen('ipconfig')
# ipconfig_contents = ipconfig_return.read()
# print('The contents of ipconfig_return:',ipconfig_contents)

# import subprocess

# p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# output = p.communicate()
# print(output)
# print(output[0])
# # The above stdout is stored in bytes
# # Convert stdout to a string and strip off the newline characters
# stdout = output[0].decode('utf-8').strip()
# print(stdout)

import os
ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

import os
whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)

ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:',ipconfig_contents)