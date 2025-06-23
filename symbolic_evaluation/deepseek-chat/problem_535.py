import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^3
e_cubed = mp.exp(3)

# Divide the result by 3
result = e_cubed / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))