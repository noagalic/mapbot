## EU4-Player-Map-Creator ##

# What is it for?
  This was created to generate player maps, to help visualize the distribution of players, for the game EU4 on the Discord server "Paradox+".
  
# What does it do?
  player_map_creator.py takes a screenshot map from Europa Universalis 4 and removes countries not listed as player nations. (see example.png for example)
  
# How does it work?
  The program takes a list of countries (player_countries_list.txt) and finds their map color from the EU game files. It then scans an input screenshot map (F10 in-game screenshot) and removes pixels that are not included in the country list.
  
# What programming language?
  player_map_creator.py is written in Python 2.7.13 and uses the Image module. (which must be downloaded seperately)

# How do I run it?
  You need to have python version 2.7 installed first (https://www.python.org/download/releases/2.7/). Then, in the command shell, enter "pip install Image" to get the Image module. Navigate to whatever directory your program is saved in (using "cd something\something\something") and run it with the command ("python player_map_creator.py").
  
  Before running it you must modify some of the text files. You also need a map screenshot in the same directory as the program. The formatting of the text files are important, see formatting.txt.  You modify player_country_list.txt with the list of player countries you want.  In eu4_directory.txt you put you EU4 game directory.  In image_names.txt you put both the original map and the output map file names.
  
  Once you've modified these properly, run the program and you'll see your map. If you run into any errors contact me, Ghostowl657.
