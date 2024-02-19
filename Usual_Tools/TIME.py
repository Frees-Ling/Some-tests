import time

def get_time(x):
    if x >= 0:
        localtime = time.asctime( time.localtime(time.time()) )
        print("Localtime :", localtime)
    else:
        pass