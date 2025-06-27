# Invite some people to dinner
guests = ['Guido van Rossum', 'Jack Turner', 'Lynn Hill']

# Initial invitations
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, hi sir, please come sit with us and have dinner.")

name = guests[2].title()
print(f"{name}, please come and eat with us.")

# Jack can't make it
print(f"\nSorry, {guests[1].title()} can't make it to dinner.")

# Replace Jack with Gary
del guests[1]
guests.insert(1, 'Gary Snyder')

# New set of invitations
print("\nUpdated Invitations:")
name = guests[0].title()
print(f"{name}, you're still invited to dinner.")

name = guests[1].title()
print(f"{name}, please come to the party dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
