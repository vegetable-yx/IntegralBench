import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute π/8
pi_over_8 = mp.pi / 8

# Compute ln(2)
ln2 = mp.log(2)

# Compute (1/4) * ln(2)
quarter_ln2 = ln2 / 4

# Sum the two terms to get the final result
result = pi_over_8 + quarter_ln2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))