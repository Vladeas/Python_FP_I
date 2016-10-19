'''
Created on Oct 15, 2016

@author: Vlad


'''

'''
The following function initializes the dictionary list                                        <<<Initialize the list>>>
of apartments with some data, for easy testing
'''
def initialize(apartment_list):
    apartment_list.append({"apartment_number":1,"service_type":'gas',"amount":100})
    apartment_list.append({"apartment_number":2,"service_type":'water',"amount":200})
    apartment_list.append({"apartment_number":3,"service_type":'gas',"amount":400})
    apartment_list.append({"apartment_number":4,"service_type":'gas',"amount":500})
    apartment_list.append({"apartment_number":5,"service_type":'heat',"amount":600})
    apartment_list.append({"apartment_number":5,"service_type":'water',"amount":250})
    apartment_list.append({"apartment_number":2,"service_type":'heat',"amount":250})
    apartment_list.append({"apartment_number":6,"service_type":'gas',"amount":390})
    apartment_list.append({"apartment_number":7,"service_type":'water',"amount":50})
    apartment_list.append({"apartment_number":8,"service_type":'gas',"amount":70})
    
    
    
'''
The following function lists on the screen                                                    <<<Print list of commands>>>
all the implemented commands  
'''
def help_command(a):
    print("X - apartment number, Y - apartment number, SERV - service type, A - expenses")
    print("add X SERV A")
    print("remove X")
    print("remove X to Y")
    print("remove SERV")
    print("replace X SERV with A")
    print("list")
    print("exit")
    

#####################################################################<<<Secondary Functions>>>###########################################################################


'''
The following function returns the apartment_number from the dictionary,                    <<<Return apartment number>>>
for a specific position in the list(apartment_list) of dictionaries(apartment)
'''
def get_apartment_number(apartment):
    return apartment["apartment_number"] 



'''
The following function returns the apartment_number from the dictionary,                    <<<Return apartment service type>>>
for a specific position in the list(apartment_list) of dictionaries(apartment)
'''
def get_apartment_service(apartment):
    return apartment["service_type"] 



'''
The following function checks if the given                                                    <<<Number check>>>
string is a number or not
'''
def number_check(unknown):
    try:
        int(unknown)
        return True     #If the value can be converted into an integer then return True
    except ValueError:
        return False    #If there is an error than the string can not be converted, return False
    



#####################################################################<<<Command Functions>>>###########################################################################


'''                                                                                       
The following function adds the new entry to a list of dictionary's,                         <<<Add an entry to the list>>>
 containing Apartment_number, service_type and amount
'''
def add_apartment_expense(apartment_list, apartment_number, service_type, amount):
    apartment = {"apartment_number":int(apartment_number),"service_type":service_type,"amount":int(amount)}       #A dictionary is created with the previous fields
    apartment_list.append(apartment)        #The new entry(dictionary) is added to the list of dictionaries



'''
The following function runs through the list of apartments and reselects                    <<<Remove selected apartment>>>
just the ones that are not equal to the one inserted by the user
'''
def remove_apartment(apartment_list,apartment_number):
    apartment_list[:] = [apt for apt in apartment_list if get_apartment_number(apt) != int(apartment_number)]



'''
The following function runs through the list of services and reselects                    <<<Remove selected service>>>
just the ones that are not equal to the one inserted by the user
'''
def remove_service_type(apartment_list,apartment_service_type):
    apartment_list[:] = [serv for serv in apartment_list if get_apartment_service(serv) != apartment_service_type]



'''
The following function runs through the list of apartments and reselects                    <<<Remove apartments from interval>>>
just the ones that are outside the given interval
'''
def remove_apartments_between(apartment_list,lower_bound,upper_bound):
    apartment_list[:] = [apt for apt in apartment_list if get_apartment_number(apt) > int(upper_bound) or get_apartment_number(apt) < int(lower_bound)]



'''
The following function replaces the expense of a certain                                     <<<Replace apartment expense>>>
apartment for a service with a new, user introduced one
'''
def replace_amount(apartment_list, apartment_number, service_type, noth, new_amount):
    for apartment in apartment_list:        #Run through all dictionaries in the list
        if get_apartment_number(apartment) == int(apartment_number) and get_apartment_service(apartment) == service_type:   #If the apt. number and service type coincide:
            apartment["amount"]=int(new_amount)     #Replace old expense with a the new one




'''
The following function displays each entry                                                  <<<Print the list of apartments>>>
'''
def print_apartment_list(apartment_list):
    if len(apartment_list) == 0:        #The instruction checks if there is any element in the list between 
        print("No apartment registered")        #If not a message is displayed
        
    for apartment in apartment_list:      #For each apartment "apt" from the apartment_list, all stored information are printed
        print(">>>apartment number = {0}, service type = {1}, amount = {2}".format(apartment["apartment_number"], apartment["service_type"], apartment["amount"]))
            #"{0},{1} and {2}" are : apartment["apartment_number"], apartment["service_type"] and apartment["amount"]




##################################################################################<<<Intermediary>>>####################################################################


'''
The following function finds out which remove function                                    <<<Remove options>>>
was called
'''
def remove_options(apartment_list,*arguments):
    if len(arguments) != 1:         #If there are multiple elements in "arguments" then the remove function is "remove x to y"
        remove_apartments_between(apartment_list,arguments[0],arguments[2])
    elif number_check(arguments[0]) == True:        #If the string can be converted to integer than remove apartment
        remove_apartment(apartment_list, int(arguments[0]))
    else: remove_service_type(apartment_list, arguments[0])     #If the string can not be converted to integer than remove service type



##########################################################################<<<Command Interpretation Functions>>>##########################################################







'''
The following function returns the command in two pieces:                                    <<<Input the command>>>
    -The first word, which defines the command
    -And the rest of the words put in a list
'''
def read_command():
    command = input("<<< ")
    position = command.find(" ")    #Returns the position of the first space " " if it exists otherwise returns -1
    
    if position == -1:      #If True the command is formed from only one word (no spaces)
        return command,""       #Returns the word and nothing else in the place of the other arguments
    
    cmd = command[:position]        #"cmd" takes the first part of the string "Primary command", up to the position of the space " "
    arguments = command[position:]      #"arguments" takes the last part of the string, from the position of the space " " to the end of the string "Arguments list"
    arguments = arguments.split()       #The last part is divided and the words are put in a list
    
    return cmd, arguments       #return "Primary command" and "Arguments list"
    


'''
The following function interprets the command and calls each function accordingly            <<<Interpret the command & Run the program>>>
'''
def execute_command():
        apartment_list = []
        
        initialize(apartment_list)
        
        commands = {"add":add_apartment_expense, "list":print_apartment_list, "remove":remove_options, "replace":replace_amount, "help":help_command}
                #The previous command creates a dictionary of functions
        
        while True:
            cmd, arguments = read_command()     #"cmd & arguments" receive the transformed command from the "read_command()" function
            
            if cmd == 'exit':       #If the command is "exit" the function stops
                break
            
            try:        #"try# repeats an instruction, if there is an Error, until the command is correct
                commands[cmd](apartment_list,*arguments)
            except KeyError as ke:      #If the command does not exist, print the following message and repeat
                print("This command is not implemented.", ke)
            except Exception as ex:     #If there are too many arguments, print the following message and repeat
                print("An error occurred; try again. " , ex)
            

#####################################################################<<<Test>>>#################################################################################



def test_number_check():
    assert number_check('1234') == True
    assert number_check('animal') == False
    assert number_check('1s2f') == False



def test():
    test_number_check()

#####################################################################<<<Main>>>#################################################################################





'''
Main function                                                                                <<<Main>>>
'''
if __name__ == '__main__':
    print("Welcome")
    print("Use 'help' for more commands")
    test()
    execute_command()
    print("How dare you !!!")
    
    



