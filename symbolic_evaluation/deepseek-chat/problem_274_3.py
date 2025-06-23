import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 625
denominator = 2

# Convert integers to mpmath floating-point numbers
num_mp = mp.mpf(numerator)
den_mp = mp.mpf(denominator)

# Perform exact division
result = num_mp / den_mp

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))