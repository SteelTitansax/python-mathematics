"""

NOTA : Introducir la factorizacion considerando la sinergia entre funciones convert_to_fraction y find factors
        el chatbot pediria numero o fraccion dependiendo de lo que entre generaria la factorizacion. 
"""

# Convert string input ( including fractions ) to float 

def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans

def convert_to_fraction():
        
    # Convert decimals to fractions 

    # Get string input , which will include a decimal point 

    digits = input ("Enter a decimal number to convert: ")

    # Get number of decimal places as an integer 

    exponent = int(len(digits)) - 2

    # Convert the input to a float number 

    n = float(digits)

    # Use the exponent to get the numerator

    numerator = int(n * 10**exponent)

    # Use the exponent to get the denominator 

    denominator = 10**exponent 

    # Percent is the first two decimal places 

    percent = n * 100

    # Output 

    print("The decimal is", n)
    print("The fraction is", numerator,"/", denominator)
    print("The percent is", percent ,"%")

def find_factors(numerator,denominator):

    factor = 0

    for factor_number in range(1,denominator+1):

        if numerator%factor_number == 0 and denominator%factor_number == 0:
            factor=factor_number
    
    # Divide out the greatest common factor

    n = int(numerator/factor)
    d = int(denominator/factor)

    print("original : ", numerator, " / ", denominator)
    print("reduced : ", n, " / ", d)

