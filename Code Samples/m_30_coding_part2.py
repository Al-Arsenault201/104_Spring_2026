# part 2 - coding from March 30, 2026

#numbers = [1,2,3,4,5]
#print(sum(numbers))

counties = ["Allegany", "Anne Arundel","Baltimore", "Baltimore City", "Calvert", "Carroll", "Caroline", "Cecil", "Charles", "Dorchester",
"Frederick", "Garrett", "Harford", "Howard", "Kent", "Montgomery", "Prince George's", "Queen Anne's", "Somerset", "St. Mary's",

"Talbot", "Washington", "Wicomico", "Worcester"]

#check to see if we got them all
print(len(counties))

#print out the counties that start with "C"
"""
for i in range(len(counties)):
    if counties[i][0] == "C":
        print(counties[i])
"""

# a new for loop
for county in counties:
    if county[0] == "C":
        print(county)


#49 ofthe 50 US states
# I left out Maryland - that was intentional
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii","Idaho", "Indiana", "Illinois", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
"Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]

#check to see how many we have
print(len(states))

states.append("Maryland")
#print(states)

states.sort()
print(states)

states.reverse()
print(states)
print(states.index("Maryland"))

states.reverse()  # put the states back in alphabetical order
print(states.index("Maryland"))
