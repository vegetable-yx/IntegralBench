import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of x (arbitrary choice for evaluation)
x_val = mp.mpf(1.0)  # Using x = 1.0 radian for evaluation

# Compute sin(x)
sin_x = mp.sin(x_val)

# Raise sin(x) to the 100th power
sin_x_100 = sin_x ** 100

# Compute sin(100*x)
sin_100x = mp.sin(100 * x_val)

# Multiply the two components
numerator = sin_x_100 * sin_100x

# Divide by 100 to get the result (ignoring the constant C)
result = numerator / 100

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))