
def clean_up_names(l):
   for i in range(len(l)):
       l[i] = l[i].replace('"', '')
	# you can also do this with l[i].strip(‘“‘)
   return l

def get_file(fname):

       useless_data = infile.readline()
       useless_data = infile.readline()
       data = infile.readlines()
       for i in range(len(data)):
           data[i] = data[i].split(",")
           data[i] = clean_up_names(data[i])
       return(data)

if __name__ == "__main__":

    with open ("Fall_2025.csv", "r") as infile:
        f25 = get_file(infile)
        print ("Fall 2025: ", f25[1],f25[-1])
    with open ("Fall_2026.csv", "r") as infile:
        f26 = get_file(infile)
        print ("Fall 2026: ", f26[1],f26[-1])
    with open ("Spring_2026.csv", "r") as infile:
        s26 = get_file(infile)
        print ("Spring 2026: ", s26[1],s26[-1])

