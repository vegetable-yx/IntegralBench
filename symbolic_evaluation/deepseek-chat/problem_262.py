import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the input value for 'a' (example value, can be changed as needed)
a_val = 1.0

# Compute sin(a) using mpmath
sin_a = mp.sin(a_val)

# Compute a squared
a_squared = a_val**2

# Compute the final result: sin(a) / a^2
result = sin_a / a_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))