import mpmath as mp

# Set the decimal precision for calculations
mp.dps = 15

# Define the argument for the dilogarithm: e^(i*π/3)
z = mp.exp(1j * mp.pi / 3)

# Calculate the dilogarithm Li_2(z)
li2_val = mp.polylog(2, z)

# Extract the real part
real_part = li2_val.real

# Multiply by 2 to get the final result
result = 2 * real_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))