import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi raised to the fourth power
pi4 = mp.pi ** 4

# Divide the result by 16 to get the final value
result = pi4 / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))