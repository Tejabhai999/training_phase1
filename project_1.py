#car showroom
class carshowroom:
    def __init__(self):
        print("Welcome Sir,we have three types of car companies:\n1.TOYOTA\n2.MAHINDRA\n3.MERCEDES")
        self.cgst="5%"
        self.cal_cgst=5/100
        self.sgst="12%"
        self.cal_sgst=12/100
        self.ins="50%"
        self.cal_ins=50/100
        print("Which type of company you want sir:")
        n=input("Enter the option:")
        self.n=n
        
    def tyt(self):
        if self.n!="1" and self.n!="TOYOTA" and self.n!="2" and self.n!="MAHINDRA" and self.n!="3" and self.n!="MERECEDES":
            print("Invalid option")
        if self.n=="1" or self.n=="TOYOTA":
            print("Models of TOYOTA:")
            print("1.Land Cruiser 250")
            print("2.Fortuner")
            self.inp=input("Enter the option:")
            if self.inp=="1" or self.inp=="Land Cruiser 250":
                print("Variant :Petrol")
                prs=10000000
                self.prs=prs
                print("Price :",prs)
            if self.inp=="2" or self.inp=="Fortuner":
                print("Variant :Diesel")
                prs=5000000
                self.prs=prs
                print("Price :",prs)
            if self.inp!="1" and self.inp!="Land Cruiser 250" and self.inp!="2" and self.inp!="Fortuner":
                print("Invalid option")
        
    def mah(self):
        if self.n=="2" or self.n=="MAHINDRA":
            print("Models of MAHINDRA:")
            print("1.XUV400")
            print("2.Scorpio")
            self.inp=input("Enter the option:")
            if self.inp=="1" or self.inp=="XUV400":
                print("Variant :Electric")
                prs=1800000
                self.prs=prs
                print("Price :",prs)
            if self.inp=="2" or self.inp=="Scorpio":
                print("Variant :Diesel")
                prs=1500000
                self.prs=prs
                print("Price :",prs)
            if self.inp!="1" and self.inp!="XUV400" and self.inp!="2" and self.inp!="Scorpio":
                print("Invalid option")
                
    def mer(self):
        if self.n=="3" or self.n=="MERCEDES":
            print("Models of MERCEDES:")
            print("1.Benz GLA")
            print("2.Benz EQS")
            self.inp=input("Enter the option:")
            if self.inp=="1" or self.inp=="Benz GLA":
                print("Variant :diesel")
                prs=4900000
                self.prs=prs
                print("Price :",prs)
            if self.inp=="2" or self.inp=="Benz EQS":
                print("Variant :Electric")
                prs=500000
                self.prs=prs
                print("Price :",prs)
            if self.inp!="1" and self.inp!="Benz GLA" and self.inp!="2" and self.inp!="Benz EQS":
                print("Invalid option")
                
    def display(self):
        
        if self.n=="1" or self.n=="TOYOTA" or self.n=="2" or self.n=="MAHINDRA" or self.n=="3" or self.n=="MERECEDES":
            if self.inp=="1" or self.inp=="2" or self.inp=="Land Cruiser 250" or self.inp=="Fortuner" or self.inp=="XUV400" or self.inp=="Scorpio" or self.inp=="Benz GLA" or self.inp=="Benz EQS":
                print("Sir,I hope u like this model")
                print("Do you want to know final price of this model(yes/no):")
                d=input()
                if d=="yes":
                    print("SHOWROOM_PRICE :",self.prs)
                    print("CGST :",self.cgst)
                    print("SGST :",self.sgst)
                    print("INSURANCE :",self.ins)
                    k=self.prs+self.cal_cgst+self.cal_sgst+self.cal_ins
                    print("Final price :",k)
                else:
                    print("Thank U For Visiting Our Showroom")
            
       
teja=carshowroom()
teja.tyt()
teja.mah()
teja.mer()
teja.display()
    
