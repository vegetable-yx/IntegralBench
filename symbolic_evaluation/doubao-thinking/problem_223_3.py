import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = mp.power(pi_val, 2)

# Divide the squared result by 2
result = mp.fdiv(pi_squared, 2)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))