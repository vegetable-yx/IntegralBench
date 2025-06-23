import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute modified Bessel functions of the first kind at z=1
I0 = mp.besseli(0, 1)  # I₀(1) calculation
I1 = mp.besseli(1, 1)  # I₁(1) calculation

# Calculate the final result using π*(I₀(1) - I₁(1))
result = mp.pi * (I0 - I1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))