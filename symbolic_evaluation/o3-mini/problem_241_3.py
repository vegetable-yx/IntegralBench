import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute digamma function at 1/2
digamma_half = mp.digamma(0.5)

# Compute digamma function at 1
digamma_one = mp.digamma(1)

# Calculate the difference: ψ(1/2) - ψ(1)
diff_digamma = digamma_half - digamma_one

# Multiply the difference by 1/16
result = diff_digamma / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))