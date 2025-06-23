import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 2 to get 2*sqrt(2)
two_sqrt2 = 2 * sqrt2

# Multiply by pi to get the final result
result = two_sqrt2 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))