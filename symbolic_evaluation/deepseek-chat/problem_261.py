import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user can modify this value as needed)
a = mp.mpf(1.0)

# Calculate the sine of a
sin_a = mp.sin(a)

# Calculate the square of a
a_squared = a**2

# Compute the result: sin(a) / a^2
result = sin_a / a_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))