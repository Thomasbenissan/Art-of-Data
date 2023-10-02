import csv
import statistics

def find_largest_average(attribute):
    """
    This function calculates and prints the species with the largest average of the given attribute.
    The attirbute parameter is a string representing the attribute to be averaged (e.g. 'bill_length_mm', 'body_mass_g').
    """
    with open('penguins.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader)  # Skip the header row
        
        specie_attribute = {}
        
        # Looping through each row in the csv file
        for penguin in csv_reader:
            specie = penguin["species"]
            
            # Initializing the list for the species if its not in the final dictionary
            if specie not in specie_attribute:
                specie_attribute[specie] = []
            
            # Skipping the penguin if the attribute field is empty
            if penguin[attribute] == '':
                continue
            specie_attribute[specie].append(float(penguin[attribute]))
        
        largest_specie_avg = 0
        largest_specie = None
        
        # Calculating the average for each species and finding the species with the largest average attribute
        for specie, values in specie_attribute.items():
            avg_value = statistics.fmean(values)
            if avg_value > largest_specie_avg:
                largest_specie_avg = avg_value
                largest_specie = specie
        
    print(largest_specie)


def chinstrap_dreamIsland():
    """
    This function calculates and prints the total number of Chinstrap penguins on Dream island.
    """
    with open('penguins.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader)  # Skip the header row

        total = 0

        # Iterating over each row in the CSV file and counting the penguins that meet the criteria 
        for penguin in csv_reader:
            if penguin['species'] == "Chinstrap" and penguin['island'] == "Dream":
                total += 1
        print(total)


find_largest_average('bill_length_mm')  # To find the species with the largest average bill length
find_largest_average('body_mass_g')  # To find the most massive species on average
chinstrap_dreamIsland()


"""

Seperate 2 functions:



def find_longest_bills():

    with open('penguins.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader) 

        bill_length = {}
        

        for pengiun in csv_reader:
            specie = pengiun["species"]

            if specie not in bill_length:
                bill_length[specie] = []

            if pengiun['bill_length_mm'] == '': #if the field is empty skip this pengiun
                continue
            bill_length[specie].append(float(pengiun['bill_length_mm']))
        
        largest_specie_avg = [0, None]

        for _specie in bill_length:
            avg_length = statistics.fmean(bill_length[_specie]) #calculate the average of each list of bill lenghts
            bill_length[_specie] = avg_length
            if(avg_length > largest_specie_avg[0]):
                largest_specie_avg[0] = avg_length
                largest_specie_avg[1] = _specie

    print(largest_specie_avg[1])

def find_most_massive():

    with open('penguins.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader) 

        specie_mass = {}
        

        for pengiun in csv_reader:
            specie = pengiun["species"]

            if specie not in specie_mass:
                specie_mass[specie] = []

            if pengiun['body_mass_g'] == '': #if the field is empty skip this pengiun
                continue
            specie_mass[specie].append(float(pengiun['body_mass_g']))
        
        largest_specie_avg = [0, None]

        for _specie in specie_mass:
            avg_mass = statistics.fmean(specie_mass[_specie]) #calculate the average of each list of bill lenghts
            specie_mass[_specie] = avg_mass
            if(avg_mass > largest_specie_avg[0]):
                largest_specie_avg[0] = avg_mass
                largest_specie_avg[1] = _specie

    print(largest_specie_avg[1])


"""


             
    
    
        


