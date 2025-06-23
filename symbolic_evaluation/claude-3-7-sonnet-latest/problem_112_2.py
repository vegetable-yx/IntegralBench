import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Multiply by 2
two_pi_cubed = 2 * pi_cubed

# Divide by 3 to get final result
result = two_pi_cubed / 3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))