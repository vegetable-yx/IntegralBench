import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute e squared (e is the base of natural logarithm)
e_squared = mp.power(mp.e, 2)

# Subtract 1 from e squared
numerator = e_squared - 1

# Divide the result by 4
result = numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))