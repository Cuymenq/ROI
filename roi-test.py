# functions
class ROI():
    def __init__(self):
        self.users = []
        self.curr_user = None 

    def create_property(self):
        pass

    def portfolio(self):        
        print(f'{self.curr_user}')
      

    def choose_property(self, curr_user):
        self.curr_user = curr_user
        
    def modify():
        pass

    def delete():
        pass

    def create_user(self, username, property_name, income_name, income_amount):

        if username not in self.users:
            new_user = User(username, property_name, income_name, income_amount)
            self.users.append(new_user)
        if self.curr_user == None:
            self.curr_user = new_user 
        
        
# From the users list we are pulling out the user at "idx" index.   
    def print_users(self):
        for idx in range(len(self.users)):            
            print(f'{idx} {self.users[idx].username}')

    def switch_user(self, user_idx):
        self.curr_user = self.users[int(user_idx)]

    # change the state of the object



class User():
    def __init__(self, username, property_name, income_name, income_amount):
        self.username = username
        self.properties = []
        self.incomes = {
            'income_name': "income name",
            'amount': "amount"
        }
        

class Property():
    def __init__(self, name):
        pass

class Incomes():
    pass


# run the program
class MainPage():
    def __init__(self):
        self.roi = ROI()

    def main(self):
        while True:
            if self.roi.curr_user != None:
                print(f"Welcome {self.roi.curr_user.username}")

            print(f"[1] Create Property - create a new property and see its ROI")
            print(f"[2] Portfolio")
            print(f"[3] Choose property - Switch current property")
            print(f"[4] Modify property")
            print(f"[5] Delete property")
            print(f"[6] Create User")
            print(f"[7] Switch Users")
            print(f"[0] Quit\n")

            query = input(f"Welcome What would you like to do? ")
            if query == "1":
                ROI.create_property()
            elif query == "2":
                return self.roi.portfolio()
            elif query == "3":
                ROI.choose_property()
            elif query == "4":
                ROI.modify()
            elif query == "5":
                ROI.delete()
            elif query == "6":
                user = input("Choose a Username: ").lower()
                property_name = input("Please enter a name for this propery: ")

                print('Please enter income information\n')
                income_name = input("Enter income name:  ")
                income_amount = int(input("Enter income amount: "))

                self.roi.create_user(user, property_name, income_name, income_amount)
            
            elif query == "7":
                self.roi.print_users()
                user_idx = input("switch  ")
                self.roi.switch_user(user_idx)
            elif query == "0":
                print("Have a nice day!")
                break

run = MainPage()
run.main()