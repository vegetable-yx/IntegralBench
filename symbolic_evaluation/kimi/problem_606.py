import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: π/2
# This is the exact value that approximates to 1.5707963268 when rounded to 10 decimals
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))