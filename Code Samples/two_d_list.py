medal_table = [
    ["United States",16,5,5],
    ["Kenya",7,2,2],
    ["Canada",3,1,1],
    ["Netherlands",2,2,2],
    ["Botswana",2,2,2]
]

#print(medal_table)

medal_table.append(["Spain",2,0,1])

#print one row
print(medal_table[5])

# print one entry
print(medal_table[1][0])


"""
total = medal_table[0][1]+medal_table[0][2] + medal_table[0][3]
medal_table[0].append(total)
"""

for i in range(0,len(medal_table)):
    total = medal_table[i][1] + medal_table[i][2] + medal_table[i][3]
    medal_table[i].append(total)
    print(medal_table[i])



