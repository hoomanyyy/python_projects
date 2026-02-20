class library:
    def __init__(self):
        self.show_book = []

    def add_book(self, name_book):
        if name_book not in self.show_book:
            self.show_book.append(name_book)
        else:
            print("i hade this sentens in my dirctory")

    def saerch(self, name_book):
        if name_book in self.show_book:
            print(name_book)
        else:
            print(f"your saerch by {name_book} is rong plaese chek again")

    def delete_book(self, name_book):
        if name_book in self.show_book:
            self.show_book.remove(name_book)
        else:
            print(f"i didnt have {name_book} and in my memory")


if __name__ == "__main__":
    nothing = library()
    name = input("PLEASE ENTER YOUR NAME ...  ")
    while True:
        print("welcome to the hooman library")
        print("menu :")
        print(f"/ 1_ add one books {name} ...  ")
        print(f"/ 2_ show the books {name} ...  ")
        print(f"/ 3_ delete one books {name} ...  ")
        print(f"/ 4_ search by one books {name} ...  ")
        print(f"/ exit")

        ask = input(f"chose one subject in my library {name}")
        ask = int(ask)

        if ask == 1:
            javab = input(
                f"{name} wich book you want add in my library and in (,) rigit that nevisande ?  "
            )
            nothing.add_book(javab)
        elif ask == 2:
            print(nothing.show_book)
        elif ask == 3:
            ja = input("wich {name} , book you want delete ?  ")
            nothing.delete_book(ja)
        elif ask == 4:
            jaa = input("wich book {name} , you want search ?  ")
            nothing.saerch(jaa)
