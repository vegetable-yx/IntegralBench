import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, 2)  # I_0(2)
I1 = mp.besseli(1, 2)  # I_1(2)

# Compute modified Struve functions
L0 = mp.struvel(0, 2)  # L_0(2)
L1 = mp.struvel(1, 2)  # L_1(2)

# Calculate the term involving Bessel functions: 16*I1(2) - 8*I0(2)
bessel_term = 16 * I1 - 8 * I0

# Calculate the Struve component: 2*L1(2) - L0(2)
struve_component = 2 * L1 - L0

# Multiply Struve component by pi: π * [2L1(2) - L0(2)]
pi_times_struve = mp.pi * struve_component

# Combine the two main parts: Bessel term + pi*Struve component
inner_sum = bessel_term + pi_times_struve

# Multiply by 2/15 to get the final result
result = (2 / 15) * inner_sum

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))