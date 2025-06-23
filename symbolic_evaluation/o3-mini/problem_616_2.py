import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide pi squared by 48
term1 = pi_sq / 48

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm of 2
ln2_sq = mp.power(ln2, 2)

# Divide the squared logarithm by 4
term2 = ln2_sq / 4

# Sum the two terms
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))