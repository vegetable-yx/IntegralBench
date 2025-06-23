import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the argument 1/√2
arg = 1 / mp.sqrt(2)

# Calculate the complete elliptic integral of the second kind E(1/√2)
E_value = mp.ellipe(arg)

# Square the elliptic integral result
E_squared = E_value ** 2

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * E_squared

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))