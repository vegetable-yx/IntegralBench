import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate trigamma function at 1/3
trigamma_one_third = mp.polygamma(1, mp.mpf(1)/3)

# Calculate trigamma function at 2/3
trigamma_two_thirds = mp.polygamma(1, mp.mpf(2)/3)

# Compute the difference between trigamma values
diff_trigamma = trigamma_one_third - trigamma_two_thirds

# Multiply by 1/12 to get final result
result = diff_trigamma / 12

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))