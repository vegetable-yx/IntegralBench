import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 1/2
# Directly compute the fraction using mpmath
result = mp.mpf(1) / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))