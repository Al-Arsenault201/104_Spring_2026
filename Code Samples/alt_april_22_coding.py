def clean_up_names(l):
   for i in range(len(l)):
       l[i] = l[i].replace('"', '')
	# you can also do this with l[i].strip(‘“‘)
   return l

def get_file(fname):
   with open(fname) as infile:
       useless_data = infile.readline()
       useless_data = infile.readline()
       data = infile.readlines()
       for i in range(len(data)):
           data[i] = data[i].split(",")
           data[i] = clean_up_names(data[i])
       return(data)

if __name__ == "__main__":
    filenames = ("Fall_2025.csv", "Fall_2026.csv", "Spring_2026.csv")
    list_of_files = []
    for filename in filenames:
        list_of_files.append(get_file(filename))
    print ("Fall 2025: ", list_of_files[0][0], list_of_files[0][-1] )
    print ("Fall 2026: ", list_of_files[1][0], list_of_files[1][-1] )
    print ("Spring 2026: ", list_of_files[2][0], list_of_files[2][-1] )


