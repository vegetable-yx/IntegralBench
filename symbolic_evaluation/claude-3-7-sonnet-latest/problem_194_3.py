import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide pi squared by 16
term1 = pi_squared / 16

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Multiply ln(2) by 1/4
term2 = 0.25 * ln2

# Compute the constant term -1/4
term3 = -0.25

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))