import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi) using mpmath's constant
pi_val = mp.pi

# Square the value of π
pi_squared = pi_val ** 2

# Divide the squared π by 5
result = pi_squared / 5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))