import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Euler-Mascheroni constant (γ)
euler_gamma = mp.euler

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Multiply ln(2) by 2
two_ln2 = 2 * ln2

# Combine the terms: -γ - 2*ln(2)
result = -euler_gamma - two_ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))