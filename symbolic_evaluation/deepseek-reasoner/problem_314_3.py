import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each term in the expression separately
zeta3 = mp.zeta(3)  # Riemann zeta function at 3
term1 = (-13/16) * zeta3

ln2 = mp.log(2)  # Natural logarithm of 2
term2 = (mp.pi**2 * ln2) / 12

term3 = (ln2**3) / 6

# Combine all terms to get the final result
result = term1 + term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))