import os
os.system('systemctl status haproxy')

if (os.system('systemctl status haproxy') == 0) :
   print ("\nHAProxy is running !!!")
else:
   print ("\nHAProxy is NOT running !!!")
