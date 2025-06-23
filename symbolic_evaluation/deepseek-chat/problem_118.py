import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square of pi
pi_squared = mp.power(mp.pi, 2)

# Divide the result by 4
result = pi_squared / 4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))