class Users:
    # Define the fields and methods for your object here.
    def __init__(self, username):
        self.username = username
        self.users = []
        self.posts = []
        self.connections = []

    def connect(self,username):
        self.users.append(username)
    def posting(self,post):
        self.connections.append(post)

class Profile:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = 0
        self.gender = gender
#       self.bio = bio
        self.profile_list = []

    def profile_add(self, profile_info):
            self.profile_list.append(profile_info)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self,name):
        self.users = []
        self.connections = connections
        self.posts = []
#'view profile option', enter in a username to see it
#    def

def user_setup():
    #Intro: Adds a user to the list
    user = Users(input("Welcome to the network! Enter a username to create a new user."))
    new_user = user.username
    print("Hello", new_user)
    #Adds user to the list of users
    user.connect(new_user)

def profile_setup():
    print("Let's set up your profile.")
    profile = Profile(input("What's your name?"))
    new_profile = profile.name
    #appends profile name to profile_info
    profile.profile_add(new_profile)

    profile = Profile(input("How old are you?"))
    new_age = profile.age
    #appends profile age to profile_info
    profile.profile_add(new_profile)

    profile = Profile(input("What's your gender?"))
    new_gender = profile.gender
    #appends profile gender to profile_info
    profile.profile_add(new_profile)

def main():
    # Define the program flow for your user interface here.
    user_setup()

#    print("Here's everyone on the network:")
#    for everyone in range(len(Users.users)):
#        print (everyone)

    user_input = input("Would you like to add another profile? (y or n)")
    if user_input == "y":
        main()
    elif user_input == "n":
        profile_setup()
    else:
        print("Please enter 'y' or 'n'.")

    print("Here's what you look like.")
    print (profile_list[0])
    print (profile_list[1])
    print (profile_list[2])





#    if user_input == "n"


# Runs your program.
#if __name__ == '__main__':
main()
