import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Multiply by 2 to get the argument for sine
arg_val = 2 * sqrt_val

# Compute the sine of the argument
sin_val = mp.sin(arg_val)

# Multiply the result by 2
result = 2 * sin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))