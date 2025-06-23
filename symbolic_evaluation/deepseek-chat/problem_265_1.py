import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sin(2)
sin_val = mp.sin(2)

# Divide by 4
div_result = sin_val / 4

# Apply negative sign
result = -div_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))