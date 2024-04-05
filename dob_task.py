def read(filename):
    """
    Reads data from the provided text file and prints it out in two sections: "Name" and "Birthdate".

    Args:
        filename (str): The name of the text file.

    """
    try:
        with open(filename, 'r') as file:
            Names = []  # This is a list that will store all the names read from the DOB text file
            Birthdates = []  # This is a list that will store all the birthdates read from the DOB text file
            for line in file:
                Line = line.strip().split()  # strip any white spaces and split the line into pieces
                # each line is split into 5 pieces - the first two pieces will be the name and surname while the 3rd,4th and 5th pieces will be the Birthdate
                Names.append(Line[0] + " " + Line[1])  # Add the first 2 pieces into the Names list.
                Birthdates.append(' '.join(Line[2:]))  # Add the last 3 pieces into the Birthdates list.

            # Print Names
            print("Name")
            for name in Names:  
                print(name)

            # Print Birthdate
            print("\nBirthdate")
            for birthdate in Birthdates:
                print(birthdate)
    except FileNotFoundError:
        print("File not found.")

# Call the function
read('DOB.txt')
