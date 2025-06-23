import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Choose a specific x-value for evaluation (arbitrary, but necessary for numerical output)
x_val = mp.mpf('0.5')

# Compute sin(100x)
sin_100x = mp.sin(100 * x_val)

# Compute sin(x)
sin_x = mp.sin(x_val)

# Raise sin(x) to the 100th power
sin_x_100 = sin_x ** 100

# Multiply sin(100x) by sin^100(x)
numerator = sin_100x * sin_x_100

# Divide by 100 to get the main expression (constant C omitted as arbitrary)
result = numerator / 100

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))