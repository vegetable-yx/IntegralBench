import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Square the value of π
pi_squared = mp.power(pi_val, 2)

# Divide by 2 to get final result
result = pi_squared / 2

# Output the result with 10 decimal places
print(mp.nstr(result, n=10))