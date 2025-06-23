import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the parameter 'a' (user can modify this value as needed)
a = 1.0  # Example value, can be changed to any real number

# Convert 'a' to mpmath floating-point number for precision
a_mp = mp.mpf(a)

# Compute the common argument (a^2)/4 for the hypergeometric functions
arg = a_mp**2 / 4

# Calculate the first hypergeometric term: _0F_1(; 3/2; a^2/4)
hyp1 = mp.hyp0f1(mp.mpf('1.5'), arg)  # 1.5 = 3/2

# Calculate the second hypergeometric term: _0F_1(; 5/2; a^2/4)
hyp2 = mp.hyp0f1(mp.mpf('2.5'), arg)  # 2.5 = 5/2

# Compute the first component: -2/3 * hyp1
term1 = -mp.mpf(2)/3 * hyp1

# Compute the second component: 5/3 * hyp2
term2 = mp.mpf(5)/3 * hyp2

# Sum the components to get the final result
result = term1 + term2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))