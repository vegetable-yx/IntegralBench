import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate the constant fraction 2/3
two_thirds = mp.mpf(2) / 3

# Combine logarithmic terms and constant: 2/3 + ln(3) - 2*ln(2)
inner_expr = two_thirds + ln3 - 2 * ln2

# Multiply by π to get final result
result = mp.pi * inner_expr

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))