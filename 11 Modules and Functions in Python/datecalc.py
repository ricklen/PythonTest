import time

# print(time.gmtime(time.time()))

# time_here = time.localtime()

# print(time_here)

# print(type(time_here))

# print("year: ", time_here[0], time_here.tm_year)

# print("month: ", time_here[1], time_here.tm_min)

from time import time as my_timer
import random

input("press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()

print("started at " + time.strftime("%X",time.localtime(start_time)))
print("ended at " + time.strftime("%X",time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))