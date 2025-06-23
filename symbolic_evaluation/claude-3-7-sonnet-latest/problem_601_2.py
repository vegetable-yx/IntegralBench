import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_val = mp.pi

# Compute π squared
pi_squared = pi_val ** 2

# Calculate the first term: π²/8
term1 = pi_squared / 8

# Calculate arctan(1/4) using mp.atan
atan_val = mp.atan(1/4)

# Calculate the second term: (π/2) * arctan(1/4)
term2 = (pi_val / 2) * atan_val

# Compute the final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))