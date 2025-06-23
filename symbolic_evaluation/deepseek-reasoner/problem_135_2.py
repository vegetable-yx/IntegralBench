import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 3/4 of pi using mpmath's constant
pi_value = mp.pi
three_pi = 3 * pi_value
result = three_pi / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))