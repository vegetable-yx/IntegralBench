import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: (π * √2) / 2
constant_factor = (mp.pi * mp.sqrt(2)) / 2

# Calculate the hypergeometric function: _1F_2(1.0; [1.25, 0.75]; 0.25)
# Using mp.hyper with parameters [a1], [b1, b2], z
hyp = mp.hyper([1.0], [1.25, 0.75], 0.25)

# Compute the final result by multiplying the constant factor with the hypergeometric function
result = constant_factor * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))