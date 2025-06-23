import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the modified Bessel functions I0(3) and I1(3)
I0 = mp.besseli(0, 3)
I1 = mp.besseli(1, 3)

# Sum the Bessel function results
sum_bessel = I0 + I1

# Calculate the coefficient (3*sqrt(3))/2
coefficient = (3 * mp.sqrt(3)) / 2

# Compute the final result
result = coefficient * sum_bessel

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))