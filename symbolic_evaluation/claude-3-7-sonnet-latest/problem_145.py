import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user should adjust this as needed)
a_val = mp.mpf(1.0)  # Example value, can be changed

# Compute cosine of a_val
cos_a = mp.cos(a_val)

# Compute (1 - cos(a_val))
one_minus_cos = 1 - cos_a

# Multiply by 2
numerator = 2 * one_minus_cos

# Divide by a_val to get final result
result = numerator / a_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))