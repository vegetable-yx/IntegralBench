import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the numerator
numerator = mp.mpf(1)

# Define the denominator
denominator = mp.mpf(5)

# Compute the result: 1/5
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))