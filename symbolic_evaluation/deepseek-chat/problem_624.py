import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Square pi to get numerator
pi_squared = pi_val ** 2

# Define denominator
denominator = 9

# Compute the final result: π²/9
result = pi_squared / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))