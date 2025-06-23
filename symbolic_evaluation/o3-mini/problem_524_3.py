import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute e^2 using the constant e
e_squared = mp.e ** 2

# Calculate the numerator: e^2 + 1
numerator = e_squared + 1

# Divide by 4 to get the result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))