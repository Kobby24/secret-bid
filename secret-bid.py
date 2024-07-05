from Day_nine import clear
print("Welcome to a secret bid")
more_players = True
diction = {}
all_entry = []
while more_players:
    name = input("Enter your name\n")
    bid = int(input("How much do you want to bid\n $"))
    to_continue = input("Are there more players 'yes' or 'no'").lower()


    def bider(name, bid,to_continue):
        
        all_entry.append(bid)
        diction[name] = bid
        
    if to_continue == "yes":
        clear()
        more_players = True
    else:
        more_players = False
    bider(name,bid,to_continue)

sas = max(all_entry)
winner = {i for i in diction if diction[i] == sas}

print(f"The winner is " + str(*winner) + f" with a bid of ${sas}")


