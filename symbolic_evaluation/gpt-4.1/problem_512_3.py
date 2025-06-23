import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^2 (square of the base of natural logarithms)
e_squared = mp.exp(2)

# Calculate the numerator: e^2 - 1
numerator = e_squared - 1

# Divide the numerator by 4 to get the result
result = numerator / 4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))