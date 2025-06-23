import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^2 using the exponential function
e_squared = mp.exp(2)

# Subtract 1 from e^2
numerator = e_squared - 1

# Divide the result by 4
result = numerator / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))