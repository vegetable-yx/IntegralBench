import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the variable x (example value, adjust as needed)
x = mp.pi / 4
# Define the integration constant C (example value, adjust as needed)
C = 0

# Calculate sin(x) and raise it to the 100th power
sin_x = mp.sin(x)
sin_power = sin_x ** 100

# Calculate sin(100x)
sin_100x = mp.sin(100 * x)

# Multiply the components and divide by 100
term = sin_power * sin_100x
result = term / 100 + C

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))