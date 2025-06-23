import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Divide pi^4 by 120
result = pi_fourth / 120

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))