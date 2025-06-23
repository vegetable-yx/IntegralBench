import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Initialize the summation variables
sum_part = mp.mpf(0)
four = mp.mpf(4)  # Base for the exponential term
n = 1  # Starting index for the series

# Compute terms until they become smaller than 1e-15
while True:
    denominator = (n**2) * (n + 1) * (four**n)
    term = mp.mpf(1) / denominator
    sum_part += term
    # Check if term is below precision threshold
    if mp.fabs(term) < 1e-15:
        break
    n += 1

# Multiply by π/8 to get the final result
result = (mp.pi / 8) * sum_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))