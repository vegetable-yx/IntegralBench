import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi^4
pi_fourth = mp.power(mp.pi, 4)

# Divide by 32 to get the result
result = pi_fourth / 32

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))