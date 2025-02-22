import pandas as pd
import matplotlib.pyplot as plt
import menu1 as m

choice=m.main_menu()
aa=pd.read_csv("C:\\Users\\Akansha\\OneDrive\\Desktop\\Yash\\MobileGames.csv")
while True:
    if choice=="v":
        print("Enter your choice to view the types of chart:")
        print("1.Bar chart")
        print("2.Line chart")
        print("3.Horizontal bar chart")
        print("4.Histogram")
        print("5.Go back to main menu.")
        c=int(input("Enter your choice from above:"))
        if c==1:
            
            aa.plot(kind="bar",x='name',y='number_of_downloads(in millions)',width=1.0,edgecolor='r')
            plt.xlabel("Name of mobile games")
            plt.ylabel("No of downloads")
            plt.title("Popularity bar chart")
            plt.show()

        elif c==2:
            aa.plot()
            plt.xlabel("Rating(out of 5)")
            plt.ylabel("No of downloads(in millions)")
            plt.title("Popularity line chart")
            plt.show()

        elif c==3:
            aa.plot(kind="barh",x='name',y='number_of_downloads(in millions)',width=1.0,edgecolor='y')
            plt.xlabel("No of downloads")
            plt.ylabel("Name of games")
            plt.title("Popularity horizontal bar chart")
            plt.show()

        elif c==4:
            aa.plot(kind="hist",x='rating(out of five)',bins=15,width=1.0,edgecolor="red")
            plt.xlabel("rating(out of five)")
            plt.ylabel("frequency")
            plt.show()
        elif c==5:
            choice=m.main_menu()

        else:
            print("wrong choice")
            break

    elif choice=='r':
        print(aa)
        break
    elif choice=='dr':
        temp=pd.read_csv("C:\\Users\\Akansha\\OneDrive\\Desktop\\MobileGames.csv")
        nr=int(input("Enter index number of row to delete."))
        temp.drop([nr],inplace=True)
        print(temp)
        break
    elif choice=='dc':
        temp=pd.read_csv("C:\\Users\\Akansha\\OneDrive\\Desktop\\MobileGames.csv")
        temp.drop(["name","rating(out of five)"],axis=1,inplace=True)
        print(temp)
        break
    elif choice=='ac':
        aa['Type']=["Parkour","Parkour","Puzzle","Strategy","Strategy","Multiplier and battle royale"]
        print(aa)
        break
    elif choice=='vc':
        nc=input("Enter name of column to view:")
        print(aa[nc])
        break
    elif choice=='vr':
        nrow=int(input("Enter row number to view:"))
        print(aa.loc[nrow])
        break
    elif choice=='a':
        df=open("C:\\Users\\Akansha\\OneDrive\\Desktop\\MobileGames.csv",'a')
        df.write("Apex legends,4.3,14")
        df.close()
        print(aa)
        break
    else:
        break
    
