import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 6
result = pi_squared / 6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))