import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Define parameters for the hypergeometric function 3F2
a1 = mp.mpf('0.5')
a2 = mp.mpf(1)
a3 = mp.mpf(1)
b1 = mp.mpf(2)
b2 = mp.mpf(2)
z = mp.mpf(1)

# Calculate the hypergeometric function value
hyper3f2_value = mp.hyp3f2(a1, a2, a3, b1, b2, z)

# Multiply by π/4 to get final result
result = (mp.pi / 4) * hyper3f2_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))