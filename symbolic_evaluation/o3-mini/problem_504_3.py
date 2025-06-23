import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of x at which to evaluate the expression
x_val = 0.1

# Calculate sin(100 * x)
sin_100x = mp.sin(100 * x_val)

# Calculate sin(x)
sin_x = mp.sin(x_val)

# Raise sin(x) to the 100th power
sin_x_100 = sin_x ** 100

# Multiply sin(100x) by sin^100(x)
numerator = sin_100x * sin_x_100

# Divide by 100 to get the expression value (constant C is set to zero for evaluation)
result = numerator / 100

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))