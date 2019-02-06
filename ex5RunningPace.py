# ex5RunningPace CSC 121

##############################################################################
#
# Create a program that accepts input for minutes, second, miles
# and then prints output for your pace (min:sec per mile)
#
#############################################################################

minutes = float(input('How many minutes did you run: '))
sec = float(input('How many seconds did you run: '))
miles = float(input('How far (miles) did you run: '))

total_time = minutes + (sec / 60)
min_per_mile = total_time / miles

# conversion of decimal to seconds
seconds = str(min_per_mile - int(min_per_mile))[1:]
final_seconds = float(seconds) * 60

print(f'You ran a pace of {int(min_per_mile)}:{round(final_seconds)} for {miles} miles.')
