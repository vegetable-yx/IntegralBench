import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π
pi_val = mp.pi

# Compute π squared
pi_squared = pi_val ** 2

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Multiply: 2 * π² * √2
result = 2 * pi_squared * sqrt2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))