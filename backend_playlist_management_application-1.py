
#**Justification Related Function "initialise"
#
#A function is created to initialise an empty list assigned to the
#variable “playlist” which will be appended to by CSV files and
#inputs from the user. Is used to create a variable for storing inputted
#data from users or imported files. The empty variable is returned. As function
#is acting as a way to initialising the data needed to store or add records no
#alternative names have been considered.
def initialise() -> list:
    
    #Empty list data is assigned to variable "playlist".
    playlist = []
    return playlist


#**Justification Related Function "add_song"
#
#The function adds stored data values within parameters “song_name” and “year”
#to the “playlist” parameter. By doing this the user's inputs taken in the front
#end module are added to the “playlist”.
def add_song(playlist: list, song_name: str, year: int):
    playlist.append( [song_name,year] )


#**Justification Related Function "get_library"
#
#Function “get_library” creates an empty string variable and performs a while loop
#to add all playlists data into total series of strings. This allows the display of
#all saved playlists and their corresponding items to be displayed and saved. 
def get_library(playlist: list) -> str:

    #Variable “library” with an empty string is created for later use in storing items
    #in all saved “playlist” lists. Alternative names such as summary could be used, but
    #in the case of a music manager program library is a more appropriate term to use
    #when describing songs found across multiple playlists.
    library=""
    
    #Variable is given integer value of 0 for use in below while loop, “i” corresponds
    #to the position 0 in the library string. Alternative name index could also be used
    #but in this case to avoid the use of length variable names as the current variable
    #“i” only is used for the placement of data and isn’t important to any detailed operations. 
    i=0

    #While loop and comparison only progress if there is data within the list “playlist”.
    while(i<len(playlist) ):
        library+=playlist[i][0]+"\t"
        library+=str(playlist[i][1])+"\n"
        i+=1
    return library
#**Justification Related Function "load_playlist"
#
#Below function “load_playlist” will open file for reading, this is done through readline.
#When the file is imported the lines are split with a comma, alternatively, they could be
#split with tabs however CSV are split with commas and thus the current method has been chosen.
#The empty list “playlist is appended the data taken from the file lines.
def load_playlist(playlist: list, filename: str):
    
    file_object = open(filename,"r")
    line = file_object.readline()

    line = file_object.readline()
    
    while(line!=""):
        fields = line.strip().split(",")
        add_song(playlist,fields[0],int(fields[1]))
        line = file_object.readline()

    file_object.close()

#**Justification Related Function "save_playlist"
#
#Function “save_playlist” will save the data inputted by the user/stored in the variable
#“library” to a CSV file.  Print statements are used however these aren’t displayed to the
#user in any way and as such are permitted to be included in the backend file/module since
#in this case they are only used to create the headings in the CSV file. Tabs are replaced
#with commas as the text contained within are being written to a file and thus need a different
#display structure.  
def save_playlist(playlist: list, filename: str):

    file_object = open(filename,"w")

    #Call to “get_library” argument will obtain values contained within and assign them to
    #current library variable. As intended data remains the same there is no conflict in using
    #the same variable name. 
    library = get_library(playlist)
    file_object.write("Song Title,Year\n")
    file_object.write(library.replace("\t",","))
    file_object.close()
    
    
    
        
    
