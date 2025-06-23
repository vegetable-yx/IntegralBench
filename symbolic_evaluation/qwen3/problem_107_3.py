import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the result using the analytical solution π²/8
result = mp.pi**2 / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))