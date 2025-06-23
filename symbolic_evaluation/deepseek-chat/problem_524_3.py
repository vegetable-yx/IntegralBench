import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute e^2 using exponential function
e_squared = mp.exp(2)

# Add 1 to e^2
numerator = e_squared + 1

# Divide by 4 to get the result
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))