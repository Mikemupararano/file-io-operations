def read(filename):
    """
    Reads data from the provided text file and prints it out in two sections: "Name" and "Birthdate".

    Args:
        filename (str): The name of the text file.
    """
    try:
        with open(filename, 'r') as file:
            Names = []  # List to store names
            Birthdates = []  # List to store birthdates

            # Iterate over each line in the file
            for line in file:
                Line = line.strip().split()  # Split the line into words
                Names.append(Line[0] + " " + Line[1])  # Add the name to the Names list
                Birthdates.append(' '.join(Line[2:]))  # Add the birthdate to the Birthdates list

            # Print the Names section
            print("Name")
            for name in Names:  
                print(name)

            # Print the Birthdate section
            print("\nBirthdate")
            for birthdate in Birthdates:
                print(birthdate)
    except FileNotFoundError:
        print("File not found.")

# Call the function
read('DOB.txt')
