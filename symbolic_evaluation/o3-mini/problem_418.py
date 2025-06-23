import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 6 to get the first term (zeta(2) = pi^2/6)
zeta_2 = pi_squared / 6

# Subtract 1 to get the final result
result = zeta_2 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))