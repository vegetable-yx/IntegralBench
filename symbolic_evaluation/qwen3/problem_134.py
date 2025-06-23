import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2 using mpmath's sqrt function
sqrt_2 = mp.sqrt(2)

# Multiply by pi using mpmath's constant
result = mp.pi * sqrt_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))