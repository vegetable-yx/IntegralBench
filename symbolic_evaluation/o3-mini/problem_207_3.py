import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

# Compute the difference of digamma functions: ψ(3/4) - ψ(1/4)
d3_4 = mp.digamma(mp.mpf('3/4'))  # Digamma of 3/4
d1_4 = mp.digamma(mp.mpf('1/4'))  # Digamma of 1/4
diff_digamma = d3_4 - d1_4

# Compute the constant factor: -√π / 4
sqrt_pi = mp.sqrt(mp.pi)
factor = -sqrt_pi / 4

# Combine to get the final result
result = factor * diff_digamma

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))