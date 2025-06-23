import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the value of π
pi_val = mp.pi

# Compute π divided by 2
half_pi = pi_val / 2

# Apply negative sign to get -π/2
result = -half_pi

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))