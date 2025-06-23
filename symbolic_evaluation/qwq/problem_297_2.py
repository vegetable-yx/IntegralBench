import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi squared
pi_squared = mp.power(pi_val, 2)

# Compute pi to the fourth power by squaring pi_squared
pi_power4 = mp.power(pi_squared, 2)

# Divide pi^4 by 160 to get final result
result = mp.fdiv(pi_power4, 160)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))