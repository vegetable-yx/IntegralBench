import mpmath as mp

mp.dps = 15  # Set internal precision

# Define parameters for the hypergeometric function
a = [mp.mpf('3/2'), mp.mpf(1)]
b = [mp.mpf('1/2'), mp.mpf('5/4'), mp.mpf('7/4')]
z = mp.mpf(9)/4

# Calculate the hypergeometric function 2F3
hyp = mp.hyper(a, b, z)

# Compute the constant factor 3^(3/2) = 3*sqrt(3)
constant_factor = 2 * mp.sqrt(3)  # 3^(3/2) * (2/3) = 2*sqrt(3)

# Calculate the final result
result = constant_factor * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))