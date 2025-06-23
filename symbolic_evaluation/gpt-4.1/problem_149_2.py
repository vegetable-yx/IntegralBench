import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the hypergeometric part: {}_3F_2(1/2, 1/2, 1/4; 1, 1; 1)
hyper_part = mp.hyp3f2(mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf('0.25'), 1, 1, 1)

# Compute pi squared
pi_sq = mp.pi ** 2

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply pi squared by sqrt(2)
numerator = pi_sq * sqrt2

# Divide by 8
factor = numerator / 8

# Multiply by the hypergeometric result
result = factor * hyper_part

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))