import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of x (here we choose x = 1 radian for evaluation)
x = mp.mpf(1)

# Compute sin(x)
sin_x = mp.sin(x)

# Compute sin(100*x)
sin_100x = mp.sin(100 * x)

# Compute sin(x) raised to the 100th power
sin_x_power100 = sin_x ** 100

# Multiply the power by sin(100x)
product = sin_x_power100 * sin_100x

# Divide by 100 to get the result
result = product / 100

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))