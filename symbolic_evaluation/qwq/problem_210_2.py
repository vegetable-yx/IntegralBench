import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Raise π to the fourth power
pi_fourth = pi_val**4

# Divide π^4 by 15 to get the result
result = pi_fourth / 15

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))