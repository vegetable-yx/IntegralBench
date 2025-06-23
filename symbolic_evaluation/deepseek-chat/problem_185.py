import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.power(mp.pi, 2)

# Compute term1: pi^2 / 16
term1 = pi_squared / 16

# Compute sqrt(8)
sqrt_8 = mp.sqrt(8)

# Compute the argument for arctan: 1 / sqrt(8)
atan_arg = 1 / sqrt_8

# Compute arctan(1/sqrt(8))
atan_val = mp.atan(atan_arg)

# Compute term2: (3 * pi * arctan(1/sqrt(8))) / 8
term2 = (3 * mp.pi * atan_val) / 8

# Compute the final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))