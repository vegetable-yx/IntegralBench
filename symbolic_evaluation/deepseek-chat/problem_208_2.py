import mpmath as mp

# Set internal decimal precision to 15 for all calculations
mp.dps = 15

# Calculate pi/2: the constant π divided by 2
result = mp.pi / 2

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))