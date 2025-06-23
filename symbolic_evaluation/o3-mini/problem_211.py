import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument
x = mp.mpf('0.5')

# Calculate Bessel functions of the first kind
j_n14 = mp.besselj(-mp.mpf('0.25'), x)  # J_{-1/4}(1/2)
j_p14 = mp.besselj(mp.mpf('0.25'), x)   # J_{1/4}(1/2)

# Calculate Struve functions (Hankel variant)
h_n14 = mp.struveh(-mp.mpf('0.25'), x)  # H_{-1/4}(1/2)
h_p14 = mp.struveh(mp.mpf('0.25'), x)   # H_{1/4}(1/2)

# Compute the product terms
term1 = j_n14 * h_n14  # J_{-1/4} * H_{-1/4}
term2 = j_p14 * h_p14  # J_{1/4} * H_{1/4}

# Combine terms and multiply by π/2
result = (mp.pi / 2) * (term1 - term2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))