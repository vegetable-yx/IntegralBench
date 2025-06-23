import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 18 to obtain the final result
result = pi_squared / 18

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))