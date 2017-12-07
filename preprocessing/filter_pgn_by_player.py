#!/usr/bin/python

import chess;
import chess.pgn;
import chess.uci;
import sys, getopt

player_firstname="Anatoly"
player_lastname="Karpov"
player_initials="A."
input_file="/other/millionbase-2.22.pgn"

def main(argv):
   global player_firstname
   global player_lastname
   global player_initials
   global input_file

   command="filter_pgn_by_player.py -p <input_file> -f <player_firstname> -l <player_lastname> -i <player_initials> | eg. filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Anatoly -l Karpov -i A."
   try:
      opts, args = getopt.getopt(argv,"h:p:f:l:i:")
   except getopt.GetoptError:
      print(command)
      sys.exit(2)
   if opts == []:
      print('Missing arguments. ' + command)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(command)
         sys.exit()
      elif opt in ("-p"):
         input_file = arg
      elif opt in ("-f"):
         player_firstname = arg
      elif opt in ("-l"):
         player_lastname = arg
      elif opt in ("-i"):
         player_initials = arg
      else:
         print('Invalid argument:', opt)
         sys.exit(2)

   #print('Input file is', input_file)
   #print('Player first name is', player_firstname)
   #print('Player last name is', player_lastname)
   #print('Player initials are', player_initials)

if __name__ == "__main__":
   main(sys.argv[1:])

#print("File", input_file)
pgn = open(input_file);

engine = chess.uci.popen_engine("/usr/games/stockfish");
engine.uci();

i = 0
j = 0
for num in range(0,7000000):
	game = chess.pgn.read_game(pgn)
	if player_lastname not in game.headers["White"] and player_lastname not in game.headers["Black"]:
		continue
	if player_lastname in game.headers["White"]:
		if player_initials not in game.headers["White"] and player_firstname not in game.headers["White"]:
			continue
	if player_lastname in game.headers["Black"]:
		if player_initials not in game.headers["Black"] and player_firstname not in game.headers["Black"]:
			continue
	print(game)
	node = game
	board = node.board()
	i = i + 1
	j = j + 1
	if j == 500:
		break
	print("\n");
pgn.close();










