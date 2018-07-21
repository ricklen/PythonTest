# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and pocess_time()

# use the documentation for the get_clock_info() function to work out
# how to call it for each of the clocks.

import time

print("Time(): ",time.get_clock_info('time'))
print("Perf_counter: ", time.get_clock_info('perf_counter'))
print("Monotonic: ",time.get_clock_info('monotonic'))
print("Process_time: ",time.get_clock_info('process_time'))