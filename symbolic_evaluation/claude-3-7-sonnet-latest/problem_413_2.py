import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi using mpmath constant
pi_value = mp.pi

# Multiply by 506
result = 506 * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))