import os
import time

time.sleep(5)

os.remove("config.txt")
os.remove("sql.txt")
os.remove("mfile.txt")
os.remove("event.txt")

os.startfile("setup.py")

exit()
