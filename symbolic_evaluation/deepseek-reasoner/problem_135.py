import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 3/4 of pi using exact symbolic relationship
pi_value = mp.pi
three_quarters_pi = (3 * pi_value) / 4

# Store final result
result = three_quarters_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))