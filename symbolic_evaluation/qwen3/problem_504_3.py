import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the input value x (assuming x=0 for demonstration)
x = mp.mpf(0)

# Calculate sin(100x)
sin_100x = mp.sin(100 * x)

# Calculate sin(x) and raise it to the 100th power
sin_x_pow100 = mp.sin(x) ** 100

# Multiply the components and divide by 100
result = (sin_100x * sin_x_pow100) / 100

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))