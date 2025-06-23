import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the square root of 15
sqrt_15 = mp.sqrt(15)

# Multiply by pi
pi_times_sqrt15 = mp.pi * sqrt_15

# Divide by 6
term = pi_times_sqrt15 / 6

# Compute the final result: - (π√15)/6 + 2
result = -term + 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))