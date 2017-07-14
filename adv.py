start = '''
One day, you come across an avocado
...
'''
A = '''
Your skin begins to tingle... are these goosebumps? NO! You have avocado skin! Do you want to go to your local witch or the local hospital?
'''
B = '''
Your eyes begin to water... what have you done?? Suddenly, everything darkens... You have avocado skin for eyes!!! oh no! You have a important meeting today that determines your future in the company. Should you stay home with your avocado eyes or go outside and face ultimate embarrassment?
'''
C = '''
The witch will give you magical soap that can cure your avocado skin... but theres a catch... SHE WANTS YOUR SOUL! Make the exchange?
'''
D = '''
The doctors start prying at your avocado skin... it didn't work. The lead surgeon reccomends a brain transplant... replacing your brain with an avocado. Will you risk it all?
'''
E = '''
You've decided to stay home. Now you are doomed because you are never going to get cured... that sucks.
'''
F = '''
You've decided to go outside. Your eyes start to feel better... Surprise! You are healed and the Ceo promotes you for your consistent dedication to the company.
'''
G = '''
Congrats! You are back to normal but you will never be the same...
'''
H = '''
Life sucks! You are not cured... but at least you have a soul...
'''
I = '''
You have avocado skin forever now...
'''
J = '''
The sun heals your avocado skin. huh. strange ...
'''
K = '''
THE END
'''

print(start)

# 1
user_input = input("Take a bite out of it? Yes or no?")
if user_input == "yes":
    print(A) # finished the story by writing what happens

    # 2
    user_input = input("Please type 'witch' or 'hospital'")
    if user_input == "witch":
        print(C)
        # 4
        user_input = input("Please type 'yes' or 'no'")
        if user_input == "yes":
            print(G) # finished the story by writing what happens
            print (K)
        elif user_input == "no":
            print(H) # finished the story writing what happens
            print (K)
        else:
            print("Please type 'yes' or 'no'")
    elif user_input == "hospital":
        print (D)
        # 5
        user_input = input("Please type 'yes' or 'no'.")
        if user_input == "yes":
            print(J) # finished the story by writing what happens
            print (K)

        elif user_input == "no":
            print(I) # finished the story writing what happens
            print (K)
        else:
            print("Please type 'yes' or 'no'.")

    else:
        print:("Please type 'witch' or 'hospital'")

elif user_input == "no":
    print(B) # finished the story writing what happens

    # 3
    user_input = input("Please type 'stay at home' or 'go outside'.")
    if user_input == "stay at home":
        print(E) # finished the story by writing what happens
        print (K)

    elif user_input == "go outside":
        print(F) # finished the story writing what happens
        print (K)

    else:
        print("Please type 'stay at home' or 'go outside'")

else:
    print("Please type 'yes' or 'no'")
