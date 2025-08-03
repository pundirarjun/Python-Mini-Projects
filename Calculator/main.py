# A Calculator for Simple arthematic operation, Trigonometric operation and Matrices

import numpy as np
import math
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    print("\n--- Select Operation ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (a^b)")
    print("6. Modulus (a % b)")

    while True:
        choice = input("Enter the choice (1/2/3/4/5/6): ")
        if choice in ("1", "2","3","4","5","6"):
            return choice
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, 5, 6.")


def simple_calculator():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    operation = get_operation()

    if operation == "1":
        print(f"Result: {a} + {b} = {a + b}")
    elif operation == "2":
        print(f"Result: {a} - {b} = {a - b}")
    elif operation == "3":
        print(f"Result: {a} * {b} = {a * b}")
    elif operation == "4":
        if b == 0:
            print("Division: Undefined (can't divide by zero)")
        else:
            print(f"Result: {a} / {b} = {a / b}")
    elif operation == "5":
        print(f"Result: {a} ^ {b} = {a ** b}")
    elif operation == "6":
        if b == 0:
            print("Modulus: Undefined (cannot mod by zero.)")
        else:
            print(f"Result: {a} % {b} = {a % b}")
    else:
        print("Invalid operation")


def trigonometric_calculator():
    print("\n --- Trigonometric Calculator ---")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    choice = input("Enter the choice (1/2/3): ")

    if choice in ["1","2","3"]:
        angle = get_number("Enter angle in degrees: ")
        radians = math.radians(angle)

        if choice == "1":
            result = math.sin(radians)
            print(f"sin({angle}) = {round(result, 6)}")
        elif choice == "2":
            result = math.cos(radians)
            print(f"cos({angle}) = {round(result, 6)}")
        elif choice == "3":
            result = math.tan(radians)
            print(f"tan({angle}) = {round(result, 6)}")
    else:
        print("Invalid operation")



def get_matrix(name= "matrix"):
    print(f"Enter number of rows for {name}")
    rows = int(input())
    print(f"Enter number of columns for {name}")
    cols = int(input())
    print(f"Enter the entries row-wise (with space): ")
    matrix_entries = []

    for i in range(rows):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            if len(row_input) != cols:
                print(f"Please enter exactly {cols } values.")
                continue
            try:
                row = [float(x) for x in row_input]
                matrix_entries.append(row)
                break
            except ValueError:
                print("Please enter valid number.")
    return np.array(matrix_entries)

def matrix_calculator():
    print("\n --- Matrix Calculator ---")
    print("Operations: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")

    choice = input("Choose operation (1-6): ")

    if choice in ["1", "2", "3"]:
        a = get_matrix("first matrix")
        b = get_matrix("second matrix")

        if choice == "1":
            if a.shape != b.shape:
                print("Error: Matrices must have the same dimensions for addition.")
                return
            result = a + b
            print("Result of addition:\n", result)
        
        elif choice == "2":
            if a.shape != b.shape:
                print("Error: Matrices must have the same dimensions for subtraction.")            
                return
            result = a - b
            print("Result of subtraction:\n", result)
        
        elif choice == "3":
            if a.shape[1] != b.shape[0]:
                print("Error: Number of column of the first matrix must equal number of rows of second matrix for multiplication.")            
                return
            result = np.dot(a, b)
            print("Result of multiplication:\n", result)

    elif choice == "4":
        a = get_matrix()
        result = a.T
        print("Transpose of matrix:\n", result)
    
    elif choice == "5":
        a = get_matrix()
        if a.shape[0] != a.shape[1]:
            print("Error: Determinant can be calculated only for square matrices.")
            return
        det = np.linalg.det(a)
        print(f"Determinant: {det}")
        
    elif choice == "6":
        a = get_matrix()
        if a.shape[0] != a.shape[1]:
            print("Error: Inverse can be calculated only for square matrices.")
            return
        try:
            inv = np.linalg.inv(a)
            print("Inverse of matrix:\n", inv)
        except np.linalg.LinAlgError:
            print("Error: Matrix is singular and cannot be inverted.")
        
        else:
            print("Invalid choice.")


def main_calculator():
    while True:
        print("\n --- Select Calculator ---")
        print("1. Simple Calculator")
        print("2. Trigonometric Calculator")
        print("3. Matrix Calculator")
        print("4. Exit")
        mode = input("Enter choice (1/2/3/4): ")
        if mode == "1":
            simple_calculator()
        elif mode == "2":
            trigonometric_calculator()
        elif mode == "3":
            matrix_calculator()
        elif mode == "4":
            print("Thank you for using my Calculator")
            break
        else:
            print("Invalid mode: Please enter 1, 2, 3 or 4")
    

main_calculator()

    





