import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the input parameter 'a' (user can modify this value)
a = 1.0

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, a)  # I_0(a)
I1 = mp.besseli(1, a)  # I_1(a)

# Compute modified Struve functions
L0 = mp.struvel(0, a)  # L_0(a)
L1 = mp.struvel(1, a)  # L_1(a)

# Calculate the expression inside the first brackets: [1 - I_0(a) + L_0(a)]
bracket1 = 1 - I0 + L0

# Multiply by π/4: π/4 * [1 - I_0(a) + L_0(a)]
term1 = (mp.pi / 4) * bracket1

# Calculate the expression inside the second brackets: [L_1(a) - I_1(a)]
bracket2 = L1 - I1

# Multiply by 1/2: (1/2) * [L_1(a) - I_1(a)]
term2 = 0.5 * bracket2

# Combine both terms: F(a) = term1 - term2
result = term1 - term2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))