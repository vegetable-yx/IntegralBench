import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi**2

# Compute pi to the fourth power (pi^4 = (pi^2)^2)
pi_fourth = pi_sq**2

# Divide by 192 to get the result
result = pi_fourth / 192

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))