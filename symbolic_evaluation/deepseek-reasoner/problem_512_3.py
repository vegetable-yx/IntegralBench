import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e squared using mpmath's exponential function
e_squared = mp.exp(2)

# Compute the difference between e squared and 1
numerator = e_squared - 1

# Divide the result by 4 to get the final value
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))