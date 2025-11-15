"""
Author: F. Gonzalez
Final Project
Date: 11/14/2025
I affirm that this project represents my ow work and I have upheld the schools
standards of academic integrity  ..... FG 

I pledge .... X. Felipe L. Gonzalez
"""




import random

#Different teams
one = "Porshe Piranhas, gives you lots of horsepower enter one to select"
two = "Lamborghini Leopards, gives you grip control on the course, enter two to select"
three = "Bugahtti Bulls, gives you ghost ability that if you loose a race, it doesn't count towards your total score, enter three to select"
four = "Tesla Tigers, gives you quick acceleration, enter four to select "

#Asks for racers name
name = input("Please input your full name:")

#Team selection
print("Great, now lets select your team:") 
print(one)
print(two)
print(three)
print(four)
#gives user 4 chances to enter the right team
for i in range(4):
    select = input("Choose your team").lower()
    if select == "one":
        user_team = "Porshe Prianhas"
        print("welcome to the Piranhas")   
        break
    elif select == "two":
        user_team = "Lamborghini Leopards"
        print("Welcome to the Leopards")  
        break  
    elif select == "three":
        user_team = "Bugatti Bulls"
        print("Welcome to the Bulls")  
        break  
    elif select == "four":
        user_team = "Tesla Tigers"
        print("Welcome to the Tigers")
        break

#Game start
print("Ok " + name + ",  welcome to the RACE TO MONACO!!!!")

#Different races in the season
races = ["Miami Grand Prix 🏝️ ", "Las Vegas Grand Prix 🎰", "Italian Grand Prix 🍕", "Millville Grand Prix 🌳"]
#everyone starts at 0 points
points = 0

#the other racers in the race
enemys = ["Max Verstappen", "Lewis Hamilton", "Fernando Alonso", "George Russell", "Lando Norris"]
def line():
    print("================================================")

#prints the other racers including your team
def show_racers(name, team):
    line()
    print("The racers in this race are those that follow: ")
    print("Max Verstapen: Red Bull")
    print("Lewis Hamiltion: Ferrari")
    print("Fernando Alonso: Aston Martin")
    print("George Russell: Mercedes")
    print("Lando Norris: Mclaren")
    print(                  name + ": " + user_team)


#Adds bonus for team, -1 position
def race_position(team):
    orgin = random.randint(1,6)
    if team == "Porshe Piranhas":
        orgin = orgin - 1
    elif team == "Lamborghini Leopards":
        orgin = orgin - 1
    elif team == "Tesla Tigers":
        orgin = orgin - 1
    
    if orgin < 1:
        return 1
    return orgin

#the points you get for placing
def return_points(place):
    if place == 1:
        return 25 
    elif place == 2:
        return 20
    elif place == 3:
        return 15
    elif place == 4:
        return 10
    elif place == 5:
        return 5
    elif place == 6:
        return 1
    


    
#Master function for to run the race
for race in races:
    print("Race racing: " + race)
    line()

    show_racers(name, user_team)

    line()
    print("Current Points: " + str(points))

    input("Press ENTER to start the race")


    line()
    #Stores user names + there position
    results = []
    user_roll = race_position(user_team)
    results.append([user_roll, name])

    #random places for the enemy racers
    for enemy in enemys:
        dice = random.randint(1,6)
        results.append([dice, enemy])
    results.sort()

    final_results = [] #stores there position
    pos_place = 1
    for res in results: 
        final_results.append([pos_place, res[1]])
        pos_place += 1
    #Check if the racer is there, then save there finish position
    for res in final_results:
        if res[1] == name:
            place = res[0]
    # applies the Bughatti Bulls effect
    if user_team == "Bugatti Bulls":
        if place == 5 or place == 6:
            print("Ghost ability lets go!, fifth or sixth place convert to +10 points!")
            points += 10
        else:
            points += return_points(place)
    else:
        points += return_points(place)
        
    #prints the racers stadning, position
    for result in final_results:
        position = result[0]
        racer = result[1]
        print(str(position) + ". " + racer)
    #special case for if they are bughatti bulls, then apply the effect
    if user_team == "Bugatti Bulls":
        if place == 1: 
            print("GOAT 1st place 🥇💯! +25 pts!")
        elif place == 2:
            print("Second place ain't bad🥈, +20pts")
        elif place == 3:
            print("not bad, third place 🥉, +15pts")
        elif place == 4:
            print("4th isn't the worst 🥲, +10pts")
        elif place == 5:
            print("Ghost ability activated!, instead of 5th or 6th, you get 10 points! ")
        elif place == 6:
            print("Ghost ability activated!, instead of 5th or 6th, you get 10 points! ")
    #normal effect for everyone else
    else:
        if place == 1: 
            print("GOAT 1st place 🥇💯! +25 pts!")
        elif place == 2:
            print("Second place ain't bad🥈, +20pts ")
        elif place == 3:
            print("not bad, third place 🥉, +15pts ")
        elif place == 4:
            print(" 4th isn't the worst 🥲, +10pts ")
        elif place == 5:
            print("5th is better than last 😢, +5pts ")
        elif place == 6:
            print("ahh, better luck next time, 😭 +1pts ")


line()
print("Good job you completed the season")
print("your total points were: "  + str(points))
line()

print()
line()
print("Final race for all the glory, the MONACO GRAND PRIX 🇲🇨🇲🇨")
line()
#Monaco bonus place on there points
if  0 <= points <= 35:
    monaco_bonus = 0
elif 36 <=  points <= 55:
    monaco_bonus = 1
elif  55 <= points <= 70:
    monaco_bonus = 2 
elif points >= 71:
    monaco_bonus = 3
else:
    monaco_bonus = 0

#Applies the final racse standongs and also the logic for the bonus
print("Season bonus to help win Monaco: +" + str(monaco_bonus))
input("Lets do it, if you win, you win it all, press enter to START")
place = race_position(user_team) - monaco_bonus
if place < 1:
    place = 1
print(name + " finnished in " + str(place))
#what happens if you place 1 
if place == 1:
    points_earned = return_points(place)
    points = points + points_earned
    print()
    print("YOU DID IT 🏆🏎️ 🏆🏎️ 🏆🏎️🏆 ")
    print(name + ", You have WON the unyielding race of MONACO ")
    print("You ARE the NEW FORUMLA 1 CHAMPION!!!!")
#What happens if you dont place 1 
else:
    points_earned = return_points(place)
    points = points + points_earned
    print("Better luck next year. Maybe one year, you will shake hands with paradise 😭😭😭 ")

