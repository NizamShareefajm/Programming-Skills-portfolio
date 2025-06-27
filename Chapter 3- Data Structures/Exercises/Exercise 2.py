# List of names
names = ['Ronnie', 'Tyler', 'Dani']

# Personalized messages
msg = f"Hello, {names[0].title()}! Hope you're having a great day!"
print(msg)

msg = f"Hello, {names[1].title()}! Hope you're having a great day!"
print(msg)

msg = f"Hello, {names[2].title()}! Hope you're having a great day!"
print(msg)
# Using a loop to print personalized messages
for name in names:
    msg = f"Hello, {name.title()}! Hope you're having a great day!"
    print(msg)