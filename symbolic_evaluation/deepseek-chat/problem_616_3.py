import mpmath as mp

# Set internal decimal precision to 15 for reliable 10-digit output
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Square ln(2)
ln2_sq = ln2**2

# Divide by 4 to get first term
term1 = ln2_sq / 4

# Calculate pi squared
pi_sq = mp.pi**2

# Divide by 16 to get second term
term2 = pi_sq / 16

# Sum both terms
result = term1 + term2

# Print final result to exactly 10 decimal places
print(mp.nstr(result, n=10))