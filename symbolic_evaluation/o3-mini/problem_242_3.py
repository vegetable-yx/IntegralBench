import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the points as exact fractions
point1 = mp.mpf('1/3')  # 1/3
point2 = mp.mpf('2/3')  # 2/3

# Compute digamma function at 1/3
digamma_1_3 = mp.digamma(point1)

# Compute digamma function at 2/3
digamma_2_3 = mp.digamma(point2)

# Compute the difference: ψ(2/3) - ψ(1/3)
diff_digamma = digamma_2_3 - digamma_1_3

# Multiply the difference by 1/12
result = diff_digamma / 12

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))