import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2 using mpmath precision
sqrt_2 = mp.sqrt(2)

# Multiply by pi using mpmath's constant
result = mp.pi * sqrt_2

# Print result with 10 decimal places using mpmath number string formatting
print(mp.nstr(result, n=10))