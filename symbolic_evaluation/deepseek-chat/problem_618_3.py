import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Euler-Mascheroni constant
gamma = mp.euler

# Subtract gamma from 1
result = 1 - gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))