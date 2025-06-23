import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute intermediate constants
sqrt2 = mp.sqrt(2)
term1 = 1 - 1/sqrt2  # Argument for first polylog
term2 = 1 + 1/sqrt2  # Argument for second polylog
term3 = 3 - 2*sqrt2  # Argument for first logarithm
term4 = 2 + sqrt2    # Argument for second logarithm

# Calculate polylogarithm terms
Li1 = mp.polylog(2, term1)  # Li₂(1 - 1/√2)
Li2 = mp.polylog(2, term2)  # Li₂(1 + 1/√2)

# Calculate logarithmic terms
log1 = mp.log(term3)  # ln(3 - 2√2)
log2 = mp.log(term4)  # ln(2 + √2)

# Combine terms inside the braces
inner_expr = Li1 - Li2 + 0.5 * log1 * log2

# Multiply by -√2 for final result
result = -sqrt2 * inner_expr

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))