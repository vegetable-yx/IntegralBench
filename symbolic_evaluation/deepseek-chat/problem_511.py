import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply the square root by 2 to get the argument for sine
arg = 2 * sqrt2

# Compute the sine of the argument
sin_val = mp.sin(arg)

# Multiply the sine result by 2 to get the final answer
result = 2 * sin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))