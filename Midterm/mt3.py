# Define a function that computes batting average (hits / at bats).
# It should have 2 parameters (ab,h). Have the function return a value.
# Then call the function with the arguments (449, 175).
# Display the batting average with 3 decimal places ex/.326


def batting_ave(ab, h):
    average = h / ab
    return average


print(round(batting_ave(449, 175), 3))
