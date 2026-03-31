# March 30 coding - showing how split and join work

#take a string and split it into component parts
college = "University of Maryland Howard County"

#first, split the string into components
new_school = college.split()
print(new_school)

#you can split on some other character
"""
weird_example = college.split("o")
print(weird_example)
"""

new_school[3] = "Baltimore"
print(new_school)

# combine elements of a list into a single string using join
# the elements will be divided in the string by whatever you put in the parenthese
our_college = (" ").join(new_school)
print(our_college)

n_school = ("").join(new_school)
print(n_school)

c_school = (",").join(new_school)
print(c_school)

# how do you know if a value is in the list
#49 ofthe 50 US states
# I left out Maryland - that was intentional
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii","Idaho", "Indiana", "Illinois", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
"Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]

#how do I know which state is missing?
# I can guess
if not "Maryland" in states:
    states.append("Maryland")
    states.sort()
    print(states)
