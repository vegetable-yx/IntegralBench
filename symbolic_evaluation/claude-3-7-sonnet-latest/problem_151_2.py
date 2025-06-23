import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the argument for the elliptic integral: 1/sqrt(2)
k_value = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind K(k)
K_val = mp.ellipk(k_value)

# Square the result of the elliptic integral
K_squared = K_val ** 2

# Multiply by pi to get the final result
result = mp.pi * K_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))