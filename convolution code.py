#CONVOLUTIONAL CODE long 

import numpy as np

gen_po = ["0","1","0","1","1"] # Represents x^2 + 1
code1 = ["1","0","1"]
code2 = ["0","1","1"]
code3 = ["1","1","0"]
n= (code1,code2,code3)

def generate_polynomial(coefficients):
    # Convert the binary coefficients to decimal
    decimal_coefficients = [int(coeff, 2) for coeff in coefficients]
    # Use numpy's poly1d function to create a polynomial
    polynomial = np.poly1d(decimal_coefficients, variable='x')
    return polynomial

def multiply_polynomials(poly1, poly2):
    # Multiply two polynomials using numpy's poly1d class
    result_poly = np.polymul(poly1, poly2)
    return result_poly

def polynomial_to_binary(polynomial):
    coefficients = polynomial.coefficients
    highest_degree = len(coefficients) - 1
    binary_coefficients = ['1' if coefficients[i] == 1 else '0' for i in range(highest_degree, -1, -1)]
    binary_representation = ''.join(binary_coefficients)
    return binary_representation


# Generate the polynomial
poly1 = generate_polynomial(gen_po)
print("Generated Polynomial: ")
print(poly1,"\n")

c=1
for code in n:
    print(" codeword: ",c,"\n")
    poly2 = generate_polynomial(code)
    print("message polynomial: ")
    print(poly2,"\n")


    # Multiply the polynomials
    poly = multiply_polynomials(poly1, poly2)
    print("Result of Multiplication: ")
    print(poly,"\n")


    # Convert the polynomial to binary representation
    binary_representation = polynomial_to_binary(poly)

    # Print the result
    print("Binary Representation of the Polynomial: ")
    print(binary_representation,"\n")

    c+=1







#short code

import numpy as np
codewords=[]
def encode_message(message, generator_polynomial):
    message = np.array(list(message), dtype=int)
    generator_polynomial = np.array(list(generator_polynomial), dtype=int)

    # Perform convolution
    encoded_message = np.convolve(message, generator_polynomial, mode='full') % 2
    return ''.join(map(str, encoded_message))

def main():
    message = input("Enter the message (binary): ")

    # Get three generator polynomials from the user
    poly1 = input("Enter the first generator polynomial (binary): ")
    poly2 = input("Enter the second generator polynomial (binary): ")
    poly3 = input("Enter the third generator polynomial (binary): ")

    # Encode the message using each generator polynomial
    encoded_message1 = encode_message(message, poly1)
    encoded_message2 = encode_message(message, poly2)
    encoded_message3 = encode_message(message, poly3)

    print("Encoded Message 1:", encoded_message1)
    print("Encoded Message 2:", encoded_message2)
    print("Encoded Message 3:", encoded_message3)

    for i in range(6):
      codewords.append(encoded_message1[i])
      codewords.append(encoded_message2[i])
      codewords.append(encoded_message3[i])
      # Print the elements separated by a space
    print("c(x)= ")
    print(" ".join(map(str, codewords)))

if __name__ == "__main__":
    main()
