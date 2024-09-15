import subprocess
import sys
required_packages = [
    "numpy",
    "matplotlib"
]
def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing {package}: {e}")
            sys.exit(1)
def main():
    install_packages(required_packages)
    print("All packages installed successfully. Running the main code...")
if __name__ == "__main__":
    main()
import cmath
print("We know that the Structure of Quadratuc Equation is...")
print(" ")
print(" ax**2 + bx + c = 0 ")
print(" ")
print("Now...")
print(" ")
a = int(input("Please enter the value of a where a!=0 : "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))
print(" ")
print("The Formula of Quadratic equation is...")
print(" ")
print("x=[-b+-sqrt{(b**2)-4ac}]/2a")
print(" ")
print("So, the Discriminant is....")
print(" ")
print("d = (b**2)- (4*a*c)")
print(" ")
d = (b**2)- (4*a*c)
print(" ")
sol1 = (-b - cmath.sqrt(d)) / (2*a)
sol2 = (-b + cmath.sqrt(d)) / (2*a)
print(f"So, the result of the equation, '{a}x**2 + {b}x + {c} = 0', should be..: ")
print(" ")
print(f"the solution are {sol1} and {sol1}")
print(" ")
if d>0:
    print("This is a 'Two Distinct Real Root' type")
elif d == 0:
    print("This is a 'Two Equal Real Root' type")
elif d<0:
    print("This is a 'Two Complex Real Root' type")
print(" ")
user_input = input("Do you want to graphically see the value? (y/n): ").strip().lower()
if user_input == 'y':
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title('Graph of Quadratic Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    print("Here is your Graph!")
elif user_input == 'n':
    print("You chose not to see the Graph.")
else:
    print("Invalid input. Please type 'y' or 'n'.")
