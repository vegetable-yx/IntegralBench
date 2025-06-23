import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Divide pi squared by 16
pi_sq_div_16 = pi_sq / 16

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply the two parts to get the result
result = pi_sq_div_16 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))