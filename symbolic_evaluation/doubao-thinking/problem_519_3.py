import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate pi/4 using mpmath's constant for pi
pi = mp.pi
result = pi / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))