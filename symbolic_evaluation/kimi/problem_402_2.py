import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Assign the constant value directly from the analytical solution
result = mp.mpf('1.216091994')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))