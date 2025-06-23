import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sin(1)
sin_val = mp.sin(1)

# Compute cos(1)
cos_val = mp.cos(1)

# Combine the sine and cosine results
sum_val = sin_val + cos_val

# Subtract 1 from the sum
inner_expr = sum_val - 1

# Multiply by 2 to get the final result
result = 2 * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))