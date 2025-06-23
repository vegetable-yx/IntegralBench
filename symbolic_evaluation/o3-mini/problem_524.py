import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e squared (e^2)
e_squared = mp.exp(2)

# Add 1 to e_squared
numerator = e_squared + 1

# Divide the result by 4
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))