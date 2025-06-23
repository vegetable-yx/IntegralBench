import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate first term: π/9*(sqrt(2) - 1)
sqrt2 = mp.sqrt(2)
term1_part = sqrt2 - 1
term1 = (mp.pi / 9) * term1_part

# Calculate second term: π/24*ln(2)
ln2 = mp.log(2)
term2 = (mp.pi / 24) * ln2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))