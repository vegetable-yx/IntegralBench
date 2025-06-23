import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

sum_result = mp.mpf(0)  # Initialize sum with mpmath floating point

for k in range(0, 5):  # Iterate over k from 0 to 4 inclusive
    binom = mp.binomial(4, k)  # Calculate binomial coefficient (4 choose k)
    exponent = 25 - 5 * k  # Compute exponent for (-1) term
    sign = (-1) ** exponent  # Determine the sign of the term
    denominator = 25 - 5 * k  # Compute denominator for the fraction
    term = binom * sign / denominator  # Calculate individual term
    sum_result += term  # Accumulate terms in the sum

result = 5 * sum_result  # Multiply the final sum by 5

print(mp.nstr(result, n=10))  # Print result with 10 decimal places