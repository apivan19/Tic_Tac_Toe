# Written in Python 3.7

# TODO: Make the various windows more modular
# TODO: Allow the Program to use words that are 3 - 15 letters long, not just 4-6

# Import graphics module
from graphics import *

# Import random function
from random import *

# Import math module
from math import *

# Import time module
import time

# Define the main() function
def main():
    # Objects returned by control panel are saved in variables
    (
        controlwin,
        newgamebutton,
        quitgamebutton,
        instructbutton,
        hintbutton,
        scoresbutton,
    ) = controlpanel()
    # Gets clicked point
    point = controlwin.getMouse()
    # Boolean condition for while loop
    gameon = False
    # Call the squareclicked() function for the INSTRUCTIONS button
    instructbool = squareclicked(point, instructbutton)
    # Call the squareclicked() function for the QUIT button
    quitbool = squareclicked(point, quitgamebutton)
    # Call the squareclicked() function for the NEW button
    newbool = squareclicked(point, newgamebutton)
    gamewinopen = False
    # Call the squareclicked() function for the HIGHSCORES button
    scoresbool = squareclicked(point, scoresbutton)

    # If INSTRUCTIONS is clicked, open instructions window
    if instructbool:
        instructions()
    # If QUIT is clicked, close the window and exit the program
    if quitbool:
        controlwin.close()
    # If NEW is clicked, open the gamepanel with all the graphic objects
    # Assign round number with score 10 for round 1
    round = 1
    score = 10
    if newbool:
        gameon = True
        # Prompts the user for what difficulty they want to play for that round and selects a word accordingly
        (
            gamewin,
            circleslist,
            alphabetlist,
            whilepolylist,
            blackpolylist,
            wordcharlist,
            guesswordlist,
            wordtoguess,
            scoretext,
            alphabet,
        ) = gamepanel()
        scoretext = Text(Point(200, 35), "SCORE: " + str(score))
        scoretext.draw(gamewin)
        gamewinopen = True
    # If HIGHSCORES is clicked, sort the file and open the high scores panel
    if scoresbool:
        # Sort the Scores file
        sort_file()
        # Opens the high score panel
        highscores()
    # Initialize boolean for gamewon
    gamewon = False
    hintallowed = True
    # Variable keeps track of polygons that have fallen
    found = 0
    poly = 0
    # Initialize boolean for gamelost
    gamelost = False
    # Use a while loop to display functions during gameplay
    while gameon:
        # Check mouse in the control panel
        checkcontrol = controlwin.checkMouse()
        # Use an if statement to check for clicks in the control panel
        if checkcontrol != None:
            # Call the squarclicked() function for NEW, QUIT, INSTRUCTIONS, HINT, and SCORES buttons
            nquitbool = squareclicked(checkcontrol, quitgamebutton)
            nnewbool = squareclicked(checkcontrol, newgamebutton)
            ninstructbool = squareclicked(checkcontrol, instructbutton)
            nhintbool = squareclicked(checkcontrol, hintbutton)
            nscoresbool = squareclicked(checkcontrol, scoresbutton)
            # if INSTRUCTIONS button is clicked, open the instructions
            if ninstructbool:
                instructions()
            # If QUIT button is clicked, close the window and exit the program
            if nquitbool:
                instructionspanel.close()
                highscorespanel.close()
                gamewin.close()
                controlwin.close()
                exit()
                gameon = False
            # If SCORES button is clicked, sort the file and open the high score panel
            if nscoresbool:
                sort_file()
                highscores()
            # If NEW button is clicked, close the window
            if nnewbool:
                gamewin.close()
                # Reopen a new gamepanel and call graphic object lists #WTF IS WHILEPOLYLIST
                (
                    gamewin,
                    circleslist,
                    alphabetlist,
                    whilepolylist,
                    blackpolylist,
                    wordcharlist,
                    guesswordlist,
                    wordtoguess,
                    scoretext,
                    alphabet,
                ) = gamepanel()
                # Reset score to 10
                score = 10
                found = 0
                # Undraw the score text
                scoretext.undraw()
                # Draw score text object with updated score
                scoretext = Text(Point(200, 35), "SCORE: " + str(score))
                scoretext.draw(gamewin)
                # Resets the polygons dropped number to 0
                poly = 0
                # Boolean for if the game window is open set to true again and EDGE CASE
                gamewinopen = True
                hintallowed = True
            # If hintbutton is clicked and hints are allowed:
            if nhintbool and hintallowed:
                # If score is greater than two, allow them to use a hint
                if score >= 2:
                    drop(blackpolylist[poly])
                    drop(blackpolylist[poly])
                    poly += 2
                    score -= 2
                    scoretext.undraw()
                    scoretext = Text(Point(200, 35), "SCORE: " + str(score))
                    scoretext.draw(gamewin)
                    # reset the boolean of hintallowed
                    hintallowed = False
                    # if all 10 polygons are lost, dispaly losing text
                    if poly == 10:
                        gamelost = True
                        # Display "losing" Text - Feature #2
                        word = "".join(wordcharlist)
                        losttext = Text(
                            Point(200, 200), f"YOU LOSE :( The word was {word}"
                        )
                        losttext.setTextColor("red")
                        losttext.setStyle("bold")
                        losttext.draw(gamewin)
                        # Display the text box that prompts the user to enter their name
                        enter_name_request = Text(Point(200, 250), "Enter your name: ")
                        enter_name_request.setTextColor("black")
                        enter_name_request.setStyle("bold")
                        enter_name_request.draw(gamewin)
                        # Display the entry box for the user to enter their name into
                        enter_name = Entry(Point(200, 300), 30)
                        enter_name.setFill("black")
                        enter_name.setTextColor("white")
                        enter_name.draw(gamewin)
                        # When the user clicks anywhere the text in the entry box is saved to the file
                        while True:
                            point = gamewin.getMouse()
                            name = enter_name.getText()
                            print(name)
                            if name:
                                break
                            else:
                                pass
                        with open("scores.txt", "a") as file:
                            file.write(f"{name},{round},{score}")
                # If score == 1, drop one polygon and display the losing text (EDGE CASE)
                if score == 1:
                    drop(blackpolylist[poly])
                    poly += 1
                    score -= 1
                    scoretext.undraw()
                    scoretext = Text(Point(200, 35), "SCORE: " + str(score))
                    scoretext.draw(gamewin)
                    hintallowed = False
                    if poly == 10:
                        gamelost = True
                        # Display "losing" Text - Feature #2
                        word = "".join(wordcharlist)
                        losttext = Text(
                            Point(200, 200), f"YOU LOSE :( The word was {word}"
                        )
                        losttext.setTextColor("red")
                        losttext.setStyle("bold")
                        losttext.draw(gamewin)
                        # Display the text box that prompts the user to enter their name
                        enter_name_request = Text(Point(200, 250), "Enter your name: ")
                        enter_name_request.setTextColor("black")
                        enter_name_request.setStyle("bold")
                        enter_name_request.draw(gamewin)
                        # Display the entry box for the user to enter their name into
                        enter_name = Entry(Point(200, 300), 30)
                        enter_name.setFill("black")
                        enter_name.setTextColor("white")
                        enter_name.draw(gamewin)
                        # When the user clicks anywhere the text in the entry box is saved to the file
                        while True:
                            point = gamewin.getMouse()
                            name = enter_name.getText()
                            print(name)
                            if name:
                                break
                            else:
                                pass
                        with open("scores.txt", "a") as file:
                            file.write(f"{name},{round},{score}")

                alphabet = [
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                    "M",
                    "N",
                    "O",
                    "P",
                    "Q",
                    "R",
                    "S",
                    "T",
                    "U",
                    "V",
                    "W",
                    "X",
                    "Y",
                    "Z",
                ]
                hintfinishbool = True
                hintfinishcount = 0
                # While boolean is true, pick 3 letters out of the alphabet list
                while hintfinishbool == True:
                    x = randint(1, 26)
                    # if the counter has reached 3 [letters eliminated], the hint has done its job
                    if hintfinishcount == 3:
                        hintfinishbool = False
                        break
                    # if the letter is in the word you are guessing, the computer will choose another letter
                    if alphabet[x - 1] in wordtoguess:
                        pass
                    # if the letter is NOT in the word you are guessing, the computer will eliminate it and increment the counter by 1
                    else:
                        circleslist[x - 1].setFill("gold")
                        alphabetlist[x - 1].setTextColor("black")
                        hintfinishcount += 1

        # If the gamepanel is open, only then move on in the code
        if gamewinopen == True:
            # Get the point
            point = gamewin.checkMouse()
            # If the point upon check mouse exists only then move on in the code
            if point != None:
                # Close the gamepanel, call graphics objects lists
                if gamewon == True:
                    gamewin.close()
                    (
                        gamewin,
                        circleslist,
                        alphabetlist,
                        whilepolylist,
                        blackpolylist,
                        wordcharlist,
                        guesswordlist,
                        wordtoguess,
                        scoretext,
                        alphabet,
                    ) = gamepanel()
                    # Update and draw the score
                    scoretext = Text(Point(200, 35), "SCORE: " + str(score))
                    scoretext.draw(gamewin)
                    # Sets the game window bool to be true one new gamepanel is opened
                    gamewinopen = True
                    found = 0
                    # Sets the game won to false
                    gamewon = False
                    # Reset the polygons dropped number to 0
                    poly = 0
                    hintallowed = True
                # If game is lost, reset the entire P block
                if gamelost == True:
                    # Sets the game lost back to false so when new game is started, it is reset
                    gamelost = False
                    # Reset the polygons dropped number to 0
                    poly = 0
                    found = 0
                    # Resets the score back to 10
                    score = 10
                    # Round is reset to 0 for the next game
                    round = 0
                    # Closes the game panel
                    gamewin.close()
                    # Since game panel is closed, the boolean is false
                    gamewinopen = False
                # Only if the game window is open, then go to the for loop
                if gamewinopen == True:
                    # Use a for loop and call the cicrcleclicked() function to check if a circle has been clicked
                    for i in range(26):
                        circboolean = circleclicked(point, circleslist[i])
                        # If a circle has been clicked, change the color to gold and the text to black
                        if circboolean:
                            circleslist[i].setFill("gold")
                            alphabetlist[i].setTextColor("black")
                            # If the letter is in the secret word print the letter
                            if str(alphabet[i]) in wordtoguess:
                                print(wordcharlist)
                                # Starts a for loop in the list of the letters of the word to be guessed, so each selected button
                                # can be compared to the letters in the list
                                for q in range(len(wordcharlist)):
                                    # If the alphabet selected matches an alphabet in the word, then it displays the alphabet
                                    if alphabet[i] == wordcharlist[q]:
                                        guesswordlist[q].draw(gamewin)
                                        found = found + 1
                                        # If you win 10 rounds, display this winning text
                                        if found == len(wordcharlist) and round == 10:
                                            gamewon = True
                                            wintext = Text(
                                                Point(200, 200), "YOU WIN!!! BOILER UP"
                                            )
                                            wintext.setTextColor("red")
                                            wintext.setStyle("bold")
                                            wintext.draw(gamewin)
                                            # Make a Text Box that prompts the user for their name
                                            enter_name_request = Text(
                                                Point(200, 250), "Enter your name: "
                                            )
                                            enter_name_request.setTextColor("black")
                                            enter_name_request.setStyle("bold")
                                            enter_name_request.draw(gamewin)
                                            # Make the entry box for the player to enter their name
                                            enter_name = Entry(Point(200, 300), 30)
                                            enter_name.setFill("black")
                                            enter_name.setTextColor("white")
                                            enter_name.draw(gamewin)
                                            # When the user clicks anywhere the text in the entry box is saved to the file
                                            while True:
                                                point = gamewin.getMouse()
                                                name = enter_name.getText()
                                                print(name)
                                                if name:
                                                    break
                                                else:
                                                    pass
                                            with open("scores.txt", "a") as file:
                                                file.write(f"{name},{round},{score}")
                                        # if you found the number of letters that are in the word:
                                        elif found == len(wordcharlist):
                                            gamewon = True
                                            # Display text when you won the round
                                            wintext = Text(
                                                Point(200, 200),
                                                f"Great Job! Click to Start Round {round+1}",
                                            )
                                            wintext.setTextColor("red")
                                            wintext.setStyle("bold")
                                            wintext.draw(gamewin)
                                            # Increment score by 10 for the next round and also increment the round
                                            round = round + 1
                                            score = score + 10
                            # If a round is lost, decrease the score by 1
                            else:
                                print(alphabet[i])
                                score = score - 1
                                # Call the drop function to drop a polygon
                                drop(blackpolylist[poly])
                                poly = poly + 1
                                # If all 10 polygons have been dropped, display "GAME LOST"
                                if poly == 10:
                                    gamelost = True
                                    # Display "losing" Text - Feature #2
                                    word = "".join(wordcharlist)
                                    losttext = Text(
                                        Point(200, 200),
                                        f"YOU LOSE :( The word was {word}",
                                    )
                                    losttext.setTextColor("red")
                                    losttext.setStyle("bold")
                                    losttext.draw(gamewin)
                                    # Display the text box that prompts the user to enter their name
                                    enter_name_request = Text(
                                        Point(200, 250), "Enter your name: "
                                    )
                                    enter_name_request.setTextColor("black")
                                    enter_name_request.setStyle("bold")
                                    enter_name_request.draw(gamewin)
                                    # Display the entry box for the user to enter their name into
                                    enter_name = Entry(Point(200, 300), 30)
                                    enter_name.setFill("black")
                                    enter_name.setTextColor("white")
                                    enter_name.draw(gamewin)
                                    # When the user clicks anywhere the text in the entry box is saved to the file
                                    while True:
                                        point = gamewin.getMouse()
                                        name = enter_name.getText()
                                        print(name)
                                        if name:
                                            break
                                        else:
                                            pass
                                    with open("scores.txt", "a") as file:
                                        file.write(f"{name},{round},{score}")
                            # Undraw the score text to reset
                            scoretext.undraw()
                            # Draw the score text with updated score
                            scoretext = Text(Point(200, 35), "SCORE: " + str(score))
                            scoretext.draw(gamewin)


# Function that defines the controlpanel() function and create the control panel
def controlpanel():
    # Make control panel window and set the background to light grey
    win = GraphWin("Welcome to:", 250, 250)
    win.setBackground("light grey")

    # Create the black rectangle containing the title "GUESS MASTER 3.0" title
    rect = Rectangle(Point(0, 0), Point(250, 20))
    rect.setFill("black")
    rect.draw(win)

    # Create a gold and bold text object title GUESS MASTER 3.0
    text = Text(Point(125, 10), "GUESS MASTER 3.0")
    text.setTextColor("gold")
    text.setStyle("bold")
    text.draw(win)

    # Create the NEW button with the NEW text inside it
    newbutton = Rectangle(Point(15, 40), Point(70, 70))
    newbutton.setFill("gold")
    newbutton.draw(win)
    new_text = Text(Point(42, 55), "NEW")
    new_text.setStyle("bold")
    new_text.setSize(10)
    new_text.draw(win)

    # Create the QUIT button with the QUIT text inside it
    quitbutton = Rectangle(Point(180, 40), Point(235, 70))
    quitbutton.setFill("black")
    quitbutton.draw(win)
    quit_text = Text(Point(205, 55), " QUIT")
    quit_text.setTextColor("gold")
    quit_text.setStyle("bold")
    quit_text.setSize(10)
    quit_text.draw(win)

    # Create the white rectangle that contains the GUESS MASTER description
    rect2 = Rectangle(Point(15, 90), Point(235, 155))
    rect2.setFill("white")
    rect2.draw(win)
    description = Text(
        Point(120, 122),
        """This is a game where your score is
    based on the number of 4-6 letter
    words you can guess within 10 tries""",
    )
    description.setSize(10)
    description.draw(win)

    # Show directions for starting a new game
    startprompt = Text(Point(120, 175), "Click NEW to start a game...")
    startprompt.setSize(10)
    startprompt.draw(win)

    # Create the Hint button
    hintbutton = Rectangle(Point(97, 40), Point(152, 70))
    hintbutton.setFill("white")
    hintbutton.draw(win)
    hinttext = Text(Point(125, 55), "HINT")
    hinttext.setStyle("bold")
    hinttext.setSize(10)
    hinttext.draw(win)

    # Create the Instructions button
    instructbutton = Rectangle(Point(10, 210), Point(115, 230))
    instructbutton.setFill("gold")
    instructbutton.draw(win)
    instructionstext = Text(Point(62, 220), "INSTRUCTIONS")
    instructionstext.setStyle("bold")
    instructionstext.setSize(10)
    instructionstext.draw(win)

    # Create the High Scores button
    scoresbutton = Rectangle(Point(150, 210), Point(240, 230))
    scoresbutton.setFill("black")
    scoresbutton.draw(win)
    scoresbuttontext = Text(Point(195, 220), "HIGH SCORES")
    scoresbuttontext.setStyle("bold")
    scoresbuttontext.setTextColor("gold")
    scoresbuttontext.setSize(10)
    scoresbuttontext.draw(win)

    # Return the win, newbutton, quitbutton graphic objects
    return win, newbutton, quitbutton, instructbutton, hintbutton, scoresbutton


# Define the gamepanel() function and create the game panel with a gold background
def gamepanel():
    gamepanel = GraphWin("Save the Block P", 400, 400)
    gamepanel.setBackground("gold")
    # Create the text object to display the SCORE at the top of the game panel
    scoretext = Text(Point(200, 35), "")
    scoretext.setTextColor("black")
    scoretext.draw(gamepanel)
    # Initialize the x and y points to be used in the for loop and if statements to create the circles
    x = 20
    y = 340
    tx = 20
    ty = 342
    # Create a list of alphabets
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    # Create a list of the number of circles
    list_circles = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
    ]
    # Create a list for the text objects for the alphabets
    list_alphabet = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
    ]
    # Create a for loop to create the circles with alphabets
    for i in range(26):
        # Moves the circles to the next line once 13 circles are created on the top line
        if i == 13:
            x = 20
            y = 370
            tx = 20
            ty = 372
        # Draw the circles with radius 12 and set the color to black
        circle = Circle(Point(x, y), 12)
        circle.setFill("black")
        # Moves the circles by 30
        list_circles[i] = circle
        x += 30
        # Add the white alphabet letters to the circles
        num = Text(Point(tx, ty), alphabet[i])
        num.setTextColor("white")
        # Move each alphabet to the right by 30
        list_alphabet[i] = num
        tx += 30

    # Create a for loop to draw the circle and alphabet objects in the gamepanel
    for j in range(26):
        list_circles[j].draw(gamepanel)
        list_alphabet[j].draw(gamepanel)

    # Create lists of white and black polygons objects
    wlist_polygons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    blist_polygons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create the top horizontal polygons in the P block and set the color to white
    polygon1 = Polygon(
        Point(150, 100), Point(140, 130), Point(190, 130), Point(200, 100)
    )
    polygon1.setFill("white")
    wlist_polygons[0] = polygon1

    polygon2 = Polygon(
        Point(200, 100), Point(190, 130), Point(240, 130), Point(250, 100)
    )
    polygon2.setFill("white")
    wlist_polygons[1] = polygon2

    polygon3 = Polygon(
        Point(250, 100), Point(240, 130), Point(290, 130), Point(300, 100)
    )
    polygon3.setFill("white")
    wlist_polygons[2] = polygon3

    # Create the polygons below the first top left polygon in the P block and set the color to white
    polygon4 = Polygon(
        Point(140, 130), Point(130, 160), Point(180, 160), Point(190, 130)
    )
    polygon4.setFill("white")
    wlist_polygons[3] = polygon4

    polygon5 = Polygon(
        Point(130, 160), Point(120, 190), Point(170, 190), Point(180, 160)
    )
    polygon5.setFill("white")
    wlist_polygons[4] = polygon5

    polygon6 = Polygon(
        Point(120, 190), Point(110, 220), Point(160, 220), Point(170, 190)
    )
    polygon6.setFill("white")
    wlist_polygons[5] = polygon6

    # Create the polygon right in the center of the P block and set the color to white
    polygon7 = Polygon(
        Point(180, 160), Point(170, 190), Point(220, 190), Point(230, 160)
    )
    polygon7.setFill("white")
    wlist_polygons[6] = polygon7

    # Create the middle right polygon of the P block and set the color to white
    polygon8 = Polygon(
        Point(230, 160), Point(220, 190), Point(270, 190), Point(280, 160)
    )
    polygon8.setFill("white")
    wlist_polygons[7] = polygon8

    # Create the polygon above middle right polygon and below top right polygon and set the color to white
    polygon9 = Polygon(
        Point(240, 130), Point(230, 160), Point(280, 160), Point(290, 130)
    )
    polygon9.setFill("white")
    wlist_polygons[8] = polygon9

    # Create the polygon at the extreme bottom left of the P block and set the color to white
    polygon10 = Polygon(
        Point(105, 220), Point(100, 240), Point(165, 240), Point(170, 220)
    )
    polygon10.setFill("white")
    wlist_polygons[9] = polygon10

    # BLACK POLYGONS BELOW!
    # Create the top horizontal polygons in the P block and set the color to black
    polygon11 = Polygon(
        Point(150, 100), Point(140, 130), Point(190, 130), Point(200, 100)
    )
    polygon11.setFill("black")
    blist_polygons[0] = polygon11

    polygon22 = Polygon(
        Point(200, 100), Point(190, 130), Point(240, 130), Point(250, 100)
    )
    polygon22.setFill("black")
    blist_polygons[1] = polygon22

    polygon33 = Polygon(
        Point(250, 100), Point(240, 130), Point(290, 130), Point(300, 100)
    )
    polygon33.setFill("black")
    blist_polygons[2] = polygon33

    # Create the polygons below the first top left polygon in the P block and set the color to black
    polygon44 = Polygon(
        Point(140, 130), Point(130, 160), Point(180, 160), Point(190, 130)
    )
    polygon44.setFill("black")
    blist_polygons[3] = polygon44

    polygon55 = Polygon(
        Point(130, 160), Point(120, 190), Point(170, 190), Point(180, 160)
    )
    polygon55.setFill("black")
    blist_polygons[4] = polygon55

    polygon66 = Polygon(
        Point(120, 190), Point(110, 220), Point(160, 220), Point(170, 190)
    )
    polygon66.setFill("black")
    blist_polygons[5] = polygon66

    # Create the polygon right in the center of the P block and set the color to black
    polygon77 = Polygon(
        Point(180, 160), Point(170, 190), Point(220, 190), Point(230, 160)
    )
    polygon77.setFill("black")
    blist_polygons[6] = polygon77

    # Create the middle right polygon of the P block and set the color to black
    polygon88 = Polygon(
        Point(230, 160), Point(220, 190), Point(270, 190), Point(280, 160)
    )
    polygon88.setFill("black")
    blist_polygons[7] = polygon88

    # Create the polygon above middle right polygon and below top right polygon and set the color to black
    polygon99 = Polygon(
        Point(240, 130), Point(230, 160), Point(280, 160), Point(290, 130)
    )
    polygon99.setFill("black")
    blist_polygons[8] = polygon99

    # Create the polygon at the extreme bottom left of the P block and set the color to black
    polygon110 = Polygon(
        Point(105, 220), Point(100, 240), Point(165, 240), Point(170, 220)
    )
    polygon110.setFill("black")
    blist_polygons[9] = polygon110

    # Draws the white polygons
    for k in range(10):
        wlist_polygons[k].draw(gamepanel)
    # Draws the black polygons
    for l in range(10):
        blist_polygons[l].draw(gamepanel)

    # Prompts the user for what difficulty they want to play for that round and selects a word accordingly
    list_words = difficulty()
    # Select random word from file words.txt
    x = randint(1, len(list_words))
    newstring = list_words[x]
    # Initialize the x and y points to create the rectangles representing the length of the secret word
    rectx = 200 - ((len(newstring) / 2) * 40)
    recty = 50
    recbx = rectx + 40
    recby = 90
    # Create empty lists
    list_guessrect = []
    list_guessword = []
    # Converts the selected random word from a string to a list
    wordcharlist = list(newstring)
    # Initializing the location of the letters in the rectangles
    wordrectx = 200 - ((len(newstring) / 2) * 32)
    wordrecty = 70

    # Creates rectangles based on length of secret word and sets the color to gold
    for x in range(len(newstring)):
        placebox = Rectangle(Point(rectx, recty), Point(recbx, recby))
        placebox.setFill("gold")
        # Creates a text object to fill the guessed letter in the rectangle
        wordchardisplay = Text(Point(wordrectx, wordrecty), wordcharlist[x])
        # Set text color to black
        wordchardisplay.setTextColor("black")
        # Upon creating each rectangle, appending to the list
        list_guessrect.append(placebox)
        list_guessword.append(wordchardisplay)
        # Updating the position of the rectangle
        rectx += 40
        recbx += 40
        # Updating the position of letters
        wordrectx += 40
    # Draw the rectangle boxes based on the number of letters in the secret word
    for x in range(len(newstring)):
        list_guessrect[x].draw(gamepanel)
    # Return the gamepanel and lists of graphic objects
    return (
        gamepanel,
        list_circles,
        list_alphabet,
        wlist_polygons,
        blist_polygons,
        wordcharlist,
        list_guessword,
        newstring,
        scoretext,
        alphabet,
    )


# Define the drop() function to accept a parameter
def drop(inpolygon):
    polygon = inpolygon
    # Change the color of the polygon to red
    polygon.setFill("red")
    # Get the points of the polygon
    point1 = polygon.getPoints()
    # Create for loop to animate the movement of the polygon
    for x in range(400):
        polygon.move(0, x)
        x = x + 10


# Define the squareclicked function() to allow clicks in the NEW and QUIT buttons
def squareclicked(point, square):
    # Get the points of X and Y where clicked
    clickx = point.getX()
    clicky = point.getY()
    # Get the points of the button
    point1 = square.getP1()
    point2 = square.getP2()
    # Get the x and y points of the button
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()
    # If clicked between the two points return True
    if x1 < clickx < x2 and y1 < clicky < y2:
        return True
    else:
        return False


# Create the circleclicked function() to accept two parameters to create the alphabet buttons
def circleclicked(point, circle):
    # Determine the properties of point and circle
    point_x = point.getX()
    point_y = point.getY()
    circle_radius = circle.getRadius()
    circle_center = circle.getCenter()
    circle_centerX = circle_center.getX()
    circle_centerY = circle_center.getY()
    # Calculate the distance
    distance = sqrt((circle_centerX - point_x) ** 2 + (circle_centerY - point_y) ** 2)
    # Create an if statement to determine if distance is less than radius
    if distance < circle_radius:
        return True
    else:
        return False


# Create the instructions window - Feature #1
def instructions():
    instructionspanel = GraphWin("Instructions", 350, 350)
    instructionspanel.setBackground("gold")
    # The header for the instructions panel
    headerbox = Rectangle(Point(0, 0), Point(350, 40))
    headerbox.setFill("black")
    headerbox.draw(instructionspanel)
    headertext = Text(Point(175, 20), "How to Play!")
    headertext.setTextColor("gold")
    headertext.setStyle("bold")
    headertext.setSize(20)
    headertext.draw(instructionspanel)

    # The Instructions Text
    instructiontext = Text(
        Point(175, 200),
        """A 4-6 letter word will be randomly selected

    Your job is to guess it

    Click on the letters at the bottom to guess the word

    A wrong guess will cause the P to degrade a little

    You have 10 tries to guess the word or you LOSE

    Every round won will add to your score

    If you win 10 rounds, you with the game

    The HINT button may help you out once a round

    ... at a cost""",
    )
    instructiontext.setStyle("bold")
    instructiontext.setSize(10)
    instructiontext.draw(instructionspanel)


# High scores panel
def highscores():
    list_of_text_objects = []
    highscorespanel = GraphWin("High Scores", 350, 350)
    highscorespanel.setBackground("white")

    # Reads the information from the txt file
    scores_file = open("scores.txt")
    scores_list = scores_file.readlines()

    # Make the High Scores Column Label Text Object and add it to list of objects
    scores_labels = Text(
        Point(140, 20), f"         Player                  Rounds                Score"
    )
    scores_labels.setTextColor("black")
    scores_labels.setStyle("bold")
    scores_labels.setSize(12)
    list_of_text_objects.append(scores_labels)

    # Make the cutesey border between the column labels and the data and then add it to the list of objects
    scores_border = Text(Point(170, 40), "=-" * 22 + "=")
    scores_border.setTextColor("black")
    scores_border.setStyle("bold")
    scores_border.setSize(12)
    list_of_text_objects.append(scores_border)
    # A counter so that only the top 7 scores are loaded onto the scoreboard
    number = 1
    y = 70
    # Iterate over the information from the file that was stored in a list
    for line in scores_list:
        x = 150
        # Break it apart into a list of lists where the sublists are composed of [player_name, round, score]
        person_list = line.split(",")
        # Make the objects for each of the top 7 scorers and then add them to the list of objects
        highscorer_stats = Text(
            Point(x, y),
            f"{person_list[0].ljust(10)}                     {person_list[1]}                           {person_list[2]}",
        )
        highscorer_stats.setTextColor("black")
        highscorer_stats.setStyle("bold")
        highscorer_stats.setSize(10)
        list_of_text_objects.append(highscorer_stats)
        # The next scorer's information will be 40 pixels lower
        y += 40
        number += 1
        # Don't create an object for the 8th top scorer.
        if number == 8:
            break

    # Draw all objects in list
    for text in list_of_text_objects:
        text.draw(highscorespanel)

    # Move objects up and then to the bottom again
    while True:
        # Iterates over the list and moves each item up a bit
        for item in list_of_text_objects:
            item.move(0, -2)
            time.sleep(0.001)
            # If the item reaches the top, send it back to the bottom by changing it's Y by +350
            if item.getAnchor().getY() <= 0:
                item.move(0, 350)


# Function that sorts the scores.txt file
def sort_file():
    # importing pandas package
    import pandas as pd

    # making data frame from csv file and adding labels to the columns
    data = pd.read_csv("scores.txt", names=["Name", "Rounds", "Score"])
    data
    # sorting data frame by Score and then by Rounds
    data.sort_values(["Score", "Rounds"], axis=0, ascending=False, inplace=True)
    data
    # save the data back to the scores.txt file
    data.to_csv(path_or_buf="scores.txt", sep=",", index=False, header=False)


# Feature 3: Function that returns the list of words necessary for the difficulty that the player selects.
def difficulty():
    difficultywin = GraphWin("Select a Difficulty", 200, 200)
    difficultywin.setBackground("gold")
    # Create the easy button
    easybutton = Rectangle(Point(20, 15), Point(180, 45))
    easybutton.setFill("black")
    easybutton.draw(difficultywin)
    easybuttontext = Text(Point(50, 30), "EASY")
    easybuttontext.setSize(12)
    easybuttontext.setStyle("bold")
    easybuttontext.setTextColor("white")
    easybuttontext.draw(difficultywin)

    # Create the medium button
    mediumbutton = Rectangle(Point(20, 55), Point(180, 85))
    mediumbutton.setFill("black")
    mediumbutton.draw(difficultywin)
    mediumbuttontext = Text(Point(60, 70), "MEDIUM")
    mediumbuttontext.setSize(12)
    mediumbuttontext.setStyle("bold")
    mediumbuttontext.setTextColor("white")
    mediumbuttontext.draw(difficultywin)

    # Create the hard button
    hardbutton = Rectangle(Point(20, 95), Point(180, 125))
    hardbutton.setFill("black")
    hardbutton.draw(difficultywin)
    hardbuttontext = Text(Point(50, 110), "HARD")
    hardbuttontext.setSize(12)
    hardbuttontext.setStyle("bold")
    hardbuttontext.setTextColor("white")
    hardbuttontext.draw(difficultywin)

    # Text message that prompts the user to select a difficulty
    select_text = Text(Point(100, 150), "Select a Difficulty!")
    select_text.setSize(12)
    select_text.setStyle("bold")
    select_text.draw(difficultywin)
    # Checks that the words.txt file is actually where it is supposed to be
    import os.path

    if os.path.isfile("words.txt"):
        with open("words.txt") as file:
            allwordslist = file.readlines()
    else:
        print(
            "Please place the 'words.txt' file in the same folder as project3_master.py"
        )
    # Split up the words appropriately for the different difficulties
    formattedwordslist = []
    for word in allwordslist:
        wordstripped = word.rstrip("\n")
        formattedwordslist.append(wordstripped)
    point = difficultywin.getMouse()
    if squareclicked(point, easybutton):
        difficultywin.close()
        easywords = []
        for word in formattedwordslist:
            if len(word) == 4:
                easywords.append(word)
        return easywords
    if squareclicked(point, mediumbutton):
        difficultywin.close()
        mediumwords = []
        for word in formattedwordslist:
            if len(word) == 5:
                mediumwords.append(word)
        return mediumwords
    if squareclicked(point, hardbutton):
        difficultywin.close()
        hardwords = []
        for word in formattedwordslist:
            if len(word) == 6:
                hardwords.append(word)
        return hardwords


# Call the main() function the proper way
if __name__ == "__main__":
    main()

