import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant e squared (e^2)
e_squared = mp.e ** 2

# Add 1 to form the numerator
numerator = e_squared + 1

# Divide by 4 to obtain the result
result = numerator / 4

# Print the result to exactly 10 decimal places using n=10 (significant digits)
print(mp.nstr(result, n=10))