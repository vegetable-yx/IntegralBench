import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Assign the exact value of pi using mpmath's constant
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))