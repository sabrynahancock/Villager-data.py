"""Functions to parse a file containing villager data."""

#name|species|personality|hobby|motto

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set() #creates an empty set named species
    data = open(filename) #opening the file

    for line in data: #checking every line in the file 
        tokens = line.split("|") #splitting every item after | into tokens
        species.add(tokens[1]) #adding token at index 1 to the set
    #species = list(species) #turning set into list
    #print(type(species))#checks what datatype it is. if its list or sets, etc

    return sorted(species, reverse=True) #sorting into alphabetical order
    #reverse = True
    #and reversing it backwards

#print(all_species("villagers.csv")) #its a string because its only the file name

def get_villagers_by_species(filename, species_string="All"): #second argument
    #is optional and set by default "All"
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

#name|species|personality|hobby|motto

    villagers = [] #creates an empty list

    for line in open(filename): #loops through every line in file
        tokens = line.split("|") #splitting every item after | into tokens

        if species_string == "All": #checking if no argument is given
            villagers.append(tokens[0]) 

        elif species_string == tokens[1]:
            villagers.append(tokens[0])


    return villagers
#print(get_villagers_by_species("villagers.csv"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = [] #empty lists of every hobby
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    
#name|species|personality|hobby|motto

    for line in open(filename):
        tokens = line.split("|")
        hobby = tokens[3] #this token is being saved in variable hobby
        name = tokens[0] #this token is being saved in variable name
        
        if hobby == "Fitness":
            fitness.append(name)
            fitness.sort()

        elif hobby == "Nature":
            nature.append(name)
            nature.sort()

        elif hobby == "Education":
            education.append(name)
            education.sort()
            
        elif hobby == "Music":
            music.append(name)
            music.sort()

        elif hobby == "Fashion":
            fashion.append(name)
            fashion.sort()

        elif hobby == "Play":
            play.append(name)
            play.sort()
            
        big_list =[fitness, nature, education, music, fashion, play]
    #print(type(big_list))
    return big_list

print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
