###ENEMY TEAMS
###GAME1
###############################################################
######################GLOBALS########################
import winsound


player_1 = ""
player_2 = ""
player_3 = ""
team_name =""
ene_name = "Immortals"
play_sym ="☻"
ene_sym = "☺"
play_sym =play_sym.replace("☻", '\033[34m☻\033[0m')
ene_sym =ene_sym.replace("☺", '\033[31m☺\033[0m')
play_win =play_sym.replace("☻", '\033[4m☻\033[34m')
play_1_kills = 0
play_2_kills = 0
play_3_kills = 0
play_1_deaths = 0
play_2_deaths = 0
play_3_deaths = 0
play_team_score = 0
ene_team_score = 0
play_count = 0
game_1_finished = False
game_2_finished = False

field_base = [" "," ","  ","   ","   ","   ",
        " v","  "," ","O","    "," ▄ ",
        ""," ","╩","  ","   o","",
         "","v ","  o","  ","  ╗"," ",
         "v ","  ▄"," ","","   ╠"," ",
         " ","     ","  ","╩","╠"," ",
         " X"," ","████ ","O","╬"," ",
         "  ","    "," ", " ╦","╠"," ",
         "^ ","  ▄"," "," ","  ╠"," ",
         " ","^"," ","o  ","   ╝"," ",
         ""," ", "╦","  ","     o"," ",
         " ^"," "," ","O   "," ","▀ ",
         " ","    ",""," ","    "," "]
field = [" "," ","  ","   ","   ","   ",
        " v","  "," ","O","    "," ▄ ",
        "  "," ","╩","  "," o","  ",
         "","v ","  o","  ","  ╗"," ",
         "v ","  ▄"," ","","   ╠"," ",
         " ","     ","  ","╩","╠"," ",
         " X"," ","████ ","O","╬"," ",
         "  ","    "," ", " ╦","╠"," ",
         "^ ","  ▄"," "," ","  ╠"," ",
         " ","^"," ","o  ","   ╝"," ",
         ""," ", "╦","  ","     o"," ",
         " ^"," "," ","O","    ","▀ ",
         " ","    ",""," ","    "," "]
field1 = field_base
field2 = field_base
field3 = field_base
################################################ GAME 1_1 #######################################################
def GAME1_1_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    field1 = field_base
    play_count += 1
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} comes out defensively.")
    print(f"\nLooks like Immortals lose their snake player, shot out by {player_2}")
    play_2_kills += 1
    print(f"Both {player_1} and {player_3} are looking to bump up.")
    input("Press enter to continue")
    field1 = field_base
    field[0] = ene_sym
    field1[5] = " "
    field1[7] = " "
    field1[67] = " "
    field1[77] = " "
    field1[13] = ene_sym
    field1[61] = play_sym
    field1[75] = play_sym
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} gets into snake 1, while {player_1} is in d2.")
    print(f"\nThe Immortals take out {player_3} out of the snake. {player_3} is furious with himself")
    play_3_deaths += 1
    print(f"{player_1} and {player_2} roll their guns, trying to get a kill.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = ene_sym
    field1[13] = ene_sym
    field1[61] = play_sym
    field1[75] = " "
    field1[59] = " "
    field1[62] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} gets into the small can")
    print(f"\nThe Immortals lose the D corner. Great shot by {player_1}!!")
    play_1_kills += 1
    print(f"{player_2} wraps around and takes out the last player. Good work by them.")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()
def GAME1_1_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} moves up to the 30.")
    print(f"\nLooks like Immortals lose their dorito corner player, shot out by {player_2}, but {team_name} lose {player_1}")
    play_2_kills += 1
    play_1_deaths += 1
    print(f"Looks like {player_2} wants to move into {player_1}'s position.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = " "
    field1[5] = ene_sym
    field1[7] = " "
    field1[18] = ene_sym
    field1[77] = " "
    field1[63] = "  "
    field1[61] = play_sym
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is heads up with the snake corner.")
    print(f"\n{player_2} is having to play real tight")
    print(f"{player_3} kills the corner player. Good work heads up")
    play_3_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[18] = ene_sym
    field1[61] = play_sym
    field1[59] = " "
    field1[41] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} gets pinched out. But {player_3} is at the fifty snake")
    play_1_deaths += 1
    print(f"{player_3} takes out the last player. Great work {team_name}")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()
def GAME1_1_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} spreads the field")
    print(f"\nTwo players walking off for Immortals. This is not a good start")
    play_2_kills += 1
    play_1_kills += 1
    print(f"Looks like {team_name} wants to close this out.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = ene_sym
    field1[5] = " "
    field1[7] = " "
    field1[72] = " "
    field1[75] = " "
    field1[77] = " "
    field1[42] = play_sym
    field1[44] = play_sym
    field1[41] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe whole team is moving up from all sides.")
    print(f"\n{player_1} is shooting from the D side, {player_3} is shooting from the snake.")
    print(f"{player_2} runs down the last man")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()    
def GAME1_1_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Doubles the back.")
    print(f"\n{player_1} walks off for {team_name}")
    play_1_deaths += 1
    print(f"Looks like {player_2} walks off as does a Immortal player.")
    play_2_deaths += 1
    play_2_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[0] = " "
    field1[5] = ene_sym
    field1[7] = ene_sym
    field1[77] = " "
    field1[67] = "  "
    field1[74] = " "
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is under heavy fire.")
    print(f"\n{player_3} has a hit on his pack. {team_name} loses")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()
def GAME1_1_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Stays in the middle.")
    print(f"\nBoth Immortals and {team_name} lose a player.")
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{player_1} focusing on that D side, while {player_3} is looking snake.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = " "
    field1[5] = ene_sym
    field1[7] = " "
    field1[32] = ene_sym
    field1[44] = " "
    field1[56] = play_sym
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nImmortals come round and trade out with {player_3}.")
    print(f"\nIts one on ones")
    play_3_kills += 1
    play_3_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[5] = " "
    field1[29] = ene_sym
    field1[32] = " "
    field1[56] = " "
    field1[51] = " "
    field1[52] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} is still at the mini wall, while the Immortals come up the snake")
    play_1_deaths += 1
    print(f"{player_1} gets shot out. Such a hard lose for {team_name}")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()
def GAME1_1_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} runs down the field!!.")
    print(f"\n{player_3} gets shot out, but Immortals lose the dorito 1 player")
    play_1_kills += 1
    play_3_deaths += 1
    print(f"{player_2} is wrapping to get a better shot.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = ene_sym
    field1[5] = ene_sym
    field1[7] = " "
    field1[59] = " "
    field1[54] = play_sym
    field1[44] = play_sym 
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} knocks out the snake corner.")
    play_2_kills += 1
    print(f"\n{player_2} gets shot in the hopper. One on ones")
    play_2_deaths += 1
    print(f"{player_1} is snapping well and peels the last Immortal players face off. What a game")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_2_play_choice()
################################################ GAME 1_2 #######################################################
def GAME1_2_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} goes for a defensive play.")
    print(f"\nBoth teams have all three players survive the break")
    print(f"{player_2} moves up to the wall.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[75] = " "
    field1[44] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} runs round and trades out")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"\nThe Immortals retake the wall, {player_3} is at the God bunker")
    print(f"Looks like this will be a long point")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = " "
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[44] = " "
    field1[77] = " "
    field1[70] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} gets gogged in his battle")
    play_1_deaths += 1
    print(f"The Immortals come running down the field.{player_3} trades out. Immortals win")
    play_3_kills += 1
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_2_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go slightly aggresive.")
    print(f"\n{player_1} walks off for {team_name}.")
    play_2_kills += 1
    play_1_deaths += 1
    print(f"Looks like {player_2} takes out the man in the wall, and slides into the Dorito 2. Immortals retreat to the back corner")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[0] = ene_sym
    field1[10] = ene_sym
    field1[32] = " "
    field1[61] = " "
    field1[54] = play_sym
    field1[63] = " "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} moves up in the snake.")
    print(f"\n{player_2} is getting checked out by the ref. He seems to be clean")
    print(f"{player_3} takes out the man in the god bunker")
    play_3_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[0] = ene_sym
    field1[10] = " "
    field1[54] = play_sym
    field1[59] = " "
    field1[23] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} is putting the last man in. {player_3} is past the fifty snake")
    print(f"{player_3} takes out the last player. Amazing work by {team_name}")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_2_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go wide")
    print(f"{player_1} and {player_3} both walk off for {team_name}. What a disaster")
    play_3_deaths += 1
    play_1_deaths += 1
    print(f"three on one now. {player_2} is all alone.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[10] = " "
    field1[30] = ene_sym
    field1[35] = ene_sym
    field1[32] = ene_sym
    field1[72] = " "
    field1[75] = play_sym 
    field1[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe Immortals are closing in from all sides.")
    print(f"{player_2} gets wasted. Immortals take the point")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()    
def GAME1_2_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Doubles up the back centre.")
    print(f"\n{player_1} takes out a player.")
    play_1_kills += 1
    print(f"Looks like {player_2} is moving up to the centre brick.{player_1} is moving to the D2")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = " "
    field1[74] = " " 
    field1[75] = " "
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is under heavy fire.")
    print(f"\n{player_2} has a hit on his pack. {team_name} loses")
    print(f"{player_3} kills the corner player. Good work heads up")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_2_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Rushes the centre.")
    print(f"\n{player_2} comes round and trades out with the wall.")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"{player_1} fills in the wall, while {player_3} dives into the snake")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = " "
    field[44] = " "
    field1[56] = " "
    field1[59] = " "
    field1[51] = ' '
    field1[44] = play_sym 
    field1[53] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} shoots an Immortal player, but gets picked off.")
    print(f"\nIts one on ones")
    play_3_kills += 1
    play_3_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ' '
    field1[44] = play_sym 
    field1[53] = ' '
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} is wrapping hard. He has put the last Immortal player in")
    play_1_kills += 1
    print(f"{player_1} moves around and bunkers him! Good win for {team_name}")
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_2_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} goes all the way down the field.")
    print(f"\n{player_1} gets shot out, but Immortals lose a player too")
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{player_2} is wrapping to get a better shot.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ' '
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[54] = ' '
    field1[59] = ' '
    field1[44] = play_sym 
    field1[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} takes out the brick.")
    play_3_kills += 1
    print(f"\n{player_2} takes out the last player. Crazy move by {team_name}")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
################################################ GAME 1_3 #######################################################
def GAME1_3_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[75] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} keeps it tight.")
    print(f"\nBoth teams making their spots. Exactly the same breakout")
    print(f"Both {player_1} and {player_3} are looking to bump up.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = " "
    field2[18] = ene_sym
    field2[67] = " "
    field2[77] = " "
    field2[61] = play_sym
    field2[75] = play_sym
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is in snake 1, while {player_1} is in d2. But an Immortals player is in D3")
    print(f"\nThe Immortals take out {player_2} out of home. {player_3} crosses over")
    play_2_deaths += 1
    print(f"{player_1} and {player_2} roll their guns, trying to get a kill.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[18] = ene_sym
    field2[61] = play_sym
    field2[75] = " "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe back player for the Immortals tries to get into the god bunker...")
    print(f"\n{player_1} saw the move coming, and plastered the Immortal cenre player. Great work by {player_1}!!")
    play_1_kills += 1
    print(f"{player_3} pushes up to snake 1. He clips the pack of the dorito player. Great shot.")
    play_3_kills += 1
    input("Press enter to continue")  
    field2 = field_base
    field2[3] = " "
    field2[5] = ene_sym
    field2[61] = " "
    field2[54] = play_sym
    field2[59] = " "
    field2[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThis has been a long point. Both teams are low on paint.")
    print(f"\n{player_3} is pounding the bunker. {player_1} moves to the brick!!")
    print(f"{player_1} finally gets a hit on the last player. What an exciting point!")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_3_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[61] = play_sym
    field2[63] = play_sym +" "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} go forward off the break")
    print(f"\nLooks like Immortals shoot out {player_1} off the break")
    play_1_deaths += 1
    print(f"Looks like {player_2} holding down the snake side, while{player_3} shots down the middle.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[61] = " "
    field2[63] = play_sym +" "
    field2[53] = " "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} takes out the home player, now he is playing heads up.")
    print(f"\n{player_2} is having to play really tight at home")
    print(f"Immortals now at the 50 'X' line")
    play_3_kills += 1
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[7] = " "
    field2[5] = ene_sym
    field2[30] = ene_sym
    field2[63] = play_sym +" "
    field2[53] = play_sym
    field2[59] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_2} gets blasted down his back and {player_3} doesn't know where the {player_2} got shot from.")
    play_2_deaths += 1
    print(f"{player_3} gets shot out of the snake. Bad luck for {team_name}")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_3_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[72] = play_sym
    field2[75] = play_sym 
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} go to the corners")
    print(f"\nOne player walking off for Immortals, but {player_1} and {player_3} also walk off")
    play_3_deaths += 1
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{team_name} is in trouble here.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[5] = " "
    field2[7] = " "
    field2[27] = ene_sym
    field2[18] = ene_sym
    field2[72] = " "
    field2[75] = " " 
    field2[67] = play_sym 
    field2[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nThe Immortals moving up. {player_2} takes out the Dorito player. One on ones.")
    print(f"\nThe last Immortal player does not know where {player_2} is.")
    print(f"{player_2} spots him, and blasts him. 2 pack for {player_2}!!")
    play_2_kills += 2
    play_team_score += 1
    input("Press enter to continue")
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    game1_3_play_choice()    
def GAME1_3_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[74] = play_sym 
    field2[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Doubles up the home.")
    print(f"\n{player_3} takes out the wide player.")
    play_3_kills += 1
    print(f"And {player_2} dives into the D1, but he has been hit.")
    play_2_deaths += 1
    input("Press enter to continue")
    field2 = field_base
    field2[5] = " "
    field2[7] = ene_sym
    field2[3] = " "
    field2[18] = ene_sym
    field2[67] = " "
    field2[74] = " "
    field2[75] = " "
    field2[54] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} is in snake corner, {player_1} is in D3.")
    print(f"\n{player_1} snap shots guy in the mini wall.")
    print(f"{player_3} smokes the last player in D3!!")
    print(f"{team_name} Takes the point")
    play_3_kills += 1
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd2.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_3_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[56] = play_sym
    field2[44] = play_sym 
    field2[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} are all heading up the pipe.")
    print(f"\nImmortals lose two players off the break!")
    play_1_kills += 1
    play_2_kills += 1
    print(f"{team_name} is spreading the field, looking for the last player.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = " "
    field2[7] = " "
    field2[56] = " "
    field2[44] = " " 
    field2[51] = " "
    field2[54] = play_sym
    field2[43] = play_sym 
    field2[41] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nThe last Immortal player is stuck at home.")
    print(f"\n{player_3} comes round to finish him off")
    print(f"\nPoint to {team_name}")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()
def GAME1_3_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[54] = play_sym
    field2[44] = play_sym 
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Streak down the field!!.")
    print(f"\n{player_3} gets shot out, so does {player_1}")
    play_1_deaths += 1
    play_3_deaths += 1
    print(f"{player_2} is all alone in the brick.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[5] = " "
    field2[7] = ene_sym
    field2[35] = ene_sym
    field2[12] = ene_sym
    field2[54] = " "
    field2[44] = play_sym 
    field2[59] = " " 
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_2} gets run down. Immortals saw that play coming!")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game1_3_play_choice()

################################################ GAME 2_1 #######################################################
def GAME2_1_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    field1 = field
    play_count += 1
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} stay close.")
    print(f"\nSplater lose the man running out to snake, good job {player_3}")
    play_3_kills += 1
    print(f"{player_3} is feeling pressure. {player_2} runs up the centre to assist.")
    input("Press enter to continue")
    field1 = field
    field[0] = ene_sym
    field1[13] = ene_sym
    field1[23] = " "
    field1[75] = " "
    field1[67] = play_sym
    field1[56] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} gets shot out trying to get to the brick. while {player_1} bumps up.")
    print(f"\n{player_3} gets a great hit on home. {player_3}.")
    play_2_deaths += 1
    play_3_kills += 1
    print(f"{player_1} moves in for the kill.")
    input("Press enter to continue")
    field1 = field_base
    field[0] = ene_sym
    field1[13] = " "
    field1[67] = " "
    field1[51] = " "
    field1[54] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nSplatter lose the D corner. Good pressure from {player_1}!!")
    print(f"\nFirst point goes to, {team_name}!!")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()
def GAME2_1_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} gathers some ground.")
    print(f"\n{team_name} lose {player_1} off the break")
    play_1_deaths += 1
    print(f"{player_2} and {player_1} are getting pounded.")
    input("Press enter to continue")
    field1 = field_base
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = " "
    field1[61] = " "
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} gets hit on the pack. He is out. 3 on 1 now")
    print(f"{player_3} is a trying to get a G. Splatter is closing in")
    play_2_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[12] = " "
    field1[15] = ene_sym
    field1[35] = ene_sym
    field1[24] = ene_sym
    field1[63] = " "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} gets bunkered out")
    play_3_deaths += 1
    print(f"{team_name} lose the first point")
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()
def GAME2_1_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} spread the field")
    print(f"\nSplatter lose 2 off the break. Bad start for them")
    play_2_kills += 1
    play_3_kills += 1
    print(f"Looks like {team_name} wants to close this out.")
    input("Press enter to continue")
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = " "
    field1[72] = " "
    field1[77] = " "
    field1[60] = play_sym
    field1[75] = play_sym 
    field1[65] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} is marching up the middle, {player_3} gets shot out trying to get into snake.")
    print(f"\n{player_1} is snaps out and gets his man. Great win")
    play_1_kills += 1
    play_3_deaths += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()    
def GAME2_1_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Double up home.")
    print(f"\n{player_1} and {player_3} get kills for {team_name}")
    print(f"{team_name} are spreading the field to pinch out the last man")
    play_2_kills += 1
    play_3_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[12] = " "
    field1[15] = ene_sym
    field1[23] = " "
    field1[67] = " "
    field1[75] = " "
    field1[65] = play_sym
    field1[74] = play_sym
    field1[56] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} is under heavy fire.")
    print(f"\n{player_1} runs down the last man. {team_name} takes the first point.")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()
def GAME2_1_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[0] = ene_sym
    field1[7] = ene_sym
    field1[5] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} runs up the middle.")
    print(f"\nSplatter and {team_name} don't lose a player off the break.")
    play_1_deaths += 1
    print(f"{player_1} gets shot out.")
    input("Press enter to continue")
    field1 = field_base
    field1[23] = " "
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[35] = ene_sym
    field1[56] = " "
    field1[44] = play_sym
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nSplatter decides to come around and trade out with {player_2}.")
    print(f"\n{player_3} is all alone out there")
    play_2_kills += 1
    play_2_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[12] = " "
    field1[24] = ene_sym
    field1[35] = ene_sym
    field1[15] = " "
    field1[44] = " "
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} shoots out the snake player. What a great move.")
    play_3_kills += 1
    print(f"{player_3} is run down from the D side. Such a hard lose for {team_name}")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()
def GAME2_1_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[12] = ene_sym
    field1[15] = ene_sym
    field1[23] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go for the suprise play.")
    print(f"\n{player_3} gets shot out, and so does {player_1}")
    play_1_deaths += 1
    play_3_deaths += 1
    print(f"{player_2} is all alone up in the centre")
    input("Press enter to continue")
    field1 = field_base
    field1[12] = ene_sym
    field1[33] = ene_sym
    field1[35] = ene_sym
    field1[15] = " "
    field1[54] = " "
    field1[44] = play_sym 
    field1[59] = " " 
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} trades with the streaking Splatter player.")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"What a game! Splatter with a great play")
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_2_play_choice()
################################################ GAME 2_2 #######################################################
def GAME2_2_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} stay tight.")
    print(f"{player_3} is shot off in the break.")
    play_3_deaths += 1
    print(f"\nSplatter have good field position")
    input("Press enter to continue")
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = " "
    field1[30] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nSplatter moves up the on the D side. {player_2} has been put in")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"\n{player_2} trades out. 2 on 1")
    print(f"{player_1} runs back to the D corner")
    input("Press enter to continue")
    field1 = field_base
    field1[33] = ene_sym
    field1[18] = " "
    field1[30] = ene_sym
    field1[67] = " "
    field1[75] = " "
    field1[72] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} is fighting hard")
    print(f"The man in the brick for Splatter gets his head peeled off.{player_3} has made it 1 on 1s")
    print(f"\n{player_1} losesthe snap shooting battle. Splatter takes the second point")
    play_1_kills += 1
    play_1_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_2_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go slightly aggresive.")
    print(f"\n{player_2} and a Splatter player walk off. 2 left for {team_name} to deal with.")
    play_1_kills += 1
    play_2_deaths += 1
    print(f"Both teams have spread the field. Could be a long point")
    input("Press enter to continue")
    field1 = field_base
    field1[18] = " "
    field1[33] = ene_sym
    field1[30] = ene_sym
    field1[7] = " "
    field1[61] = play_sym
    field1[63] = " "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} moves up the snake.")
    print(f"\n{player_1} is getting checked out by the ref. He is out")
    print(f"{player_3} takes out the man in the centre can. 1 on 1s")
    play_3_kills += 1
    play_1_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[30] = ene_sym
    field1[33] = " "
    field1[61] = " "
    field1[59] = " "
    field1[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is at the fifty snake")
    print(f"{player_3} takes out the last player. Amazing work by {team_name}")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_2_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} take the corners")
    print(f"{player_1} takes out the man streaking the centre. {team_name} in a good position")
    play_1_kills += 1
    print(f"{player_3} makes it into snake while {player_2} goes to the centre brick")
    input("Press enter to continue")
    field1 = field_base
    field1[18] = " "
    field1[33] = " "
    field1[18] = ene_sym
    field1[0] = ene_sym
    field1[72] = play_sym
    field1[75] = " "
    field1[44] = play_sym 
    field1[77] = " "
    field1[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nSplatter in all sorts of trouble here. {player_3} removes the D corner")
    print(f"{player_3} keeps going and removes the last man. 2 pack for {player_3} and the point!")
    play_3_kills += 2
    play_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()    
def GAME2_2_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Doubles up the back centre.")
    print(f"\n{player_1} is removed.")
    play_1_deaths += 1
    print(f"Looks like {player_2} and {player_3} want to spread out.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[30] = ene_sym
    field1[32] = ene_sym
    field1[18] = " "
    field1[33] = ene_sym
    field1[75] = " "
    field1[67] = play_sym
    field1[74] = " " 
    field1[76] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} gets googed out.")
    print(f"\n{player_2} gets run down. {team_name} gets Aced!")
    play_3_deaths += 1
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_2_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Run up the centre.")
    print(f"\n{player_1} kills the man running to D2.")
    play_1_kills += 1
    play_2_deaths += 1
    play_3_deaths += 1
    print(f"The man in the centre for Splater runs round and takes out {player_2} and {player_3}.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[18] = ene_sym
    field1[33] = " "
    field[44] = " "
    field1[51] = " "
    field1[56] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} is switching from D to sanke side, trying to get a G.")
    print(f"\nHe gets one! {player_1} takes one out. Its one on ones")
    play_1_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[23] = ene_sym
    field1[7] = ' '
    field1[56] = play_sym 
    field1[18] = ' '
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} has lost the last player. ")
    play_1_deaths += 1
    print(f"{player_1} gets shot in the back! Hard lose for {team_name}")
    ene_team_score += 1
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_2_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[18] = ene_sym
    field1[33] = ene_sym
    field1[7] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} streak down field.")
    print(f"\n{player_1} trades out")
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{player_2} runs through and also trades out. Its a blood bath")
    play_2_kills += 1
    play_2_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[33] = " "
    field1[18] = " "
    field1[7] = ene_sym
    field1[54] = ' '
    field1[54] = ' '
    field1[59] = play_sym 
    field1[47] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} keeps low in the snake. The last Splatter player does not know where he is.")
    play_3_kills += 1
    print(f"\n{player_3} sprays him. Crazy move by {team_name}")
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
################################################ GAME 2_3 #######################################################
def GAME2_3_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[75] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} take it easy this point.")
    print(f"\nBoth teams are playing safe. Could be a long point")
    print(f"Both {player_1} takes out the snake player, but {player_3} is also walking off.")
    print(f"Both {player_2} goes to the centre brick")
    play_3_deaths += 1
    play_1_kills += 1
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[7] = ene_sym
    field2[10] = " "
    field2[75] = " "
    field2[77] = " "
    field2[45] = play_sym
    field2[67] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} snaps round and takes out the Splatter player at home.")
    print(f"\n{team_name} players did not see the move from Splatter to the back corner. ")
    play_2_deaths += 1
    print(f"{player_1} moves up to D3. {player_2} gets shot out. 1 on 1s")
    input("Press enter to continue")
    field2 = field_base
    field2[0] = ene_sym
    field2[7] = " "
    field2[3] = " "
    field2[67] = " "
    field2[45] = " "
    field2[54] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe back player for the Immortals tries to get into the god bunker...")
    print(f"\n{player_1} saw the move coming, and plastered the Immortal cenre player. Great work by {player_1}!!")
    play_1_kills += 1
    print(f"{player_3} pushes up to snake 1. He clips the pack of the dorito player. Great shot.")
    play_3_kills += 1
    input("Press enter to continue")  
    field2 = field_base
    field2[3] = " "
    field2[5] = ene_sym
    field2[61] = " "
    field2[54] = play_sym
    field2[59] = " "
    field2[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe last to players both load their last pods.")
    print(f"\n{player_1} moves to the 50 yard line. ")
    print(f"He gets the hit. Great shot from {player_1}. What an exciting point!")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_3_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[61] = play_sym
    field2[63] = play_sym +" "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} move to their 30")
    print(f"\n{player_3} shot off the break")
    play_3_deaths += 1
    play_2_kills += 1
    print(f"Looks like {player_2} got a shot on the snake player.")
    input("Press enter to continue")
    field2 = field_base
    field2[33] = ene_sym
    field2[5] = ene_sym
    field2[10] = " "
    field2[3] = " "
    field2[61] = play_sym 
    field2[59] = " "
    field2[63] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nSplatter have a man at the centre can, he is forcing {player_2} to play tight .")
    print(f"\n{player_1} has had enough of this and comes around to trade out")
    print(f"\n1 on 1s. {player_2} at the fifty brick, splatter in the snake corner")
    play_1_kills += 1
    play_1_deaths += 1
    input("Press enter to continue")
    field2 = field_base
    field2[33] = " "
    field2[5] = ene_sym
    field2[63] = " "
    field2[45] = play_sym
    field2[61] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nIts a snap shooting battle.")
    play_2_deaths += 1
    print(f"{player_2} gets hit on the hopper. Bad luck for {team_name}")
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_3_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[72] = play_sym
    field2[75] = play_sym 
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nSpread play by {team_name}.")
    print(f"\nOne player walking off for Immortals, but {player_1} and {player_3} both walk off")
    play_3_deaths += 1
    play_2_kills += 1
    play_1_deaths += 1
    print(f"{team_name} is in trouble here.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[7] = " "
    field2[10] = ene_sym
    field2[13] = ene_sym
    field2[72] = " "
    field2[75] = play_sym 
    field2[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nSplatter pushing up, guns rolling.")
    print(f"{player_2} gets blasted!!Point to Splatter")
    play_2_deaths += 1
    ene_team_score += 1
    input("Press enter to continue")
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    game2_3_play_choice()    
def GAME2_3_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[74] = play_sym 
    field2[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Doubles up the home.")
    print(f"\n{player_3} and {player_2} each get a G.{player_1} walks off too though")
    play_3_kills += 1
    play_2_kills += 1
    print(f"Now {team_name} slowly spread out.")
    play_1_deaths += 1
    input("Press enter to continue")
    field2 = field_base
    field2[10] = " "
    field2[3] = ene_sym
    field2[7] = " "
    field2[67] = " "
    field2[74] = " "
    field2[75] = " "
    field2[54] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} is in snake corner, {player_2} is in D3.")
    print(f"\n{player_2} is getting put in.")
    print(f"{player_3} gets a great shot from the corner.")
    print(f"{team_name} Takes the point")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd2.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_3_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[56] = play_sym
    field2[44] = play_sym 
    field2[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} rush the middle.")
    print(f"\nSplatter lose two players off the break!")
    play_1_kills += 1
    play_3_kills += 1
    print(f"{team_name} are beating the home bunker, keeping the last man in.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = " "
    field2[7] = " "
    field2[44] = " "
    field2[56] = play_sym
    field2[27] = play_sym 
    field2[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nThe last Splatter player is stuck at home.")
    print(f"\n{player_2} is going to bunker him out!")
    print(f"\nPoint to {team_name}")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()
def GAME2_3_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[10] = ene_sym
    field2[7] = ene_sym
    field2[54] = play_sym
    field2[44] = play_sym 
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} are going all out.")
    print(f"\n{player_3} and {player_1} both walk off.")
    play_1_deaths += 1
    play_3_deaths += 1
    print(f"{player_2} is all alone in the brick.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[7] = ene_sym
    field2[10] = ene_sym
    field2[27] = ene_sym
    field2[54] = " "
    field2[44] = play_sym 
    field2[59] = " " 
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_2} gets run down. Splatter with a huge win!")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game2_3_play_choice()

################################################ GAME 3_1 #######################################################
def GAME3_1_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    field1 = field_base
    play_count += 1
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} go short.")
    print(f"\nReavers ace back player removes {player_3}")
    play_3_deaths += 1
    print(f"Both {player_1} and {player_2} are dumping paint. Reavers lose the man in D3")
    play_2_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = " "
    field1[77] = " "
    field1[67] = play_sym
    field1[75] = " "
    field1[69] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} is moving up the D side.")
    print(f"\nThe Reavers smoke {player_2}. {player_1} is alone against 2")
    play_2_deaths += 1
    print(f"{player_1} wastes the man in the middle.")
    input("Press enter to continue")
    field1 = field_base
    field1[10] = ene_sym
    field1[33] = ene_sym
    field1[15] = " "
    field1[67] =" "
    field1[69] = " "
    field1[60] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} rolls off to hold off the attack")
    print(f"\nGreat shot by {player_1}!! 1 on 1s now")
    play_1_kills += 1
    print(f"{player_1} over snaps and gets wasted. First point to Reavers")
    play_1_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()
def GAME3_1_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} goes forth.")
    print(f"\n{player_3} shots one out, but {team_name} lose {player_1}")
    play_3_kills += 1
    play_1_deaths += 1
    print(f"Looks like {player_2} wants to move into {player_1}'s position.")
    input("Press enter to continue")
    field1 = field_base
    field1[10] = " "
    field1[15] = ene_sym
    field1[18] = ene_sym
    field1[77] = " "
    field1[63] = "  "
    field1[61] = play_sym
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} stays in snake 1 and is dumping paint.")
    print(f"\n{player_2} is real trouble")
    print(f"{player_2} is getting checked out by the ref. He has a hit")
    play_2_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[15] = " "
    field1[17] = ene_sym
    field1[30] = ene_sym
    field1[18] = " "
    field1[61] = " "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is shooting heads up and at the fifty, trying to get level the field.")
    play_3_deaths += 1
    print(f"{player_3} gets a hit on the shoulder. Unfortunate lose for {team_name}")
    ene_team_score += 1
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()
def GAME3_1_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} spreads the field")
    print(f"\nTwo players walking off for {team_name}. This is not a good start for them")
    play_1_deaths += 1
    play_3_deaths += 1
    print(f"{player_2} is all alone out there.")
    input("Press enter to continue")
    field1 = field_base
    field1[0] = ene_sym
    field1[5] = " "
    field1[7] = " "
    field1[72] = " "
    field1[75] = " "
    field1[77] = " "
    field1[42] = play_sym
    field1[44] = play_sym
    field1[41] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nReavers are moving up the field.")
    print(f"{player_2} had no chance there. Reavers win!!!")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()    
def GAME3_1_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Doubles the home bunker.")
    print(f"\n{player_1} walks off for {team_name}")
    play_1_deaths += 1
    print(f"Looks like {player_2} gets a kill, and darts out to the centre.")
    play_2_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[18] = " "
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[44] = play_sym
    field1[67] = "  "
    field1[74] = " "
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is under heavy fire.")
    print(f"\n{player_2} wraps and gets one. {team_name} is up on bodies.")
    print(f"\n{player_2} gets picked off, but {player_3}. {team_name} wins!!!")
    play_3_kills += 1
    play_2_kills += 1
    play_2_deaths += 1
    play_team_score += 1
    winsound.PlaySound('crowd2.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()
def GAME3_1_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go to the wall.")
    print(f"\nReavers have no idea what {team_name} is right now.")
    play_1_kills += 1
    print(f"{player_1} takes one out.")
    input("Press enter to continue")
    field1 = field_base
    field1[18] = " "
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[44] = play_sym
    field1[56] = play_sym
    field1[32] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is wrapping round and dumping paint at the can.")
    print(f"\n{player_2} is playing possum. He is waiting for his opportunity to get a kill.")
    print(f"\n{player_3} gets his man.")
    play_3_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[5] = " "
    field1[29] = ene_sym
    field1[52] = " "
    field1[56] = play_sym
    field1[51] = play_sym
    field1[52] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"{player_2} storms round and kills the final man. What a play from {team_name}")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()
def GAME3_1_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[15] = ene_sym
    field1[10] = ene_sym
    field1[18] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} runs down the field!!.")
    print(f"\n{player_3} gets trades his body")
    play_3_kills += 1
    play_3_deaths += 1
    play_1_deaths += 1
    print(f"{player_1} is picked off.")
    input("Press enter to continue")
    field1 = field_base
    field1[18] = ene_sym
    field1[15] = ene_sym
    field1[10] = " "
    field1[59] = " "
    field1[54] = " "
    field1[44] = play_sym 
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_2} is trying his best to take out the man in the can.")
    print(f"\nReavers dart down the field and shoot {player_2} down his back")
    play_2_deaths += 1
    print(f"Reavers take the point. What a game!")
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_2_play_choice()
################################################ GAME 3_2 #######################################################
def GAME3_2_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[75] = play_sym
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} goes for a defensive play.")
    print(f"\n{ene_name} have all three players survive the break")
    print(f"{player_3} gets shot out.")
    print(f"{player_2} gets a great shot on {ene_name}'s d side player'.")
    play_3_deaths += 1
    play_2_kills += 1
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[10] = " "
    field1[5] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[77] = " "
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nBoth teams are burning through paint")
    print(f"\n{player_2} runs round and trades out")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"{player_1} is in a 1 on 1 with the {ene_name} snake player in the corner")
    input("Press enter to continue")
    field1 = field_base
    field1[5] = ene_sym
    field1[32] = " "
    field1[75] = " "
    field1[67] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} loads his last pod.")
    play_1_deaths += 1
    print(f"{ene_name}'s last man gets a great on {player_1}. {ene_name} win")
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_2_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[61] = play_sym
    field1[63] = play_sym +" "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} push up.")
    print(f"\n{player_2} comes off for {team_name}.")
    play_2_deaths += 1
    print(f"{player_3} makes it into snake unseen")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[32] = ene_sym
    field1[10] = ene_sym
    field1[61] = play_sym
    field1[63] = " "
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} stitches up the man in the centre.")
    print(f"\n{player_1} is getting aks for a check from the ref. He is out")
    print(f"{player_3} takes out the man in the god bunker")
    play_3_kills += 1
    play_1_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[5] = ene_sym
    field1[10] = ene_sym
    field1[7] = " "
    field1[32] = " "
    field1[59] = play_sym
    field1[61] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} plays down the tape")
    print(f"{ene_name} send the D side man down the field to bunker {player_3}. Amazing work by {ene_name}")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdB00.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_2_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} go for the corners")
    print(f"{player_1} and {player_3} each get a kill. {team_name} in a good position here.")
    play_3_kills += 1
    play_1_kills += 1
    play_3_deaths += 1
    print(f"{player_3} gets a hit. Way too impatient.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[10] = " "
    field1[32] = ene_sym
    field1[72] = play_sym
    field1[75] = play_sym 
    field1[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe last player for {ene_name} is hammering {player_1}'s bunker. {player_2} is going to come and bunker him.'")
    print(f"{player_2} gets the last man. The point goes to {team_name}.")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()    
def GAME3_2_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Doubles up the back centre.")
    print(f"\n{player_1} takes out a player.")
    play_1_kills += 1
    print(f"Looks like {player_2} is moving up to the centre brick.{player_1} is moving to the D2")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = " "
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[67] = " "
    field1[74] = " " 
    field1[75] = " "
    field1[67] = play_sym
    field1[74] = play_sym 
    field1[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is under heavy fire.")
    print(f"\n{player_2} has a hit on his pack. {team_name} loses")
    print(f"{player_3} kills the corner player. Good work heads up")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_2_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[56] = play_sym
    field1[44] = play_sym 
    field1[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} Rushes the centre.")
    print(f"\n{player_2} comes round and trades out with the wall.")
    play_2_kills += 1
    play_2_deaths += 1
    print(f"{player_1} fills in the wall, while {player_3} dives into the snake")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = " "
    field[44] = " "
    field1[56] = " "
    field1[59] = " "
    field1[51] = ' '
    field1[44] = play_sym 
    field1[53] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} shoots an Immortal player, but gets picked off.")
    print(f"\nIts one on ones")
    play_3_kills += 1
    play_3_deaths += 1
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ' '
    field1[44] = play_sym 
    field1[53] = ' '
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_1} is wrapping hard. He has put the last Immortal player in")
    play_1_kills += 1
    print(f"{player_1} moves around and bunkers him! Good win for {team_name}")
    play_team_score += 1
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_2_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field1
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field1 = field_base
    field1[7] = ene_sym
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[54] = play_sym
    field1[44] = play_sym 
    field1[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} goes all the way down the field.")
    print(f"\n{player_1} gets shot out, but Immortals lose a player too")
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{player_2} is wrapping to get a better shot.")
    input("Press enter to continue")
    field1 = field_base
    field1[7] = ' '
    field1[10] = ene_sym
    field1[32] = ene_sym
    field1[54] = ' '
    field1[59] = ' '
    field1[44] = play_sym 
    field1[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field1[0]}   {field1[1]}   {field1[2]}  {field1[3]}   {field1[4]}   {field1[5]}  |")
    print (f"| {field1[6]}   {field1[7]}   {field1[8]}  {field1[9]}   {field1[10]}   {field1[11]}  |")
    print (f"| {field1[12]}   {field1[13]}   {field1[14]}  {field1[15]}   {field1[16]}   {field1[17]}  |")
    print (f"| {field1[18]}   {field1[19]}   {field1[20]}  {field1[21]}   {field1[22]}   {field1[23]}  |")
    print (f"| {field1[24]}   {field1[25]}   {field1[26]}  {field1[27]}   {field1[28]}   {field1[29]}  |")
    print (f"| {field1[30]}   {field1[31]}   {field1[32]}  {field1[33]}   {field1[34]}   {field1[35]}  |")
    print (f"| {field1[36]}   {field1[37]}   {field1[38]}  {field1[39]}   {field1[40]}   {field1[41]}  |")
    print (f"| {field1[42]}   {field1[43]}   {field1[44]}  {field1[45]}   {field1[46]}   {field1[47]}  |")
    print (f"| {field1[48]}   {field1[49]}   {field1[50]}  {field1[51]}   {field1[52]}   {field1[53]}  |")
    print (f"| {field1[54]}   {field1[55]}   {field1[56]}  {field1[57]}   {field1[58]}   {field1[59]}  |")
    print (f"| {field1[60]}   {field1[61]}   {field1[62]}  {field1[63]}   {field1[64]}   {field1[65]}  |")
    print (f"| {field1[66]}   {field1[67]}   {field1[68]}  {field1[69]}   {field1[70]}   {field1[71]}  |")
    print (f"| {field1[72]}   {field1[73]}   {field1[74]}  {field1[75]}   {field1[76]}   {field1[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} takes out the brick.")
    play_3_kills += 1
    print(f"\n{player_2} takes out the last player. Crazy move by {team_name}")
    play_2_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
################################################ GAME 3_3 #######################################################
def GAME3_3_def_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[75] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{team_name} keeps it tight.")
    print(f"\nBoth teams making their spots. Exactly the same breakout")
    print(f"Both {player_1} and {player_3} are looking to bump up.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = " "
    field2[18] = ene_sym
    field2[67] = " "
    field2[77] = " "
    field2[61] = play_sym
    field2[75] = play_sym
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\n{player_3} is in snake 1, while {player_1} is in d2. But an Immortals player is in D3")
    print(f"\nThe Immortals take out {player_2} out of home. {player_3} crosses over")
    play_2_deaths += 1
    print(f"{player_1} and {player_2} roll their guns, trying to get a kill.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[18] = ene_sym
    field2[61] = play_sym
    field2[75] = " "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThe back player for the Immortals tries to get into the god bunker...")
    print(f"\n{player_1} saw the move coming, and plastered the Immortal cenre player. Great work by {player_1}!!")
    play_1_kills += 1
    print(f"{player_3} pushes up to snake 1. He clips the pack of the dorito player. Great shot.")
    play_3_kills += 1
    input("Press enter to continue")  
    field2 = field_base
    field2[3] = " "
    field2[5] = ene_sym
    field2[61] = " "
    field2[54] = play_sym
    field2[59] = " "
    field2[47] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓_____________")
    print(f"\nThis has been a long point. Both teams are low on paint.")
    print(f"\n{player_3} is pounding the bunker. {player_1} moves to the brick!!")
    print(f"{player_1} finally gets a hit on the last player. What an exciting point!")
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_3_agg_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field2
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[61] = play_sym
    field2[63] = play_sym +" "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} go forward off the break")
    print(f"\nLooks like Immortals shoot out {player_1} off the break")
    play_1_deaths += 1
    print(f"Looks like {player_2} holding down the snake side, while{player_3} shots down the middle.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[61] = " "
    field2[63] = play_sym +" "
    field2[53] = " "
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} takes out the home player, now he is playing heads up.")
    print(f"\n{player_2} is having to play really tight at home")
    print(f"Immortals now at the 50 'X' line")
    play_3_kills += 1
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[7] = " "
    field2[5] = ene_sym
    field2[30] = ene_sym
    field2[63] = play_sym +" "
    field2[53] = play_sym
    field2[59] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_2} gets blasted down his back and {player_3} doesn't know where the {player_2} got shot from.")
    play_2_deaths += 1
    print(f"{player_3} gets shot out of the snake. Bad luck for {team_name}")
    play_3_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_3_spread_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[72] = play_sym
    field2[75] = play_sym 
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} go to the corners")
    print(f"\nOne player walking off for Immortals, but {player_1} and {player_3} also walk off")
    play_3_deaths += 1
    play_1_kills += 1
    play_1_deaths += 1
    print(f"{team_name} is in trouble here.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[5] = " "
    field2[7] = " "
    field2[27] = ene_sym
    field2[18] = ene_sym
    field2[72] = " "
    field2[75] = " " 
    field2[67] = play_sym 
    field2[77] = " "
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nThe Immortals moving up. {player_2} takes out the Dorito player. One on ones.")
    print(f"\nThe last Immortal player does not know where {player_2} is.")
    print(f"{player_2} spots him, and blasts him. 2 pack for {player_2}!!")
    play_2_kills += 2
    play_team_score += 1
    input("Press enter to continue")
    winsound.PlaySound('applause-01.wav', winsound.SND_FILENAME)
    game3_3_play_choice()    
def GAME3_3_double_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[67] = play_sym
    field2[74] = play_sym 
    field2[75] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Doubles up the home.")
    print(f"\n{player_3} takes out the wide player.")
    play_3_kills += 1
    print(f"And {player_2} dives into the D1, but he has been hit.")
    play_2_deaths += 1
    input("Press enter to continue")
    field2 = field_base
    field2[5] = " "
    field2[7] = ene_sym
    field2[3] = " "
    field2[18] = ene_sym
    field2[67] = " "
    field2[74] = " "
    field2[75] = " "
    field2[54] = play_sym
    field2[77] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_3} is in snake corner, {player_1} is in D3.")
    print(f"\n{player_1} snap shots guy in the mini wall.")
    print(f"{player_3} smokes the last player in D3!!")
    print(f"{team_name} Takes the point")
    play_3_kills += 1
    play_1_kills += 1
    play_team_score += 1
    winsound.PlaySound('crowd2.wav.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_3_centre_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[56] = play_sym
    field2[44] = play_sym 
    field2[51] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} are all heading up the pipe.")
    print(f"\nImmortals lose two players off the break!")
    play_1_kills += 1
    play_2_kills += 1
    print(f"{team_name} is spreading the field, looking for the last player.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = " "
    field2[7] = " "
    field2[56] = " "
    field2[44] = " " 
    field2[51] = " "
    field2[54] = play_sym
    field2[43] = play_sym 
    field2[41] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\nThe last Immortal player is stuck at home.")
    print(f"\n{player_3} comes round to finish him off")
    print(f"\nPoint to {team_name}")
    play_3_kills += 1
    play_team_score += 1
    winsound.PlaySound('applause-8.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()
def GAME3_3_hail_mary_play():
    winsound.PlaySound('Paintball2.wav', winsound.SND_FILENAME)
    global field
    global player_1 
    global player_2 
    global player_3 
    global team_name
    global play_count
    global play_1_kills 
    global play_2_kills 
    global play_3_kills 
    global play_1_deaths 
    global play_2_deaths 
    global play_3_deaths 
    global play_team_score
    global ene_team_score 
    global field_base
    play_count += 1
    field2 = field_base
    field2[3] = ene_sym
    field2[5] = ene_sym
    field2[7] = ene_sym
    field2[54] = play_sym
    field2[44] = play_sym 
    field2[59] = play_sym
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{team_name} Streak down the field!!.")
    print(f"\n{player_3} gets shot out, so does {player_1}")
    play_1_deaths += 1
    play_3_deaths += 1
    print(f"{player_2} is all alone in the brick.")
    input("Press enter to continue")
    field2 = field_base
    field2[3] = " "
    field2[5] = " "
    field2[7] = ene_sym
    field2[35] = ene_sym
    field2[12] = ene_sym
    field2[54] = " "
    field2[44] = play_sym 
    field2[59] = " " 
    print("_____________▓▓▓_____________")
    print (f"| {field2[0]}   {field2[1]}   {field2[2]}  {field2[3]}   {field2[4]}   {field2[5]}  |")
    print (f"| {field2[6]}   {field2[7]}   {field2[8]}  {field2[9]}   {field2[10]}   {field2[11]}  |")
    print (f"| {field2[12]}   {field2[13]}   {field2[14]}  {field2[15]}   {field2[16]}   {field2[17]}  |")
    print (f"| {field2[18]}   {field2[19]}   {field2[20]}  {field2[21]}   {field2[22]}   {field2[23]}  |")
    print (f"| {field2[24]}   {field2[25]}   {field2[26]}  {field2[27]}   {field2[28]}   {field2[29]}  |")
    print (f"| {field2[30]}   {field2[31]}   {field2[32]}  {field2[33]}   {field2[34]}   {field2[35]}  |")
    print (f"| {field2[36]}   {field2[37]}   {field2[38]}  {field2[39]}   {field2[40]}   {field2[41]}  |")
    print (f"| {field2[42]}   {field2[43]}   {field2[44]}  {field2[45]}   {field2[46]}   {field2[47]}  |")
    print (f"| {field2[48]}   {field2[49]}   {field2[50]}  {field2[51]}   {field2[52]}   {field2[53]}  |")
    print (f"| {field2[54]}   {field2[55]}   {field2[56]}  {field2[57]}   {field2[58]}   {field2[59]}  |")
    print (f"| {field2[60]}   {field2[61]}   {field2[62]}  {field2[63]}   {field2[64]}   {field2[65]}  |")
    print (f"| {field2[66]}   {field2[67]}   {field2[68]}  {field2[69]}   {field2[70]}   {field2[71]}  |")
    print (f"| {field2[72]}   {field2[73]}   {field2[74]}  {field2[75]}   {field2[76]}   {field2[77]}  |")
    print("_____________▓▓▓_____________")
    print(f"\n{player_2} gets run down. Immortals saw that play coming!")
    play_2_deaths += 1
    ene_team_score += 1
    winsound.PlaySound('laughter-2.wav', winsound.SND_FILENAME)
    input("Press enter to continue")
    game3_3_play_choice()

################################################ MENUS #######################################################
def game1_2_play_choice():
    field_base = field
    print(f"\nThis is the score for round 2\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME1_2_def_play()
    elif play == "2":
        GAME1_2_agg_play()
    elif play == "3":
        GAME1_2_spread_play()
    elif play == "4":
        GAME1_2_double_play()
    elif play == "5":
        GAME1_2_centre_play()
    elif play == "6":
        GAME1_2_hail_mary_play()
def game1_3_play_choice():
    field_base = field
    if play_team_score == 2:
       winG1() 
    elif ene_team_score == 2:
       lose() 
    else:
        print(f"\nThis is the score for round 3\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
        print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
        play = input("Which play would you like to do: ")
        while play not in ["1","2", "3", "4", "5", "6"]:
            play = input("Which play would you like to do: ")
        if play == "1":
            valid = True
            GAME1_3_def_play()
        elif play == "2":
            GAME1_3_agg_play()
        elif play == "3":
            GAME1_3_spread_play()
        elif play == "4":
            GAME1_3_double_play()
        elif play == "5":
            GAME1_3_centre_play()
        elif play == "6":
            GAME1_3_hail_mary_play()
def game2_2_play_choice():
    field_base = field
    print(f"\nThis is the score for round 2\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME2_2_def_play()
    elif play == "2":
        GAME2_2_agg_play()
    elif play == "3":
        GAME2_2_spread_play()
    elif play == "4":
        GAME2_2_double_play()
    elif play == "5":
        GAME2_2_centre_play()
    elif play == "6":
        GAME2_2_hail_mary_play()
def game2_3_play_choice():
    field_base = field
    if play_team_score == 2:
       winG2() 
    elif ene_team_score == 2:
       lose() 
    else:
        print(f"\nThis is the score for round 3\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
        print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
        play = input("Which play would you like to do: ")
        while play not in ["1","2", "3", "4", "5", "6"]:
            play = input("Which play would you like to do: ")
        if play == "1":
            valid = True
            GAME2_3_def_play()
        elif play == "2":
            GAME2_3_agg_play()
        elif play == "3":
            GAME2_3_spread_play()
        elif play == "4":
            GAME2_3_double_play()
        elif play == "5":
            GAME2_3_centre_play()
        elif play == "6":
            GAME2_3_hail_mary_play()
def game3_2_play_choice():
    field_base = field
    print(f"\nThis is the score for round 2\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME3_2_def_play()
    elif play == "2":
        GAME3_2_agg_play()
    elif play == "3":
        GAME3_2_spread_play()
    elif play == "4":
        GAME3_2_double_play()
    elif play == "5":
        GAME3_2_centre_play()
    elif play == "6":
        GAME3_2_hail_mary_play()
def game3_3_play_choice():
    field_base = field
    if play_team_score == 2:
       win() 
    elif ene_team_score == 2:
       lose() 
    else:
        print(f"\nThis is the score for round 3\n{team_name} = {play_team_score}\n{ene_name} = {ene_team_score}")
        print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
        play = input("Which play would you like to do: ")
        while play not in ["1","2", "3", "4", "5", "6"]:
            play = input("Which play would you like to do: ")
        if play == "1":
            valid = True
            GAME3_3_def_play()
        elif play == "2":
            GAME3_3_agg_play()
        elif play == "3":
            GAME3_3_spread_play()
        elif play == "4":
            GAME3_3_double_play()
        elif play == "5":
            GAME3_3_centre_play()
        elif play == "6":
            GAME3_3_hail_mary_play()


def player_register():
    global player_1
    global player_2
    global player_3
    global team_name
    player_1 = input("Please enter player 1's name: ")
    player_2 = input("Please enter player 2's name: ")
    player_3 = input("Please enter player 3's name: ")
    team_name = input("Please enter your team name: ")

def play_choice():
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME1_1_def_play()
    elif play == "2":
        GAME1_1_agg_play()
    elif play == "3":
        GAME1_1_spread_play()
    elif play == "4":
        GAME1_1_double_play()
    elif play == "5":
        GAME1_1_centre_play()
    elif play == "6":
        GAME1_1_hail_mary_play()
def play_choice2():
    global ene_name
    ene_name = "Splatter"
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME2_1_def_play()
    elif play == "2":
        GAME2_1_agg_play()
    elif play == "3":
        GAME2_1_spread_play()
    elif play == "4":
        GAME2_1_double_play()
    elif play == "5":
        GAME2_1_centre_play()
    elif play == "6":
        GAME2_1_hail_mary_play()
def play_choice3():
    global ene_name
    ene_name = "Reavers"
    print("\n1) = Defensive play\n2) = Aggresive play\n3) = Spread play\n4) = Double up play\n5) = Centre play\n6) = Hail Mary play")
    play = input("Which play would you like to do: ")
    while play not in ["1","2", "3", "4", "5", "6"]:
        play = input("Which play would you like to do: ")
    if play == "1":
        valid = True
        GAME3_1_def_play()
    elif play == "2":
        GAME3_1_agg_play()
    elif play == "3":
        GAME3_1_spread_play()
    elif play == "4":
        GAME3_1_double_play()
    elif play == "5":
        GAME3_1_centre_play()
    elif play == "6":
        GAME3_1_hail_mary_play()
    

def winG1 ():
    global ene_team_score
    global play_team_score
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    print(f"\n{team_name}\n{play_win*3} WINS!!! {play_win*3}")
    print(f"STATS\n{player_1}\nGAMES: {play_count}\nKILLS: {play_1_kills}\nDEATHS : {play_1_deaths}\nKILL RATIO : {play_1_kills / play_count}")
    print(f"\n{player_2}\nGAMES: {play_count}\nKILLS: {play_2_kills}\nDEATHS : {play_2_deaths}\nKILL RATIO : {play_2_kills / play_count}")
    print(f"\n{player_3}\nGAMES: {play_count}\nKILLS: {play_3_kills}\nDEATHS : {play_3_deaths}\nKILL RATIO : {play_3_kills / play_count}")
    ene_team_score = 0
    play_team_score = 0
    play_choice2()
def winG2 ():
    global ene_team_score
    global play_team_score
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    print(f"\n{team_name}\n{play_win*3} WINS!!! {play_win*3}")
    print(f"STATS\n{player_1}\nGAMES: {play_count}\nKILLS: {play_1_kills}\nDEATHS : {play_1_deaths}\nKILL RATIO : {play_1_kills / play_count}")
    print(f"\n{player_2}\nGAMES: {play_count}\nKILLS: {play_2_kills}\nDEATHS : {play_2_deaths}\nKILL RATIO : {play_2_kills / play_count}")
    print(f"\n{player_3}\nGAMES: {play_count}\nKILLS: {play_3_kills}\nDEATHS : {play_3_deaths}\nKILL RATIO : {play_3_kills / play_count}")
    ene_team_score = 0
    play_team_score = 0
    play_choice3()
def win ():
    winsound.PlaySound('crowd1.wav.wav', winsound.SND_FILENAME)
    print(f"\n{team_name}\n{play_win*3} WINS THE TOURNEMENT!!! {play_win*3}")
    print(f"\n{team_name}\n{play_win*3} WINS!!! {play_win*3}")
    print(f"STATS\n{player_1}\nGAMES: {play_count}\nKILLS: {play_1_kills}\nDEATHS : {play_1_deaths}\nKILL RATIO : {play_1_kills / play_count}")
    print(f"\n{player_2}\nGAMES: {play_count}\nKILLS: {play_2_kills}\nDEATHS : {play_2_deaths}\nKILL RATIO : {play_2_kills / play_count}")
    print(f"\n{player_3}\nGAMES: {play_count}\nKILLS: {play_3_kills}\nDEATHS : {play_3_deaths}\nKILL RATIO : {play_3_kills / play_count}")
    exit()   

def lose ():
    winsound.PlaySound('crowdBoo.wav.wav', winsound.SND_FILENAME)
    print(f"\n{team_name}\n{ene_sym*3} LOSES!!! {ene_sym*3}")
    print(f"\n{team_name}\n{play_win*3} WINS!!! {play_win*3}")
    print(f"STATS\n{player_1}\nGAMES: {play_count}\nKILLS: {play_1_kills}\nDEATHS : {play_1_deaths}\nKILL RATIO : {play_1_kills / play_count}")
    print(f"\n{player_2}\nGAMES: {play_count}\nKILLS: {play_2_kills}\nDEATHS : {play_2_deaths}\nKILL RATIO : {play_2_kills / play_count}")
    print(f"\n{player_3}\nGAMES: {play_count}\nKILLS: {play_3_kills}\nDEATHS : {play_3_deaths}\nKILL RATIO : {play_3_kills / play_count}")
    exit()

player_register()
play_choice()