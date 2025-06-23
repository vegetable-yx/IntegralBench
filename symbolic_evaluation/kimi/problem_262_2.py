import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate 1 - 1/e term
e_reciprocal = 1 / mp.e
one_minus_e_reciprocal = 1 - e_reciprocal

# Calculate pi/2 term
pi_half = mp.pi / 2

# Multiply components to get final result
result = pi_half * one_minus_e_reciprocal

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))