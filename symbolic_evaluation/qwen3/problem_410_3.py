import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate 2 times Euler's number
two_e = 2 * mp.e

# Compute the final result by dividing sqrt(pi) by (2e)
result = sqrt_pi / two_e

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))