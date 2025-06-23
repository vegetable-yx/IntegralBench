import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4 using mpmath's constant for pi
pi_val = mp.pi
result = pi_val / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))