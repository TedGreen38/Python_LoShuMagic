'''
Name: Ted Green
Date: Jan 31, 2019
Project: Lo Shu Magic Square

'''

def read_File():
    #reads file and returns contents to the main function
    f = open("ref.txt","r")
    return f

def checkSquare(x,y,z):
    #function that will check numbers to see if they are the correct value. also makes sure there are no repeating values
    if x!=y and x!=z and y!=z: 
        if x+y+z == 15:
            return True
        else:
            return False
    else:
        return False

def main():
    #reads a file and goes through line by line
    f = read_File()
    for line in f:

        #splits up line and puts data in a 3x3 2D array
        data = line.split()
        loShu = [[int(data[0]),int(data[1]),int(data[2])],
                 [int(data[3]),int(data[4]),int(data[5])],
                 [int(data[6]),int(data[7]),int(data[8])]]

        #variable that will decide if array is a valid lo shu magic square
        valid = True

        #checks all possible 3-digit sum combinations in a lo shu magic square. if any check is false, then the current arrangement is not a pu
        if checkSquare(loShu[0][0],loShu[0][1],loShu[0][2]) == False:
            valid = False #Top Left Horizontal
        if checkSquare(loShu[0][0],loShu[1][0],loShu[2][0]) == False:
            valid = False #Top Left Vertical
            
        if checkSquare(loShu[1][0],loShu[1][1],loShu[1][2]) == False:
            valid = False #Middle Horizontal
        if checkSquare(loShu[0][1],loShu[1][1],loShu[2][1]) == False:
            valid = False #Middle Vertical
            
        if checkSquare(loShu[2][0],loShu[2][1],loShu[2][2]) == False:
            valid = False #Bot Right Horizontal
        if checkSquare(loShu[0][2],loShu[1][2],loShu[2][2]) == False:
            valid = False #Bot Right Vertical
            
        if checkSquare(loShu[0][0],loShu[1][1],loShu[2][2]) == False:
            valid = False #Top Left Diagonal
        if checkSquare(loShu[2][0],loShu[1][1],loShu[0][2]) == False:
            valid = False #Top Right Diagonal    

        if valid == True:
            print("valid")
        else:
            print("invalid")
      
main()
