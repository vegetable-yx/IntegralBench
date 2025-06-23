import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k)

# Square the elliptic integral result
E_squared = E_value ** 2

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * E_squared

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))