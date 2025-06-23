import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each term of the expression separately
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2
term1 = pi_fourth / 144

ln2 = mp.log(2)
ln2_squared = ln2 ** 2
term2 = (pi_squared * ln2_squared) / 24

ln2_fourth = ln2 ** 4
term3 = ln2_fourth / 12

zeta3 = mp.zeta(3)
term4 = (zeta3 * ln2) / 2

# Combine all terms to get the final result
result = term1 - term2 + term3 - term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))