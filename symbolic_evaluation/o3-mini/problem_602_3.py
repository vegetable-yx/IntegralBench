import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi to the fourth power
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Divide by 120 to get the result
result = pi_fourth / 120

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))