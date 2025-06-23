import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the complete elliptic integral of the first kind at k=0.5
k_value = mp.mpf('0.5')
K_half = mp.ellipk(k_value)  # K(0.5)

# Multiply by 3/2
term = mp.mpf('3') / mp.mpf('2') * K_half  # (3/2) * K(0.5)

# Subtract pi to get the final result
result = term - mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))