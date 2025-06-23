import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute the Struve H function of order 0 at 2
H0_value = mp.struveh(0, 2)

# Calculate the (1 - H_0(2)) component
one_minus_H = 1 - H0_value

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * one_minus_H

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))