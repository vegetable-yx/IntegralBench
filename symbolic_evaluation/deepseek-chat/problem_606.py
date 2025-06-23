import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^2
pi_squared = mp.pi ** 2

# Divide by 4 to get the result
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))