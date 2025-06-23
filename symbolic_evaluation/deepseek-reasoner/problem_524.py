import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate e squared
e_squared = mp.exp(2)

# Calculate numerator (e^2 + 1)
numerator = e_squared + 1

# Divide by 4 to get final result
result = numerator / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))