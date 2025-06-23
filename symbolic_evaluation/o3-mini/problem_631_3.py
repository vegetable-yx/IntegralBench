import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute sin(1) directly
result = mp.sin(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))