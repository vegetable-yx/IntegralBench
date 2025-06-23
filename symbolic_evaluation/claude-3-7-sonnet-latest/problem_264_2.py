import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi/4
term1 = mp.pi / 4

# Calculate sin(2)
sin_val = mp.sin(2)

# Calculate sin(2)/4
term2 = sin_val / 4

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))