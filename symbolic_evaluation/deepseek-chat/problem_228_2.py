import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute pi squared divided by 24
term1 = pi_sq / 24

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm
term2 = ln2 ** 2

# Sum the two terms: pi^2/24 + ln(2)^2
inner_sum = term1 + term2

# Multiply by pi/2
result = (mp.pi / 2) * inner_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))