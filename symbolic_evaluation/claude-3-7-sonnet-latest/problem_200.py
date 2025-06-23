import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the cosine of 1 radian
cos_val = mp.cos(1)

# Subtract the cosine value from 1
one_minus_cos = 1 - cos_val

# Multiply the result by 2
result = 2 * one_minus_cos

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))