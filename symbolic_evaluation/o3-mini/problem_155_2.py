import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the constant pi squared
pi_sq = mp.pi ** 2

# Calculate the natural logarithm of 2
ln2 = mp.log(2)
# Compute the square of ln(2)
ln2_sq = ln2 ** 2

# Compute the dilogarithm (polylog(2, x)) at 1/2 and -1/2
li2_half = mp.polylog(2, 0.5)
li2_neg_half = mp.polylog(2, -0.5)

# Construct the numerator: pi^2 - 2*(ln(2))^2 - 4*Li2(1/2) + 4*Li2(-1/2)
numerator = pi_sq - 2*ln2_sq - 4*li2_half + 4*li2_neg_half

# Divide by 8 to get the final result
result = numerator / 8

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))