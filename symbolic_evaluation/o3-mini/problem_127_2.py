import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the generalized hypergeometric function 1F2
# Arguments: a = [1/4], b = [1/2, 3/4], z = 1/16
hyp = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(3)/4], mp.mpf(1)/16)

# Calculate the constant factor: (π * √2) / 4
constant_factor = (mp.pi * mp.sqrt(2)) / 4

# Multiply the constant factor by the hypergeometric function
result = constant_factor * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))