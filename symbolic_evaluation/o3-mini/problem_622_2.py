import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Calculate the constant 1/2
one_half = mp.mpf(1) / 2

# Combine the terms: π/4 - 1/2
result = pi_over_4 - one_half

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))