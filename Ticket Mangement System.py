class Ticket:
    def __init__(self):
        self.ticket_queue = []
        self.available = {"VIP" : [10000, 10], "General" : [2500, 500], "Student" : [800, 100]}
    
    def request(self,t,q):
        temp = (self.t,self.available[self.t][0],self.q)
        self.ticket_queue.append(temp) 
        self.available[self.t][1] -= self.q
        # print(ticket_queue)
        print("Your ticket requests")
        for x in self.ticket_queue:
            print(x)

    def process(self):
        if len(self.ticket_queue) == 0:
            print("Please request a ticekt first")
            return 

        name = input("Enter your name : ")
        for x in range(len(self.ticket_queue)):
            for i in self.ticket_queue:
                print(f"{i[2]} {i[0]} tickets are allocated to {name} ")
                self.ticket_queue.pop(0)
        return

    def display(self):
        print()
        for i in self.available:
            print(f"Type - {i} | Price - {self.available[i][0]}  | Quantity - {self.available[i][1]}\n")

    def inp(self):
        while True:
            inp = input("\nPress\n1 to Request ticket\n2 to final\n3 to display available tickets\n0 to exit the system\n: ")

            if inp == '1':
                if len(self.ticket_queue) >= 5:
                    print("Please confirm your pending tickets first")
                    continue
            
                self.t = input("Enter the type of ticket ")
        
                if self.t not in self.available:
                    print("Please enter valid ticket type") 
                
                else:
                    try:
                        self.q = int(input("Enter the quantity of total tickets : "))
                        if self.q > self.available[self.t][1]:
                            print("Insufficient tickets requested!!")
                        else:
                            self.request(self.t,self.q)
                    except:
                        print("Invalid input type")
            
            
            elif inp == '2':
                self.process()

            elif inp == '3':
                self.display()
            
            elif inp == '0':
                print("System terminated!")
                break
        
            else:
                print("Invalid input!!")
obj = Ticket()
obj.display()
obj.inp()