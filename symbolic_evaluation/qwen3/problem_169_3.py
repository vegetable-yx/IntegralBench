import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π²/3
pi_squared_over_3 = mp.power(mp.pi, 2) / 3

# Calculate 2π√3
two_pi_sqrt3 = 2 * mp.pi * mp.sqrt(3)

# Calculate -4π
minus_4pi = -4 * mp.pi

# Combine all terms
result = pi_squared_over_3 + two_pi_sqrt3 + minus_4pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))