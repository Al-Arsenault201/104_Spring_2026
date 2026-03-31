# 49 states

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii","Idaho", "Indiana", "Illinois", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
"Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]
states.insert(19, "Maryland")

print(states)

# print out the name of every state that ends in a vowel
# assume that vowels are a, e, i, o, u, and y

vowels = ['a', 'e','i','o','u','y']

for statename in states:
    if statename[-1] in vowels:
        print(statename)

