import csv
import statistics
import random

# This function calculates and returns the average speed of all Digimons in the digimon.csv file
def avg_spd():
    with open('digimon.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader) # skip header line

        speeds = []
        for digimon in csv_reader:
            speeds.append(float(digimon['Spd']))
        
        return(round(statistics.fmean(speeds))) 

# This function counts and returns the number of Digimons in the digimon.csv file
# that have the specified attribute in the specified category

def count_digimon(category, attribute):
    with open('digimon.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader)

        count = 0
        for digimon in csv_reader:
            if digimon[category] != attribute:
                continue
            
            count += 1
        
        return(count)

# This function returns a list containing the names of up to three Digimons from the digimon.csv file
# that have a collective memory less than 15 and collective attack greater than 300
def find_team():
    with open('digimon.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        next(csv_reader)

        team = []
        
        for digimon in csv_reader:
            if int(digimon['Memory']) > 5: #if Digimon has more than 5 memory move to the next digimon
                continue
            if int(digimon["Atk"]) < 100: #if the digimon has less than 100 attack move to the next digimon
                continue
            if len(team) == 3: #if there are already 3 digimons in the team break out of the for loop
                break

            #if all conditions are met add the digimon's name to the team 
            team.append(digimon["Digimon"]) 
            

        return(team)

print(find_team())


    