import time
from array import *

# list of time limits in milliseconds
time_limits = array('i', [500, 2000, 4000, 8000, 16000, 32000, 64000])

# save the counts from each time limit
final_counts = array('i', [])

# get time now in milliseconds
def now():
    return int(round(time.time()*1000))

# return the answer to this BIG math problem
def do_math():
	return 9832128.2/382 + (3002*28*3) - 4.2 + (308*5) - 302.2802

# print the answer to the math problem
print do_math()

# save the final counts in a new arra#
# count how many times it does the math problem in the time limit
def math_count(time_limit):
	# the amount of times its done the math problem
	count = 0

	# start the timer
	start = now()

	# setting the time limit
	stop = start + time_limit

	print "the time limit is"
	print time_limit

	# while the present is less than the time limit,do the math problem
	# and count it 
	while(now() < stop):
		do_math()
		count = count+1
	return count

# loop the time limits array
# get final count from each time limit
for limit in time_limits:
	final_counts.append(math_count(limit))

# print all the counts from each time limit
# find the average
sum_value = 0
sum_number = 126500
for count in final_counts:
	sum_value = sum_value + count
	print count

# mean average = (sum of counts)/(sum of time limits)
average_count = sum_value / sum_number

print "The average number of completions per second"
print average_count * 1000

