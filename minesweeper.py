# This is the initial grid

grid1 =  [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] 
]


# Declare the mine_count function to take an argument 'gridx'

def mine_count(gridx):

    count_mines = 0                                         # Declare initial variable to count the mines, count_mines
    
    for x in range(0,len(gridx)):                           # This loop runs for x from rows 1,2,3... to end of rows. In the eg 0 to 5 range, index 0-4
        for y in range(0,len(gridx[0])):                    # This is the inner loop for columns running for y in the range 0 to the end of colunmns ie len of 1st column
            
            count_mines = 0                                 # This resets the mine count to 0 for each element in the grid

            if gridx[x][y] == '-':                          # If the index at x,y is mine free '-' then follow the below conditions to increase the mine counter

                if  x-1 >= 0 and y-1 >= 0:                  # If row indexes, x-1, and column indexes, y-1, are both above 0 then position [x-1][y-1] can be checked
                    if gridx[x-1][y-1] == '#':              # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1
                
                if  y-1 >= 0:                               # If y-1 is greater than 0 then the [x][y-1] position can be checked
                    if gridx[x][y-1] == "#":                # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1          
                
                if  x < len(gridx)-1 and y-1 >= 0:          # If x is less than length minus 1 and y is greater than -1 then the [x+1][y-1] position can be checked
                    if gridx[x+1][y-1] == "#":              # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1  
                
                if x-1 >= 0:                                # If x-1 is greater than 0 then the [x-1][y] position can be checked
                    if gridx[x-1][y] == "#":                # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1
                
                if x-1 >= 0 and y < len(gridx)-1:           # If y is less than length minus 1 and x-1 is greater than 0 then the [x-1][y+1] position can be checked
                    if gridx[x-1][y+1] == "#":              # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1                    
                
                if y < len(gridx)-1:                        # If y is less than length minus 1 then the [x][y+1] position can be checked
                    if gridx[x][y+1] == "#":                # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1                    
                
                if x < len(gridx)-1 and y < len(gridx)-1:   # If x & y are less than length minus 1 then the [x+1][y+1] position can be checked
                    if gridx[x+1][y+1] == "#":              # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1                    
                
                if x < len(gridx)-1:                        # If x is less than length minus 1 then the [x+1][y] position can be checked
                    if gridx[x+1][y] == "#":                # If there's a mine in this position then increase the count_mines by 1
                        count_mines += 1                    

                gridx[x][y] = str(count_mines)              # If no mine at the position set each grid position to the mine count
    
    return gridx


mine_count(grid1)                                           # Call the function mine_count for (grid1)
print(grid1)                                                # Print the transformed grid1
