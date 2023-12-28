#NON SYSTEMATIC CYCLIC CODE long code
import numpy as np

def generate_polynomial(coefficients):
    # Convert the binary coefficients to decimal
    decimal_coefficients = [int(coeff, 2) for coeff in coefficients]
    # Use numpy's poly1d function to create a polynomial
    polynomial = np.poly1d(decimal_coefficients, variable='x')
    return polynomial

gen_bin = ["0","1", "0", "1"]  # Represents x^2 + 1
code1 = ["1","0","1","1"]

# Generate the polynomial
resulting_polynomial = poly1 = generate_polynomial(gen_bin)
print("Generated Polynomial:")
print(resulting_polynomial)

resulting_polynomial = poly2 = generate_polynomial(code1)
print("message polynomial: ")
print(resulting_polynomial)

def multiply_polynomials(poly1, poly2):
    # Multiply two polynomials using numpy's poly1d class
    result_poly = np.polymul(poly1, poly2)
    return result_poly

# Multiply the polynomials
result = poly = multiply_polynomials(poly1, poly2)
print("Result of Multiplication:")
print(result)

def polynomial_to_binary(polynomial):
    coefficients = polynomial.coefficients
    highest_degree = len(coefficients) - 1
    binary_coefficients = ['1' if coefficients[i] == 1 else '0' for i in range(highest_degree, -1, -1)]
    binary_representation = ''.join(binary_coefficients)
    return binary_representation

# Convert the polynomial to binary representation
binary_representation = polynomial_to_binary(poly)

# Print the result
print("Binary Representation of the Polynomial:")
print(binary_representation)





#short code

def polynomial_multiply(poly1, poly2):
    m, n = len(poly1), len(poly2)
    result = [0] * (m + n - 1)
    for i in range(m):
        for j in range(n):
            result[i + j] ^= poly1[i] * poly2[j]
    return result
message = input("Enter the message as a binary string: ")
generator_poly = [1, 1, 0, 1]
message_poly = list(map(int, message))
non_systematic_code = polynomial_multiply(message_poly, generator_poly)
print("Message (M(x)): ", message)
print("Generator Polynomial (G(x)): ", generator_poly)
print("Non-Systematic Cyclic Code (N(x)): ", non_systematic_code)
