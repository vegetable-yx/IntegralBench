import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared using mpmath's constant
pi_value = mp.pi
result = pi_value ** 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))