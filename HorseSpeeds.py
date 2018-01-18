import numpy as np

np.set_printoptions(precision=2) # set numpy decimal digits to 2

horseWalk = np.array(4.) # mph four-beat walk
horseJog = np.array([8.1, 12]) # mph two-beat gait
horseCanter = np.array([12., 15.]) # mph three-beat gait
horseGallop = np.array([25., 30.]) # mph

humanWalk = np.array([3.1, 5.6]) # mph

measurementSystem = raw_input("Is the distance in miles or kilometres? ") # miles kilometres
distance = float(input("What distance are you travelling?   "))

# Check if
if measurementSystem == "kilometres" or measurementSystem == "kilometers" or measurementSystem == "km":
    distance = distance/1.609344

print "\nHuman walk"

humanWalkInHours = distance/humanWalk
humanWalkInMinutes = humanWalkInHours*60

print np.where(humanWalkInHours < 1, 'Mins', 'Hours')
print np.where(humanWalkInHours < 1, humanWalkInMinutes, humanWalkInHours)

print "\nHorse four-beat walk"
print distance/horseWalk
print "\nHorse two-beat gait jog"
print distance/horseJog
print "\nHorse three-beat gait canter or lope"
print distance/horseCanter
print "\nHorse gallop"
print distance/ horseGallop
