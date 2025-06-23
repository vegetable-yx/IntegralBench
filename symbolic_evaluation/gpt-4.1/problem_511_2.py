import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 2 to get the argument for sine
arg = 2 * sqrt_2

# Compute the sine of the argument
sin_val = mp.sin(arg)

# Multiply by 2 for the final result
result = 2 * sin_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))