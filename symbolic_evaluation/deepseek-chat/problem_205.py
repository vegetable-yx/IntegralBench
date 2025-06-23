import mpmath as mp

# Set the precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Define the variable and constants
# The integral result is expressed in terms of special functions and constants
# Result = \frac{\pi \sqrt{2}}{4} \left( \frac{1}{2} \mathbf{L}_{-1}\left(\frac{\sqrt{2}}{2}\right) + \frac{1}{2} \mathbf{H}_{-1}\left(\frac{\sqrt{2}}{2}\right) \right)

# Calculate the argument z = sqrt(2)/2
z = mp.sqrt(2) / 2

# Compute the modified Struve function L_{-1}(z)
struveL = mp.struvel(-1, z)

# Compute the Hankel Struve function H_{-1}(z)
struveH = mp.struveh(-1, z)

# Combine the Struve functions: (struveL + struveH) / 2
combined_struve = (struveL + struveH) / 2

# Multiply by the constant factor: (pi * sqrt(2) / 4) * combined_struve
result = (mp.pi * mp.sqrt(2) / 4) * combined_struve

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))