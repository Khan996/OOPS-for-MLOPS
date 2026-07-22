class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook. How would you like to proceed?
                            1. Press 1 to sign up
                            2. Press 2 to sign in
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any key to exit\n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            pass
        else:
            exit()
    def signup(self):
        email = input("Please enter your email/username: ")
        pwd = input("Please enter your password: ")
        print("You have successfully signed up! \n")
        self.username = email
        self.password = pwd
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please sign up first by entering your username and password \n")
        else:
            uname = input("Please enter your email/username: ")
            pwd = input("Please enter your password: ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!\n")
                self.loggedin = True
            else:
                print("Please input correct credentials. \n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here: \n")
            print(f"Following content has been posted succesfully: {txt}")
        else:
            print("Please sign in/sign up first to post status \n")
        self.menu()

   

user1 = chatbook()
