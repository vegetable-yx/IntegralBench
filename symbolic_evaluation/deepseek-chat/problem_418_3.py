import mpmath as mp

# Set internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 6 to get the zeta(2) value (Basel problem solution)
zeta2 = pi_squared / 6

# Subtract 1 to get the final result
result = zeta2 - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))