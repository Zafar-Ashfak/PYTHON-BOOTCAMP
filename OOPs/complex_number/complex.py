class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_complex(self):
        print(f"{self.real} + {self.img}i")

    # ****** Normal function ******
    # def add(self, num2):
    #     new_real = self.real + num2.real
    #     new_img = self.img + num2.img
    #     return Complex(new_real, new_img)

    # ******* Dunder function
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

def main():
    c1 = Complex(3, 5)
    c1.show_complex()

    c2 = Complex(4, 12)
    c2.show_complex()

    print("--------")
    # c3 = c1.add(c2)
    c3 = c1 + c2
    c3.show_complex()

main()