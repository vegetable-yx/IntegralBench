import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the infinite series using polylogarithms
Li2_half = mp.polylog(2, 0.5)       # Li_2(1/2)
Li2_quarter = mp.polylog(2, 0.25)   # Li_2(1/4)

# Compute even-indexed terms contribution (sum over 1/4^n/(2n)^2)
sum_even_contribution = 0.25 * Li2_quarter

# Calculate the series sum by subtracting even terms from full polylog(2, 1/2)
series_sum = 2 * (Li2_half - sum_even_contribution)

# Compute the final result using the analytical expression
result = (4 - 3 * series_sum) / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))