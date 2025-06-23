import mpmath as mp
mp.dps = 15

# Compute Struve H function H_0(1)
struve_h0 = mp.struveh(0, 1)

# Compute modified Struve L function L_0(1)
struve_l0 = mp.struvel(0, 1)

# Calculate each component of the solution
term1 = (mp.pi/2) * (1 - struve_h0)
term2 = (mp.pi/2) * struve_l0

# Combine terms for final result
result = term1 - term2

# Output with 10 decimal precision
print(mp.nstr(result, n=10))