import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# User must define the value of 'a' here as a string for exact representation
# Example: to set a=2, replace '1.0' with '2.0'
a_val = mp.mpf('1.0')  # Replace with desired value of a

# Compute the square of a
a_squared = a_val**2

# Calculate the result: π divided by a squared
result = mp.pi / a_squared

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))