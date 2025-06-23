import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values, can be changed)
a = 1.0
b = 1.0

# Compute z = (b^2 * a) / 16
z = (b**2 * a) / 16.0

# Calculate the first hypergeometric function: 0F1(;1;z)
F1 = mp.hyper([], [1], z)

# Calculate the second hypergeometric function: 0F1(;3/2;z)
F2 = mp.hyper([], [1.5], z)  # 3/2 = 1.5

# Compute Gamma(1/4) and Gamma(3/4)
gamma_14 = mp.gamma(0.25)    # Gamma(1/4)
gamma_34 = mp.gamma(0.75)    # Gamma(3/4)

# Compute the ratio: Gamma(1/4) / Gamma(3/4)
gamma_ratio = gamma_14 / gamma_34

# First term: π√2 * 0F1(;1;z)
term1 = mp.pi * mp.sqrt(2) * F1

# Second term: [b * Gamma(1/4) / (2 * Gamma(3/4))] * 0F1(;3/2;z)
term2 = (b * gamma_ratio) / 2 * F2

# Combine terms and multiply by √a
result = mp.sqrt(a) * (term1 + term2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))