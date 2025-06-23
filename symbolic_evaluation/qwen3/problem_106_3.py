import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Compute π²/8 term
term_pi_sq_over_8 = pi_squared / 8

# Calculate 2√3 component
sqrt_3 = mp.sqrt(3)
term_2sqrt3 = 2 * sqrt_3

# Combine all components: π²/8 + 4 - 2√3
result = term_pi_sq_over_8 + 4 - term_2sqrt3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))