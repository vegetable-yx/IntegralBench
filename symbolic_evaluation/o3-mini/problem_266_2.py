To evaluate the given analytical expression \(\frac{\pi}{2}\left[J_0(a)\mathbf{H}_0(a) - J_1(a)\mathbf{H}_1(a)\right]\) to 10 decimal places using mpmath, we follow these steps:

1. Set the internal precision to 15 decimal places using `mpmath.dps = 15`.
2. Define the parameter `a` (here set to 1.0 as an example; adjust as needed).
3. Compute the Bessel functions \(J_0(a)\) and \(J_1(a)\) using `mp.besselj`.
4. Compute the Struve functions \(\mathbf{H}_0(a)\) and \(\mathbf{H}_1(a)\) using `mp.struveh`.
5. Calculate the intermediate terms: \(J_0(a)\mathbf{H}_0(a)\) and \(J_1(a)\mathbf{H}_1(a)\).
6. Subtract these terms and multiply by \(\frac{\pi}{2}\).
7. Print the result formatted to 10 decimal places using `mp.nstr`.

Here's the Python code implementing these steps:

import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example: a = 1.0)
a = 1.0

# Compute Bessel function of the first kind, order 0
J0 = mp.besselj(0, a)

# Compute Struve function (Hankel), order 0
H0 = mp.struveh(0, a)

# Compute Bessel function of the first kind, order 1
J1 = mp.besselj(1, a)

# Compute Struve function (Hankel), order 1
H1 = mp.struveh(1, a)

# Calculate J0(a) * H0(a)
term1 = J0 * H0

# Calculate J1(a) * H1(a)
term2 = J1 * H1

# Compute the expression inside the brackets: term1 - term2
bracket_term = term1 - term2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bracket_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))

**Note:** The variable `a` is set to `1.0` as an example. To evaluate the expression for a different value of `a`, simply modify the line `a = 1.0` accordingly. The code outputs a single floating-point number with 10 decimal places.