import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant value from the analytical solution
result = mp.mpf(1005)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))