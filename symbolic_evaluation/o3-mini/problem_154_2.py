import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Calculate the dilogarithm (Li_2) at 1/2
li2_half = mp.polylog(2, 0.5)

# Calculate the trilogarithm (Li_3) at 1/2
li3_half = mp.polylog(3, 0.5)

# Compute ln^3(2)
ln2_cubed = ln2 ** 3

# Calculate the first term: 26 * Li_3(1/2)
term1 = 26 * li3_half

# Calculate the second term: -13 * ln2 * Li_2(1/2)
term2 = -13 * ln2 * li2_half

# Sum all terms: term1 + term2 + ln2_cubed
total_sum = term1 + term2 + ln2_cubed

# Multiply by 1/8 to get the final result
result = total_sum / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))