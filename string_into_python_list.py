MyList = []

# convert string into 2d array ( python list )
# the main idea is and 2d list in python look like : "  [[1, 0, 10], [25, 35, 2], [0 ,0 ,0]]
# so we should 2 nested loop between  '['  and  ']'  and catch numbers and skip ',' and 'SPACE'

def string_to_list(myString):
    indx = 0
    rowList = []
    finalList = []
    if myString[0]=='[': # the first character start with '['  /// start character must be '['
        indx = indx + 1
        while myString[indx]!=']': # while we dont reach the ']'
            if myString[indx]==',': # skip all character ','
                indx = indx + 1
            elif myString[indx]==' ': # skip all character ' ' SPACE
                indx = indx + 1
            elif myString[indx]=='[' : # for all rows that start with '['
                indx = indx + 1
                while myString[indx]!=']': # while dosemt reach the closing tag ']'
                    if myString[indx]==',': # skip all character ','
                        indx = indx + 1
                    elif myString[indx]==' ': # skip all character ' ' SPACE
                        indx = indx + 1
                    else: # for all other numbers :
                        h_indx = indx + 1
                        while myString[h_indx]!=',' and myString[h_indx]!=']': # find end index of a number
                            h_indx = h_indx + 1
                        h_Str = ""
                        for i in range(indx,h_indx): # from first_index to end_index add number character by character
                            h_Str = h_Str + str(myString[i])
                        rowList.append(int(h_Str)) # conver string of number to int and add it to array_row_list
                        indx = h_indx
                indx = indx + 1
                finalList.append(rowList) # add new row_list (1D) as new row to array_list (2D)
                rowList = [] # reset row_list
    return finalList
                    
    

myStr = str(input()) # / get input from user
MyList = string_to_list(myStr)
