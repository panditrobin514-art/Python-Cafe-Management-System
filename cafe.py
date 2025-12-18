class pythoncafe:
    def __init__(self):
        print("\t\t\t\t\t\t\t Python Cafe")
        print("\t\t\t\t\t\t\t since-1991")
        print("\t\t\t\t\t\t\t www.pythoncafe.com")
        print("\t\t\t\t\t\t\t Wel-Come")
        print("Here is your menu")
        x=["Indian","Chines","Italian","Korean"]
        j=1
        for i in x:
            print(j,".",i)
            j=j+1
    def indian(self):
        a=["Rajma","Matar-Paneer","Paneer Tikka","Lassi","Green-salad","Mix-Veg"]
        b=[120,100,150,30,50,130]
        indian_={"Indian Food Items":a,"Price":b}
        print("\n")

        import pandas as  pd
        df=pd.DataFrame(indian_,index=[i for i in range(1,7)])
        print("\n\nIndian Food \n\n")
        print(df)
        l=[]
        e="yes"
        while e=="yes":
            a=int(input("\nEnter the position of the item= "))
            b=int(input("\nEnter the quantity= "))
            c=(df["Price"][a])*b
            l.append(c)
            e=input("\nDo you want to Re-Order (yes/no)= ")
            if e=="no":
                print("\nThank-You")
            elif e=="yes":
                pass
            else:
                print("Invalis Input \n")

        amount=sum(l)
        tax=amount*0.05
        total_amount=amount+tax

        from colorama import Fore,Back,Style
        print(Fore.YELLOW+Back.LIGHTBLACK_EX+Style.BRIGHT  +f"Total Amount {amount}")
        print("Total Tax ",tax)
        print("toal Amount ",total_amount)

    def chines(self):
        a=["Tofu and Mushroom Stir Fry","Veg Chow Mein","Veg Fried Rice","Crispy Bottom Pan-Fried Veg Buns","Lo-Mean Noodles","Spring Veg Stir Fry"]
        b=[200,180,160,210,150,130]
        chines_={"Chines Food Items":a,"Price":b}

        import pandas as pd
        df=pd.DataFrame(chines_,index=[i for i in range(1,7)])
        print("\n\nChines Food \n\n")
        print(df)
        l=[]
        e="yes"
        while e=="yes":
            a=int(input("\nEnter the position of the item= "))
            b=int(input("\nEnter the Quantity of the item= "))
            c=(df["Price"][a])*b
            l.append(c)
            e=input("Do you want to Re-Order (yes/no)= ")
            if e=="no":
                print("Thank-You")
            elif e=="yes":
                pass
            else:
                print("Invalid Input \n")
                
        amount=sum(l)
        tax=amount*0.05
        total_amount=amount+tax
        from colorama import Fore,Back,Style
        print(Fore.YELLOW+Back.LIGHTBLACK_EX+Style.BRIGHT  +f"Total Amount {amount}")
        print("Total Tax ",tax)
        print("toal Amount ",total_amount)

    def italian(self):
        a=["Cecilia Vecchi","Risotto","Pizza","Pasta","Gnochhi","Pesto alla Genovese"]
        b=[300,240,280,210,320,290]
        italian_={"Italian Food":a,"Price":b}

        import pandas as pd
        df=pd.DataFrame(italian_,index=[i for i in range(1,7)])
        print("\n\nItalian Food \n\n")
        print(df)
        l=[]
        e="yes"
        while e=="yes":
            a=int(input("\nEnter the position of the food= "))
            b=int(input("\nEnter the quantity of the food= "))
            c=(df["Price"][a])*b
            l.append(c)
            e=input("Do you want to Re-Order (yes/no)= ")
            if e=="no":
                print("Thank-You")
            elif e=="yes":
                pass
            else:
                print("Invalid input \n")

        amount=sum(l)
        tax=amount*0.05
        total_amount=amount+tax

        from colorama import Fore,Back,Style
        print(Fore.YELLOW+Back.LIGHTBLACK_EX+Style.BRIGHT  +f"Amount {amount}")
        print("Total Tax ",tax)
        print("toal Amount ",total_amount)

    def korean(Self):
        a=["bibimbap","kimchi fried rice","gimbap","Dongchimi","Sweet Potato latte","Korean Coleslaw"]
        b=[210,300,280,250,180,240]
        korean_={"Korean Food Item":a,"Price":b}

        import pandas as pd
        df=pd.DataFrame(korean_,index=[i for i in range(1,7)])
        print("\n\nKorean Food \n\n")
        print(df)
        l=[]
        e="yes"
        while e=="yes":
            a=int(input("\nEnter the position of food = "))
            b=int(input("Enter the quantitiy = "))
            c=(df["Price"][a])*b
            l.append(c)
            e=input("Do you want to Re-Order (yes/no)= ")
            if e=="no":
                print("Thank-You")
            elif e=="yes":
                pass
            else:
                print("Invalid Input")

        amount=sum(l)
        tax=amount*0.05
        total_amount=amount+tax

        from colorama import Fore,Back,Style
        print(Fore.YELLOW+Back.LIGHTBLACK_EX+Style.BRIGHT +f"Amount {amount}")
        print("Total Tax ",tax)
        print("Total Amount ",amount)

ob1=pythoncafe()

valid_choice = False

choice=input("\nEnter your food choice= ")
if choice=="indian":
    ob1.indian()
elif choice=="chines":
    ob1.chines()
elif choice=="italian":
    ob1.italian()
elif choice=="korean":
    ob1.korean()
else:
    print("Invalid Input")

valid_choice = True
       
payment=input("\nEnter payment mode (cash/online)= ")
if payment=="cash":
    print("\n Thank- You")
elif payment=="online":
    print("Please Scan QR-Code")
    import cv2 as cv
    img=cv.imread("D:\\qr.JPEG")
    cv.imshow("qr",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Invalid Payment Mode")

                