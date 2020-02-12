class fareh():
    """docstring for ClassName"""
    def __init__(self,res='',s=0,r=0,t=0,a=1800,name='',address='',checkin='',checkout='',roomno=101):
	    self.res = res
	    self.r=r
	    self.t=t
	    self.s=s
	    self.a=a
	    self.name=name
	    self.address=address
	    self.checkin=checkin
	    self.checkout=checkout
	    self.roomno=roomno
    def datain(self):
            self.name=input("\nEnter your name:")
            self.address=input("\nEnter your address:")
            self.checkin=input("\nEnter your check in date:")
            self.checkout=input("\nEnter your checkout date:")
            print("Your room no.:",self.rno,"\n")
    def room(self):
        print ("Type of Room")

        print ("1.  General       ---->Rs 1000 PN\-")

        print ("2.  Non-AC        ---->rs 2000 PN\-")

        print ("3.  AC-Room       ---->rs 4000 PN\-")

        print ("4.  Deluxe        ---->rs 5000 PN\-")

        print ("5.  Luxury Lounge ---->rs 7000 PN\-")

        x=int(input("Enter The Choice"))

        n=int(input("Number of Night stay"))

        if(x==1):

            print ("you have opted General Room")

            self.s=1000*n

        elif (x==2):

            print ("you have opted Non-AC Room")

            self.s=2000*n

        elif (x==3):

            print ("you have opted AC-Room")

            self.s=4000*n

        elif (x==4):
            print ("you have opted Deluxe Room")

            self.s=5000*n
        elif (x==5):
            print ("you have opted Luxury Lounge Room")

            self.s=7000*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.s,"\n")
    def restbill(self):
        print("****MENU****")
        print("1. Water-----> Rs25", "2. Tea-----> Rs10", "3. Breakfast Combo-----> Rs60", "4. Lunch -----> Rs110", "5. Dinner----->100", "6. Exit")
        while (1):
            c=int(input("Enter the choice :"))
            if(c==1):
                d=int(input("Enter the Quantity:"))
                self.r=self.r+20*d
            elif(c==2):
                d=int(input("Enter the Quantity:"))
                self.r=self.r+10*d
            elif(c==3):
                d=int(input("Enter the Quantity:"))
                self.r=self.r+90*d
            elif(c==4):
                d=int(input("Enter the Quantity:"))
                self.r=self.r+110*d
            elif(c==5):
                d=int(input("Enter the Quantity:"))
                self.r=self.r+150*d
            elif(c==6):
                break;
            else:
                print("Invalid option")
            print("Total Food",self.r,"\n")
    def	laundrybill(self):
         print(" Laundry ")
         print("1. Shorts----->Rs3", "2. Trousers-----> Rs4", "3. Shirt-----> Rs5", "4. Suit----->Rs8", "5. Exit")
         while (1):

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")
            print("Total Laundry Cost",self.t,"\n")

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.checkin)
        print ("Check out date",self.checkout)
        print ("Room no.",self.roomno)
        print ("Room Rent:",self.s)
        print ("Food Bill:",self.r)
        print ("Laundary Bill:",self.t)

        self.res=self.s+self.t+self.p+self.r

        print ("Bill Amount:",self.res)
        print ("Service charge",self.a)
        print ("Grand Total:",self.res+self.a,"\n")
        self.roomno+=1
def main():
    a=fareh()
    while(1):   
        print("1. Enter Customer Data")
        print("2. Calculate Rent")
        print("3. Restaurant Bill")
        print("4. Laundry bill")
        print("5. Total Rent")
        print("6. EXIT")

        b=int(input("\n Enter the choice"))
        if(b==1):
            
            a.datain()
        if(b==2):
            a.room()
        if(b==3):
            a.restbill()
        if(b==4):
            a.laundrybill() 
        if(b==5):
            a.display()
                
        if(b==6):
            quit()

main()
         


