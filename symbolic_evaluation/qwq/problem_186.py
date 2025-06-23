import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = mp.power(pi_val, 2)

# Divide the squared π by 32
result = mp.fdiv(pi_squared, 32)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))