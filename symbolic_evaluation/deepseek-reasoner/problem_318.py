import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator
numerator = 2

# Get the value of pi from mpmath
pi_value = mp.pi

# Compute the result of 2/pi
result = numerator / pi_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))