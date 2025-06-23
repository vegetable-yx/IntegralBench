import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute (pi^2 - 8)
pi_sq_minus_8 = pi_squared - 8

# Multiply sqrt(2) by (pi^2 - 8)
result = sqrt2 * pi_sq_minus_8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))