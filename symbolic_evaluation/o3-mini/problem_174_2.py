import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute intermediate values
a = mp.asin(1/4)              # arcsin(1/4)
b = mp.atan(mp.sqrt(15))       # arctan(sqrt(15))

# Compute complex arguments for dilogarithms
z1 = 1/4 + 1j * mp.sqrt(15)/4  # (1 + i*sqrt(15))/4
z2 = 1/4 - 1j * mp.sqrt(15)/4  # (1 - i*sqrt(15))/4

# Compute dilogarithms
dilog1 = mp.polylog(2, z1)
dilog2 = mp.polylog(2, z2)

# Combine terms inside the brackets
term1 = mp.pi * a**2           # π * [arcsin(1/4)]^2
term2 = -2 * b * a             # -2 * arctan(sqrt(15)) * arcsin(1/4)
term3 = dilog1 + dilog2        # Sum of dilogarithms
inner_sum = term1 + term2 + term3

# Multiply by π/8 for final result
result = (mp.pi / 8) * inner_sum

# Output result to 10 decimal places
print(mp.nstr(result, n=10))