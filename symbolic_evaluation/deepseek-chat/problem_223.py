import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi squared
pi_squared = mp.pi ** 2

# Subtract 4 from pi squared
result = pi_squared - 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))