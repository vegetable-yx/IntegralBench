import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate e^(pi/4)
exp_pi4 = mp.exp(mp.pi/4)

# Multiply sqrt(2) by e^(pi/4)
sqrt2_times_exp_pi4 = sqrt_2 * exp_pi4

# Subtract 1 from the product
numerator = sqrt2_times_exp_pi4 - 1

# Divide by 2 to get final result
result = numerator / 2

print(mp.nstr(result, n=10))