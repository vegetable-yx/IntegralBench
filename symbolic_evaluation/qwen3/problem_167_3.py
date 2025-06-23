import mpmath as mp
mp.dps = 15

# Calculate constants and components
pi = mp.pi
ln3 = mp.log(3)

# Compute (8π/3) * ln(3)
term1 = (8 * pi) / 3
term1 = term1 * ln3

# Compute 4π/3
term2 = (4 * pi) / 3

# Final result by subtraction
result = term1 - term2

print(mp.nstr(result, n=10))