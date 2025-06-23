import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the parameters for the hypergeometric function
a = mp.mpf('1.5')   # 3/2
b = mp.mpf('0.75')  # 3/4
c = mp.mpf('2.0')   # 2
z = mp.mpf('0.25')  # 1/4

# Calculate the hypergeometric function 2F1(a, b; c; z)
hyper = mp.hyp2f1(a, b, c, z)

# Calculate the constant factor: π * √2 / 4
constant_factor = (mp.pi * mp.sqrt(2)) / 4

# Compute the final result by multiplying the constant factor with the hypergeometric function
result = constant_factor * hyper

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))