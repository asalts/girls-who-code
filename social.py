class User:
    def __init__(self, username):
        self.username = username

    class Profile:
        def __init__(self, name, gender, bio):
                self.name = name
                self.age = 0
                self.gender = gender
                self.bio = bio

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.posts = []
        self.connections = []
        self.user_list = []

    def connect(self,friend):
        self.connections.append(friend)
    def post(self,posting):
        self.posts.append(posting)
    def add_friend(self,new_friend):
        self.user_list.append(new_friend)

def main():
    # Define the program flow for your user interface here.
        print("Enter a username to create a new user.")
        user = User(input("Enter a new username."))
        new_user = user.username
        print("Hello", new_user)
        # Need to addtest user to the list of users



# Runs your program.
if __name__ == '__main__':
    main()
