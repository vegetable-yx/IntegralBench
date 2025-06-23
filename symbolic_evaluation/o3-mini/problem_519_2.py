import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4: a fundamental mathematical constant expression
pi_value = mp.pi
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))