import mpmath as mp
mp.dps = 15

# Calculate pi^4 by first squaring pi and then squaring the result
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Divide the result by 16 to get the final value
result = pi_fourth / 16

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))