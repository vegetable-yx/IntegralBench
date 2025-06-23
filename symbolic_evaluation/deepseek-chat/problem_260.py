import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate cosine of 1 radian
cos_val = mp.cos(1)

# Compute the term (1 - cos(1))
one_minus_cos = 1 - cos_val

# Multiply by pi/2
result = (mp.pi / 2) * one_minus_cos

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))