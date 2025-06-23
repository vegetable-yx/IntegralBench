import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared
pi_value = mp.pi  # Get the constant pi
result = pi_value ** 2  # Square pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))