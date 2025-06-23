import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the fourth power
pi_power4 = pi_val**4

# Divide by 1024 to get the final result
result = pi_power4 / 1024

print(mp.nstr(result, n=10))