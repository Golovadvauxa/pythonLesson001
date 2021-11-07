import platform
import sys

info = "OS Info is \n{}\n\nPython version is {} {}".format(platform.uname(), sys.version, platform.architecture())
print(info)

with open("Solutions/1/os_info.txt", 'w') as ff:
    ff.write(info)
