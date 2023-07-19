import sys
import backend_playlist_management_application

#**Justification Comments for Code Block/Function "obtain_sttring"
#
#The core of the program's design is the input and output of strings, the “obtain_string” function
#provides an alternative to multiple sections of code where text is displayed to the user indicating
#the need for a input with a seperate statement and condition handling a invalid input. The parameter/argument
#prompt allows any section of the code to call to the “obtain_string” function and display its unique prompt
#to the user with the subsequent inputted line from the user assigned to a variable. A loop contained within
#the function will repeatedly ask for a correct input if it is empty, with the valid input from the user been
#assigned to a variable which is finally returned to the specific instance where the function is called with
#the “inputted_string” variable been assigned to the individual variable that calls to “obtain_string”.
#
#A example of this operation in the current program would be the call to the "obtain_string" function from the
#variable "song_name" in the function "main", the prompt will be displayed to the user by the write statment
#inside the below function with the users input been assinged to the "inputted_string" variable. From here the
#variable is checkec in the while loop for a empty value, if the conditon is met then the user is displayed with
#error message with the variable "inputted_string" getting the value from the line the user will input in response.
#Following from that the variable is returned to the call to it in the code which is this example is the "song_name"
#variable, resulting in the "song_name" been assinged the value returned from the function.
def obtain_string(prompt:str)->str:
   
    sys.stdout.write(prompt)
    inputted_string = sys.stdin.readline().strip()

    #While loop and conditions are implemented to check for empty inputs from the user. This is done by simply
    #done through a comparison operation if the variable “inputted_string” is equal to an empty value then the
    #condition will be met, and a print statement will display text indicating the user has given an invalid
    #input and or empty input. After the user has seen the displayed error text the variable “inputted_string”
    #is given the value of the line the user has inputted. 
    while(inputted_string == ""):
        sys.stdout.write("Invalid Input Error! Please Re-Enter: ")
        inputted_string = sys.stdin.readline().strip()

    return inputted_string

#**Justification Comments for Code Block/Function "main"
#
#A function known as “main” contains all while loops and if statements that in turn have contained readlines
#and writes from the sys library. All variable data values are assigned within “main” but are appended and or
#handled within the separate backend.py file. 
def main():
    
    playlist = backend_playlist_management_application.initialise()

    #The string variable contains the main interface and initial menu displayed to the user which contains
    #available options in the program. Current implementation cuts down on unnecessary sys write statements.
    #Having the main menu presented and organized in such a way means changes are easy to make and below
    #code-blocks are free of unneeded sys writes since they can simply refer to the variable containing the
    #menu strings. 
    main_menu=""
    main_menu+="===============================\n"
    main_menu+="Playlist Management Application\n"
    main_menu+="===============================\n"
    main_menu+="[I]mport Playlist File\n"
    main_menu+="[A]dd a Song\n"
    main_menu+="[D]isplay Songs\n"
    main_menu+="[S]ave Playlist\n"
    main_menu+="E[x]it\n"
    main_menu+="Selection: "

    sys.stdout.write(main_menu)

    #*Repeated Justification for Below Variable - Please Refer Here for Justication for "main_menu_choice"
    #
    #Reads and strips the line containing the user's input which subsequently is assigned to the variable in
    #question for later conditions when determining which menu selection has been made. As this needs to be
    #defined before any conditions its current placement is unavoidable and is the best practice. Alternative
    #names could be “choice” however given there is arguably instances where multiple examples where a choice
    #is stored/made having specific itself as only relating to main menu choice.  
    menu_menu_choice=sys.stdin.readline().strip().lower()

    #While loop and condition enable the entire program to loop after one of the available code blocks/indented
    #if statements have finished As the option to "end" the program is given to the string value of “x” when
    #anything else that is entered doesn’t meet those criteria each of the indented if statements and conditions
    #will be checked against the user's “main_menu_choice”. 
    while(menu_menu_choice!="x"):
        sys.stdout.write("\n")
        
        #The statement contains code related to importing and opening a named CSV file. Once the condition is met
        #a sys write then displays a short message indicating to the user what section of the program they are in
        #currently. A variable then calls to the obtain string function which as justified previously will display a
        #prompt, in this section of the code the prompt will be a request for the user to input a CSV filename. Then
        #from the backend module, the “load_playlist” function is run. 
        if(menu_menu_choice=="i"):
            sys.stdout.write("Import Playlist File...\n")

            #Variable calls to “obtain_string” which strips the line input from the user and then assigns it to the
            #variable name “filename”. The variable name chosen doesn’t affect other variables known as filename since
            #the program in its current state only asks for input again when saving to a CSV file. As such name of the
            #file assigned to the filename can be almost anything since this is completely user-defined, given the file
            #exists. 
            filename = obtain_string("Enter a Filename: ")
            backend_playlist_management_application.load_playlist(playlist,filename)

        #Responsibility of if statement is to take and display write statements and readlines related to operations which
        #aim to append the “playlist” list variable. Inputs are handled again by the call to the “obtain_string” function,
        #as such the variable "inputted_string" returned from that function is assigned to the variable calling to “obtain_string”,
        #which in this case is song_name. Contained within the elif statement is a loop with an indented input validation try-except.
        #This will prevent invalid integer numbers to be stored and assigned to the year variable when they are converted to strings. 
        elif (menu_menu_choice=="a"):
            sys.stdout.write("Add Song...\n")

            #Song name is used to store the string taken from the line the user inputs in response to the text-based prompt
            #requesting the name of the song. As with similar calls to the function “obtain_string”, the prompt is displayed,
            #and the user’s input is read from the line and assigned to the instance of the variable calling to the function
            #“obtain_string”. The current naming scheme for said variable has been made due to the overall simplicity of
            #variables purpose, as it is unlikely that the variable in question could be made more descriptive. 
            song_name = obtain_string("Enter Song Title: ")

            #Variable is given the value of “false” for the below condition and while loop. The purpose of the variable is to
            #start while loop every time to have a looping try-except scenario.
            input_ok = False

            #While loop is created to handle inputs for requested integers, previous variable “input_ok” has been created to
            #intentionally run while loop and the below try-except. Below code block will create a variable to store the user's
            #input for the prompt requesting the year of the previous inputted song that the user chose. The condition within
            #the while loop is created in such a way that it enables a loop that will always start and will only be met when
            #the input entered after it starts is correct otherwise the user will be repeatedly asked to enter a valid input for the prompt.
            while(input_ok == False):

                #Acts and operates like similar variables that call to “obtain_string”. Alternatives for a variable name that could be
                #considered are “song_year” or “year_of_song”. 
                year_string = obtain_string("Enter Song Year: ")
                try:
                    year = int(year_string)
                    input_ok = True
                except:
                    sys.stdout.write("Invalid Year! ")

            backend_playlist_management_application.add_song(playlist,song_name,year)
        
        #An elif statement is used like in all previous instances to separate each of the menu options from each other. A print statement is
        #again used to indicate what section of the program the user is in. The “get_library” function from the backend module is assigned
        #to the “library” variable in the current module. Following the variable creation, a print statement is used to provide a permanent
        #interface that has been structured to have all the relevant data displayed underneath its appropriate column. Another print statement
        #is used to display the given to the “library” variable which as previously stated is attributed to the return of the “get_library”
        #function in the backend module.
        elif (menu_menu_choice=="d"):
            sys.stdout.write("Displaying Song Items...\n")
            library = backend_playlist_management_application.get_library(playlist)
            sys.stdout.write("Song Name\tYear\n")
            sys.stdout.write(library)

        #Elif statement operates similar to previous indented elif and if statements which are used to contain their respected menu selections
        #and processes. In this case, the below code block takes an input given by the user by using the “obtain_string” function which in this
        #case prompt will be a request for the user to input a filename. Upon completion of mentioned code, the backend modules function “save_playlist”
        #is run.
        elif (menu_menu_choice=="s"):
            sys.stdout.write("Saving all Items\n")
            filename = obtain_string("Enter filename: ")
            backend_playlist_management_application.save_playlist(playlist,filename)
            
        #Else statement is entirely used to handle invalid main menu inputs, if none of the above if statements are met then the user has entered an
        #invalid input selection at the main menu. This is indicated through a sys write containing text giving the user an error and asking for another
        #input, the relevant variable readline is indented outside of the else for use in both invalid inputs and handling of options after a menu process
        #has been completed. 
        else:
            sys.stdout.write("Invalid Menu Selection, Please Re-Enter\n")

        sys.stdout.write(main_menu)

        #**Repeated Justification for Below Variable - Please Refer to Justication for "main_menu_choice"
        menu_menu_choice=sys.stdin.readline().strip().lower()
    sys.stdout.write("\nApplication Successfully Completed...\n")

main()
            
            
                
            
            
