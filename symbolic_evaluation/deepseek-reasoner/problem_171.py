import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = mp.power(pi_val, 2)

# Divide the squared π by 320
result = pi_squared / 320

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))