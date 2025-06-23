import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Compute pi squared
pi_squared = mp.pi ** 2

# Square pi squared to get pi to the fourth power
pi_fourth = pi_squared ** 2

# Divide by 64 to get the final result
result = pi_fourth / 64

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))