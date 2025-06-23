import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerical value of 506 * pi
constant = 506
pi_value = mp.pi
result = constant * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))