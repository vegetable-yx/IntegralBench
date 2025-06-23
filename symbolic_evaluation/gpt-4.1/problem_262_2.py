import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute components of the analytical solution
term1 = 1 - mp.besselj(0, 2)  # 1 - J_0(2)
term2 = mp.struveh(0, 2)      # Struve H_0(2)

# Combine terms with proper scaling
result = (mp.pi / 8) * (term1 - term2)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))