import numpy as np

human_walk = np.array([3.1, 5.6])    # mph

horse_walk = np.array([4.])          # mph four-beat walk
horse_jog = np.array([8.1, 12])      # mph two-beat gait
horse_canter = np.array([12., 15.])  # mph three-beat gait
horse_gallop = np.array([25., 30.])  # mph

while True:
    measurement_system = raw_input("Is the distance in miles or kilometres? ")  # miles/kilometres
    if measurement_system == "miles" \
            or measurement_system == "km" \
            or measurement_system == "kilometres" \
            or measurement_system == "kilometers":
        break
    else:
        print "Incorrect input. Please try again"
        continue

while True:
    try:
        usr_distance = float(input("What distance are you travelling?       "))
        if usr_distance <= 0:
            print "Please enter a value that is greater than zero"
            continue
    except NameError:
        print "Incorrect input. Please enter a distance value (integer or float)"
    else:
        break

# Check if distance is give in kilometres and convert it to miles
if measurement_system == "kilometres" or measurement_system == "kilometers" or measurement_system == "km":
    usr_distance = usr_distance/1.609344


def time_results(distance, speeds):
    """
    Method for calculating and printing our results.
    Of the time result is less than an hour it displays the result in minutes
    """
    time_in_hours = distance/speeds
    time_in_minutes = time_in_hours*60
    str_array = np.where(time_in_hours < 1, ' minutes', ' hours')
    floats_array = np.where(time_in_hours < 1, time_in_minutes, time_in_hours)

    floats_as_strings_array = floats_array.astype(str)

    # slice long floats
    if floats_as_strings_array.shape == (2,):
        first_string, second_string = floats_as_strings_array[0], floats_as_strings_array[1]
        print first_string[:4] + str_array[0] + " to " + second_string[:4] + str_array[1]

    else:  # horse_walk.shape is (1,)
        first_string = floats_as_strings_array[0]
        print first_string[:4] + str_array[0]


print "\nHuman walk (at 3.1mph to 5.6mph)"
time_results(usr_distance, human_walk)
print "\nHorse four-beat to (4mph)"
time_results(usr_distance, horse_walk)
print "\nHorse two-beat gait jog (8.1mph to 12mph)"
time_results(usr_distance, horse_jog)
print "\nHorse three-beat gait canter or lope (12mph to 15mph)"
time_results(usr_distance, horse_canter)
print "\nHorse gallop (25mph to 30mph)"
time_results(usr_distance, horse_gallop)
