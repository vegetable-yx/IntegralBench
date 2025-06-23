import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the (sqrt(5) - 2) term
term = sqrt5 - 2

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))