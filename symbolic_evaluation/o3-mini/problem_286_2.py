import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define constants and intermediate values
sqrt2 = mp.sqrt(2)  # √2

# Calculate argument for the first log squared term: (√2 + 1)/2
a = (sqrt2 + 1) / 2

# Calculate argument for the second log term: (3 + 2√2)/2
b = (3 + 2 * sqrt2) / 2

# Calculate argument for the first dilogarithm: 1 - √2/2
c1 = 1 - sqrt2/2

# Calculate argument for the second dilogarithm: √2/2
c2 = sqrt2/2

# Compute the logarithms needed
log_a = mp.log(a)
log_b = mp.log(b)

# Calculate each term of the expression
# Term1: (π/32) * [ln((√2+1)/2)]^2
term1 = (mp.pi / 32) * (log_a ** 2)

# Term2: (1/16) * ln((√2+1)/2) * ln((3+2√2)/2)
term2 = (1/16) * log_a * log_b

# Term3: -(1/8) * Li₂(1 - √2/2)
term3 = (-1/8) * mp.polylog(2, c1)

# Term4: (1/8) * Li₂(√2/2)
term4 = (1/8) * mp.polylog(2, c2)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))