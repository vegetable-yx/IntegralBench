import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the analytical expression components
# Result = \frac{\pi}{8} \zeta(3) - \frac{\pi}{16} \log^3(2) + \frac{\pi^3}{24} \log(2)

# Compute each term separately
term1 = (mp.pi / 8) * mp.zeta(3)
term2 = (mp.pi / 16) * (mp.log(2) ** 3
term3 = (mp.pi ** 3 / 24) * mp.log(2)

# Combine the terms: term1 - term2 + term3
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))