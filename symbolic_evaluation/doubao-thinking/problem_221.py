import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerical value of 3π/16
pi_value = mp.pi
coefficient = mp.mpf(3)/mp.mpf(16)  # Compute 3/16 with high precision
result = coefficient * pi_value     # Multiply by the coefficient

print(mp.nstr(result, n=10))