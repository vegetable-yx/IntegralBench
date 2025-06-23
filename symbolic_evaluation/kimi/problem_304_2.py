import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first term: -(π * sqrt(3))/12
pi_times_sqrt3 = mp.pi * mp.sqrt(3)
term1 = -pi_times_sqrt3 / 12

# Calculate the second term: 11/18
term2 = mp.mpf(11) / 18

# Combine both terms for final result
result = term1 + term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))