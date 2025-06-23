import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the value of pi using mpmath constant
pi_value = mp.pi

# Multiply by 3 to get the result
result = 3 * pi_value

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))