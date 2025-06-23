import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define the input value for the natural logarithm
number = mp.mpf(3)

# Compute the natural logarithm of 3
result = mp.log(number)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))