import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.power(mp.pi, 3)

# Divide by 12
result = pi_cubed / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))