import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator (π - 2)
numerator = mp.pi - 2

# Divide by 8 to get the final result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))