#input = "3x+2y-32z=-2,7x-2y+5z=-14,2x+4y+z=6"
#expected out put = "Equations 3x+2y-32z=-2 and 7x-2y+5z=-14 work best because 2y cancels out -2y"
# or in gcf = "Equations 3x+4y-32z=-2 and 7x-2y+5z=-14 work best because 4y and -2y because you can multiply them to the same factor"

#check for malformed input

lst_of_variables = [] #gives us the variables being used in this program
#when we take in the input we want to have it so everything is lowercase to minimize malformed inputs
lst_of_best_equation = []

def num_commas(input):
    num_of_comma = 0
    for i in input:
        if i == ',':
            num_of_comma +=1
    return num_of_comma
def remove_spaces(input):
    #just adding a making everything lower-case for just managability sake
    input.lower()
    new_input = ""
    for i in input:
        if i == " ":
            new_input += ""
        else:
            new_input += i
    return new_input
def get_variables(input):
    for i in input:
        if i.isdigit() is False and i != '+' and i != '-' and i != '=' and i != ',' and i not in lst_of_variables and i !='\n':
            lst_of_variables.append(i)

#This allows users to put multiple commas but still take in the input for use
def remove_extra_commas(input):
    new_input = ""
    fix_input = ""
    prev_char = ''

    for i in input:
        if prev_char == '':
            prev_char = i

        if prev_char == ',' and i == ',':
            new_input += ""
        else:
            prev_char = i
            new_input += i
    if new_input == "":
        return " "

    if new_input[-1] == ',':
        for i in range(len(new_input)-1):
            fix_input += new_input[i]

        new_input = fix_input

    return new_input

def error_input(input):
    error = 0
    num_of_comma = 0
    operators = 0
    if input == '':
        error += 1
    for i in input:
        if i == ',':
            num_of_comma +=1
        if i == ' ':
            error +=1
        if i == '-' or i == '+' or i == '=':
            operators += 1
    if num_of_comma == 0 or num_of_comma < 2 or operators == 0:
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
    for m in range(num_commas(input)):
        while input[i] != ',':
            list_string+=input[i]
            i += 1
        empty_lst.append(list_string)
        list_string = ""
        i += 1
    return empty_lst
#print(input_to_lst("4x+2y+31z=3,9x-3y+32z=5,10x+5y-11z=6,x+12y-5z=54"))

#put equation properties into a map ex: {"equations":["3x+2y-32z=-2","7x-2y+5z=-14","2x+4y+z=6"], "x":[3,7,2], "y":[2,-2,4]}


def eq_to_map(input_lst,Input):
    get_variables(Input)
    print(lst_of_variables)
    empty_map = {}
    eq_lst = []
    for i in input_lst:
        eq_lst.append(i)
        empty_map["Equation"] = eq_lst

    variable = "" #use this for variables like x y z
    num = '' #use this for negative integers
    neg = 1
    constant = 0 #use this for integers
    empty_lst = []
    for i in range(num_commas(Input)+1):
        equation = input_lst[i]
        #when we reach = we want to skip to the next list element
        for j in equation:
            if j == '=':
                num = ''
                constant = 0
                neg = 1
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
                neg += 1

            elif variable == '+':
            #basically we want to empty everything and do nothing
                neg += 1

            elif num == '-' and equation[neg].isdigit():
                neg += 1

            elif equation[neg] in lst_of_variables:
                neg += 1

            else:
                #we reach an x y z char
                #here we throw var:num into the map list

                if constant == 0:

                    if '-' + str(variable) in input_lst[i]:
                        constant = -1

                    else:
                        constant = 1

                if variable in empty_map:
                    empty_map[variable].append(constant)
                    constant = 0
                    neg += 1
                else:
                    empty_lst.append(constant)
                    empty_map[variable] = empty_lst
                    constant = 0
                    empty_lst = []
                    neg += 1

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
        if len(output) != 0:
            break

        for j in check_lst:
            if -1 * j in check_lst:
                print(check_lst)
                output.append(str(j)+i)
                output.append(str((-1)*j)+i)
                lst_of_best_equation.append(input_map["Equation"][check_lst.index((-1)*j)])
                lst_of_best_equation.append(input_map["Equation"][check_lst.index(j)])
                break
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
                    output.append(str(prev_item)+i)
                    output.append(str(j)+i)
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(j)]) #correct
                    break
                index +=1

            elif prev_item < j or j < 0:
                calc = j % prev_item
                if calc == 0:
                    output.append(str(j)+i)
                    output.append(str(prev_item)+i)
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(j)]) #correct
                    lst_of_best_equation.append(input_map["Equation"][check_lst.index(prev_item)])
                    break
                index +=1
            else:
                prev_item = j
                index += 1
    return output

#note here, if two vars are equal they count towards gcf since you have to multiply one by -1
