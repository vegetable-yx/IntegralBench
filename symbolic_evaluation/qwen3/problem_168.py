import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the value of pi
result = pi_value ** 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))