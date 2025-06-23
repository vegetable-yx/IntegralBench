import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^3 using exponential function
e_cubed = mp.exp(3)

# Divide the result by 3 to get final value
result = e_cubed / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))