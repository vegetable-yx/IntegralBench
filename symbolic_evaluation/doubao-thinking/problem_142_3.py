import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the hyperbolic sine integral of 2
sh_i = mp.shi(2)

# Multiply by 1/2 to get the final result
result = 0.5 * sh_i

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))