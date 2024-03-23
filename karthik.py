class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
            print("Toyota,Mercedes")
            self.n=input("enter car company")
            if self.n=="Toyota":
                print("welcome to Toyota")
                self.model()
                break
            elif self.n=="Mercedes":
                print("welcome to Mercedes")
                self.model()
                break
            else:
                print("enter valid company")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("select from Fortuner and LL")
                self.choice=input("enter the car")
                if self.choice=="Fortuner":
                    self.print(self.choice)
                    break
                elif self.choice=="LL":
                    self.print(self.choice)
                    break
                else:
                    print("enter valid")
        elif self.n==("Mercedes"):
            while True:
                print("select from avg and gw")
                self.choice=input("enter the car")
                if self.choice=="avg":
                   self.price(self.choice)
                   break
                else:
                    print("enter valid")
    def print(self,choice):
        if choice=="Fortuner":
            self.p=4300000
        elif choice=="LL":
            self.p=324325252
        elif choice=="avg":
            self.p=2400000
        elif choice=="gw":
            self.p=328762872
        tot_p=self.p+self.sgst+self.cgst+self.insurance
        print(tot_p)
c=car()
c.company()

                
        
