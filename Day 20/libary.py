library = ["Jod", "Zampya"]
try:
    while True:
        print(
            "--- WELCOME TO MY LIB --- \n 1 : Add books \n 2 : Show books \n 3 : Update books \n 4 : Remove books \n 5 : Exit "
        )
        choice = int(input("Enter choice : "))
        if choice == 1:
            B1 = int(input("Enter how many books your want to add : "))
            for i in range(B1):
                book = input(f"Enter {B1} book name : ")
                if book != "":
                    if book not in library:
                        library.append(book)
                        print("Book added successfully")
                    else:
                        print(f"{book} is already added pls try different ")
                else:
                    print("Enter value is Invalid")
        elif choice == 2:
            if len(library) > 0:
                for i in range(len(library)):
                    print(f"{i+1}) {library[i]}")
            else:
                print("Sorry currently libarary is Empty !")
        elif choice == 3:
            Bname = input("Enter Books name to update : ")
            if Bname != "":
                ind = None
                for i in range(len(library)):
                    if Bname == library[i]:
                        ind = i
                        pass
                if ind != None:
                    NewBook = input(f"Enter New title for {Bname} : ")
                    library[ind] = NewBook
                    print("Book rename successfully ! ")
                else:
                    print("Book not found in DataBase! ")
            else:
                print("Book name Invalid!")
        elif choice == 4:
            Rbook = input("Enter book title to remove : ")
            flag = False
            for i in range(len(library)):
                if library[i] == Rbook:
                    print('Book Found')
                    flag = True
                    library.pop(i)
        elif choice == 5:
            print("Thank you forusing our services")
            break
        else:
            print("Enter Invalid Value -- Try agian --")
except:
    print("Wrong Input")
