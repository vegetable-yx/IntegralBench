import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Euler-Mascheroni constant with negative sign
gamma_term = -mp.euler

# Calculate natural logarithm of 2 with negative sign
ln2_term = -mp.log(2)

# Combine terms to get final result
result = gamma_term + ln2_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))