import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerical value of 5π/8
coefficient = mp.mpf(5)/8  # Convert 5/8 to high-precision float
result = coefficient * mp.pi  # Multiply by π

print(mp.nstr(result, n=10))  # Print result with 10 decimal places