import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define common constants and expressions
pi = mp.pi
sqrt2 = mp.sqrt(2)

# Calculate the argument for the logarithm
log_arg = (3 + 2 * sqrt2) / 4

# Compute the first term: π(2 - √2) / (2√2)
numerator1 = pi * (2 - sqrt2)
denominator1 = 2 * sqrt2
term1 = numerator1 / denominator1

# Compute the second term: (π/4) * ln((3 + 2√2)/4)
term2 = (pi / 4) * mp.log(log_arg)

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))