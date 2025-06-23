import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define truncation limits for the double sum
M_max = 100
N_max = 100
k_max = 2 * M_max  # Maximum k = m + n

# Precompute coefficients a_m and a_n
a_list = []
base = mp.mpf(16)  # Base for the exponential term
for i in range(0, M_max + 1):
    num = mp.factorial(2 * i)
    denom = mp.factorial(i)**2 * (base**i) * (2 * i + 1)
    a_i = num / denom
    a_list.append(a_i)

# Precompute bracket terms for each k = m + n
bracket_list = []
for k in range(0, k_max + 1):
    term1 = mp.pi / (4 * k + 8)  # First part of the bracket
    num_g = mp.gamma(k + 3.5)  # Gamma(k + 7/2)
    denom_g = (4 * k + 8) * mp.sqrt(mp.pi) * mp.gamma(k + 3)
    term2 = num_g / denom_g  # Second part of the bracket
    bracket = term1 - term2
    bracket_list.append(bracket)

# Initialize total sum
total = mp.mpf(0)

# Double sum over m and n
for m in range(0, M_max + 1):
    for n in range(0, N_max + 1):
        k = m + n
        if k <= k_max:  # Ensure k is within precomputed range
            term = a_list[m] * a_list[n] * bracket_list[k]
            total += term

# Multiply by the outer factor 1/4
result = total / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))