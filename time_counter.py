import time

def procedure():
   time.sleep(5)

# measure process time
t0 = time.perf_counter()
procedure()
print ("Timeout: " + str(round(time.perf_counter(),2)) + " seconds ")

