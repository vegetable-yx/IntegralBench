import mpmath as mp

# Set the internal decimal precision to 15 to ensure 10 decimal places in the result
mp.dps = 15

# Compute π squared: result = π * π
pi_val = mp.pi
result = pi_val ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))