import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate components of the analytical solution
struve_term = mp.struveh(0, 1)  # Compute Struve H_0(1)
pi_half = mp.pi / 2             # Precompute π/2

# Combine terms according to analytical expression
result = pi_half * struve_term - 1

# Output final result with 10 decimal precision
print(mp.nstr(result, n=10))