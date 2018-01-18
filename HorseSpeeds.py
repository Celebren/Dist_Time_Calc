import numpy as np

np.set_printoptions(precision=2)  # set numpy decimal digits to 2

human_walk = np.array([3.1, 5.6])    # mph

horse_walk = np.array(4.)            # mph four-beat walk
horse_jog = np.array([8.1, 12])      # mph two-beat gait
horse_canter = np.array([12., 15.])  # mph three-beat gait
horse_gallop = np.array([25., 30.])  # mph

measurement_system = raw_input("Is the distance in miles or kilometres? ")  # miles/kilometres
usr_distance = float(input("What distance are you travelling?       "))

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
    str_array = np.where(time_in_hours < 1, 'Mins', 'Hours')
    floats_array = np.where(time_in_hours < 1, time_in_minutes, time_in_hours)

    str2strings_array = np.array2string(str_array)
    floats2strings_array = np.array2string(floats_array)

    combined_array =  np.core.defchararray.add(floats2strings_array, str2strings_array)

    print combined_array
    print combined_array.shape



print "\nHuman walk (at 3.1mph and 5.6mph)"
time_results(usr_distance, human_walk)
print "\nHorse four-beat walk (4mph)"
time_results(usr_distance, horse_walk)
print "\nHorse two-beat gait jog(8.1mph and 12mph)"
time_results(usr_distance, horse_jog)
print "\nHorse three-beat gait canter or lope (12mph and 15mph)"
time_results(usr_distance, horse_canter)
print "\nHorse gallop (25mph and 30mph)"
time_results(usr_distance, horse_gallop)
