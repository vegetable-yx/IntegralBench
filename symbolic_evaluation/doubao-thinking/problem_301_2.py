import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each term of the expression separately
ln2 = mp.log(2)  # Natural logarithm of 2

term1 = (5 * mp.pi**2) / 12  # (5π²)/12 term
term2 = 4 * ln2  # 4ln2 term
term3 = 4 * ln2**2  # 4(ln2)² term
term4 = 4  # Constant term

# Combine all terms to get the final result
result = term1 + term2 - term3 - term4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))