import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute Catalan's constant using mpmath's built-in constant
G = mp.catalan

# Multiply by 2 to get the final result
result = 2 * G

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))