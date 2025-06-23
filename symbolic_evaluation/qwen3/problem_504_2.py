import mpmath as mp

mp.dps = 15  # Set internal precision

# Define the variable (assuming evaluation at x=0.5)
x = mp.mpf('0.5')

# Calculate sin(100x)
sin_100x = mp.sin(100 * x)

# Calculate sin(x)^100 using mpmath power
sin_x_pow100 = mp.sin(x) ** 100

# Multiply components and divide by 100
result = (sin_100x * sin_x_pow100) / 100

# Print result with 10 decimal places
print(mp.nstr(result, n=10))