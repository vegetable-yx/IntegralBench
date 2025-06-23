import mpmath as mp

# Set decimal places for internal calculations to 15
mp.dps = 15

# Calculate pi/6
pi_over_6 = mp.pi / 6

# Calculate sqrt(3)
sqrt_3 = mp.sqrt(3)

# Calculate sqrt(3)/8
sqrt_3_over_8 = sqrt_3 / 8

# Sum the two terms
result = pi_over_6 + sqrt_3_over_8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))