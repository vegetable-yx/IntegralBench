import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate 2 times Euler's number
two_e = 2 * mp.e

# Compute final result by dividing sqrt(pi) by (2e)
result = sqrt_pi / two_e

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))