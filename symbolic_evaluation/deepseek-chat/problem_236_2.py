import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the exact value of pi from mpmath constant
pi_value = mp.pi

# Format and print the result to 10 decimal places
print(mp.nstr(pi_value, n=10))