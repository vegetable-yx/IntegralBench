import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 6 to get the Basel problem solution (zeta(2))
basel_result = pi_squared / 6

# Subtract 1 to get the final result
result = basel_result - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))