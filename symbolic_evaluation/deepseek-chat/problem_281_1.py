import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 4π
# Compute π value
pi_val = mp.pi

# Multiply by 4
result = 4 * pi_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))