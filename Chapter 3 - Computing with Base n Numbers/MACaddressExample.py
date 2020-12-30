# Python Program to find
# MAC address of your computer by using UUID module

import uuid

# address using uuid and getnode() function
# making use of hexadecimal number system
print (hex(uuid.getnode()))
