import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 32 to get the final result
result = pi_squared / 32

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))