import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator and denominator as integers
numerator = -2023
denominator = 2022

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Perform the division to compute the rational number
result = num_mp / den_mp

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))