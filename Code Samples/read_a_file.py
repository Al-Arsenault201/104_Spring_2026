# practice reading from a file

def create_dictionary(student_record):
    student_scores = {}
    student_scores["last_name"] = student_record[0]
    student_scores["first_name"] = student_record[1]
    student_scores["student_id"] = student_record[2]
    student_scores["p1"] = int(student_record[3])
    student_scores["p2"] = int(student_record[4])
    student_scores["p3"] = int(student_record[5])
    student_scores["t1"] = int(student_record[6])
    student_scores["t2"] = int(student_record[7])
    student_scores["p4"] = int(student_record[8])
    return student_scores

if __name__ == "__main__":
    filename = "/Users/alfredarsenault/Downloads/Fall_2025 (2).csv"


    """    data = infile.read()
    
        print(data)
        useful_data = data.split("\n")
        print(useful_data)
    """
    with open (filename,"r") as infile:
        # I want to get rid of the first two lines of the file
        # they don't contain useful data
        # I *could* still use readlines() and then pop the first two items from the list
        # but lets be cleaner
        #read the first header line and throw it away
        useless_data = infile.readline()   #reads one line of data
        #read the second header line and throw it away
        useless_data = infile.readline()


        list_data = infile.readlines()
        print(list_data)
        for i in range(3):
            print(list_data[i])

        for i in range(len(list_data)):
            list_data[i] = list_data[i].split(",")
            #print(list_data[i])
            #create a dictionary of this data
            list_data[i] = create_dictionary(list_data[i])
            print(list_data[i])
        #print(list_data)


    newfilename = "/Users/alfredarsenault/Downloads/8Apriloutfile.txt"
    with open(newfilename,"w") as outfile:
        outfile.write("This is the header row\n")
        outfile.write("\tNow we can add data\n")

        name_list = []
        for i in range(len(list_data)):
            name_list.append(list_data[i]["last_name"])

        #outfile.writelines(name_list)
        outfile.write("\n".join(name_list))
        








