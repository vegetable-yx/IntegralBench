import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The integral of sin(sin(x) - x) from 0 to 2π is analytically zero due to symmetry
result = mp.mpf(0)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))