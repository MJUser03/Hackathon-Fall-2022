#input = "3x+2y-32z=-2,7x-2y+5z=-14,2x+4y+z=6"
#expected out put = "Equations 3x+2y-32z=-2 and 7x-2y+5z=-14 work best because 2y cancels out -2y"
# or in gcf = "Equations 3x+4y-32z=-2 and 7x-2y+5z=-14 work best because 4y and -2y because you can multiply them to the same factor"

#check for malformed input

lst_of_variables = [] #gives us the variables being used in this program
#when we take in the input we want to have it so everything is lowercase to minimize malformed inputs
lst_of_best_equation = []

def error_input(input):
    error = 0
    num_of_comma = 0
    if input == '':
        error += 1
    for i in input:
        if i == ',':
            num_of_comma +=1
        if i == ' ':
            error +=1
    if num_of_comma != 2:
        error +=1
    #we will check the variables in a future function
    if error != 0:
        return 1
    else:
        return 0

 #puts equations into a list for easy use in turning it into a map

def input_to_lst(input):
    #a comma is added to the end as a terminator for our while loop
    input+=','
    empty_lst = []
    list_string = ""
    i=0
    #in this demo we are only allowing 3 equations
    for m in range(3):
        while input[i] != ',':
            list_string+=input[i]
            i += 1
        empty_lst.append(list_string)
        list_string = ""
        i += 1
    return empty_lst

#put equation properties into a map ex: {"equations":["3x+2y-32z=-2","7x-2y+5z=-14","2x+4y+z=6"], "x":[3,7,2], "y":[2,-2,4]}


def eq_to_map(input_lst):
    empty_map = {"Equation":[input_lst[0],input_lst[1],input_lst[2]]}
    variable = "" #use this for variables like x y z
    num = '' #use this for negative integers
    constant = 0; #use this for integers
    empty_lst = []
    for i in range(3):
        equation = input_lst[i]
        #when we reach = we want to skip to the next list element
        for j in equation:

            if j == '=':
                constant = 0
                break

            # check if the number is negative
            if j != '-':
                variable = j
            else: #if negative add the - into num
                num = j

            if variable.isdigit(): #we are at a constant
                if num != '': #num is negative
                    constant = -1 * int(variable)#set constant to the int
                    num = ''
                else:
                    if constant != 0:
                        if constant < 0: #negative
                            constant = (-1 * constant) * 10 + int(variable)
                            constant = -1 * constant
                        else:
                            constant = constant * 10 + int(variable)
                    else:
                        constant = int(variable)

            elif variable == '+' or num == '-':
            #basically we want to empty everything and do nothing
                constant = constant

            else:
                #we reach an x y z char
                #here we throw var:num into the map list
                if constant == 0:
                    constant = 1


                if variable in empty_map:

                    empty_map[variable].append(constant)
                    constant = 0
                else:
                    lst_of_variables.append(variable)
                    empty_lst.append(constant)
                    empty_map[variable] = empty_lst
                    constant = 0
                    empty_lst = []

    return empty_map

#here we check to make sure out map in not maleformed/the equations can be computated

def error_map(input_map):
    var_dif = 0;
    for i in lst_of_variables:
        if len(input_map[i])== 1:
            var_dif += 1

    if var_dif >= 2:
        return 1

    else:
        return 0


#finds if there are varibles in out list that cancels out, if so return a list of the two equations

def cancel_out(input_map):
    output = []
    for i in lst_of_variables:
        check_lst = input_map[i] #eg [3,7,2]
        index = 0
        prev_item = 0
        if len(output) != 0:
            break

        for j in check_lst:
            if prev_item == 0:
                prev_item = j
                index += 1
            else:
                if prev_item < 0 and j > 0: #if the previous item is negative and current item is postive..
                    if((-1*prev_item)==j):
                        output.append(prev_item)
                        output.append(j)

                        #put the two equations into a lst
                        lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                        lst_of_best_equation.append(input_map["Equation"][index])
                        break
                    index +=1
                elif prev_item > 0 and j < 0: #if the previous item is postive and current is negative...
                    if (prev_item == (-1*j)):
                        output.append(prev_item)
                        output.append(j)
                        lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                        lst_of_best_equation.append(input_map["Equation"][index])
                        #put the two equations into a lst
                        break
                    index += 1
                else:
                    prev_item = j
                    index +=1
    return output


#when there isn't variables that cancel out we check for a common factor
def Common_factor(input_map):
    output = []
    for i in lst_of_variables:
        check_lst = input_map[i]  # eg [3,7,2]
        index = 0

        prev_item = 0
        if len(output) != 0:
            break

        for j in check_lst:
            if prev_item == 0:
                prev_item = j
                index += 1

            elif prev_item > j or prev_item < 0:
                calc = prev_item % j
                if calc == 0:
                    output.append(prev_item)
                    output.append(j)
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                    lst_of_best_equation.append(input_map["Equation"][index]) #correct
                    break
                index +=1

            elif prev_item < j or j < 0:
                calc = j % prev_item
                if calc == 0:
                    output.append(j)
                    output.append(prev_item)
                    lst_of_best_equation.append(input_map["Equation"][index]) #correct
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                    break
                index +=1
            else:
                prev_item = j
                index += 1
    return output

#note here, if two vars are equal they count towards gcf since you have to multiply one by -1


