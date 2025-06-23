import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute components of the first term: (π*(4√2 -5))/72
sqrt2 = mp.sqrt(2)  # Calculate square root of 2
numerator_part1 = 4 * sqrt2 - 5  # Compute (4√2 -5)
term1 = (mp.pi * numerator_part1) / 72  # First term calculation

# Compute components of the second term: (π/6)(ln(1+√2) - ln2)
log_diff = mp.log(1 + sqrt2) - mp.log(2)  # Calculate logarithmic difference
term2 = (mp.pi / 6) * log_diff  # Second term calculation

# Combine terms and format result
result = term1 + term2
print(mp.nstr(result, n=10))