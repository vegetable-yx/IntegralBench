import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_total = mp.mpf(0)  # Initialize sum with mpmath precision

for k in range(5):  # Sum from k=0 to k=4
    binom = mp.binomial(4, k)  # Calculate binomial coefficient (4 choose k)
    exponent = (-1) ** (25 - 5 * k)  # Compute (-1) raised to (25-5k)
    denominator = 25 - 5 * k  # Calculate denominator term
    term = binom * exponent / denominator  # Compute individual term
    sum_total += term  # Accumulate sum

result = 5 * sum_total  # Multiply final sum by 5

print(mp.nstr(result, n=10))  # Print result with 10 decimal places