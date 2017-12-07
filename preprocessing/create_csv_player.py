#!/usr/bin/python

import chess;
import chess.pgn;
import chess.uci;
import sys, getopt

player_name="none"

def main(argv):
   global player_name

   command="create_csv_player.py -n <player_name> -| eg. create_csv_player.py 2.pgn -n karpov"
   try:
      opts, args = getopt.getopt(argv,"h:n:")
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
      elif opt in ("-n"):
         player_name = arg
      else:
         print('Invalid argument:', opt)
         sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])

def write_with_comma_w(str):
   file_white.write("," + unicode(str));
   return;

def write_with_comma_b(str):
   file_black.write("," + unicode(str));
   return;

def write_w(str):
   file_white.write(str);
   return;

def write_b(str):
   file_black.write(str);
   return;

pgn = open("/apps/chess/players/output/" + player_name + ".pgn");
file_white = open("output/chess_white_" + player_name + ".csv", 'w');
file_black = open("output/chess_black_" + player_name + ".csv", 'w');

engine = chess.uci.popen_engine("/usr/games/stockfish");
engine.uci();
print(engine.name);
print(engine.author);
print("\n");

write_w("Event,Site,Date,Round,Player,Colour,Result,Elo,ECO");
write_b("Event,Site,Date,Round,Player,Colour,Result,Elo,ECO");

write_with_comma_w("after_10_steps_no_queen,after_10_steps_pawn_sacrifices,after_10_steps_piece_sacrifices,after_10_steps_rook_sacrifices,after_10_steps_bishop_sacrifices,after_10_steps_knight_sacrifices");
write_with_comma_b("after_10_steps_no_queen,after_10_steps_pawn_sacrifices,after_10_steps_piece_sacrifices,after_10_steps_rook_sacrifices,after_10_steps_bishop_sacrifices,after_10_steps_knight_sacrifices");

write_with_comma_w("after_20_steps_no_queen,after_20_steps_pawn_sacrifices,after_20_steps_piece_sacrifices,after_20_steps_rook_sacrifices,after_20_steps_bishop_sacrifices,after_20_steps_knight_sacrifices");
write_with_comma_b("after_20_steps_no_queen,after_20_steps_pawn_sacrifices,after_20_steps_piece_sacrifices,after_20_steps_rook_sacrifices,after_20_steps_bishop_sacrifices,after_20_steps_knight_sacrifices");

#write_with_comma_w("after_30_steps_no_queen,after_30_steps_pawn_sacrifices,after_30_steps_piece_sacrifices,after_30_steps_rook_sacrifices,after_30_steps_bishop_sacrifices,after_30_steps_knight_sacrifices");
#write_with_comma_b("after_30_steps_no_queen,after_30_steps_pawn_sacrifices,after_30_steps_piece_sacrifices,after_30_steps_rook_sacrifices,after_30_steps_bishop_sacrifices,after_30_steps_knight_sacrifices");

write_with_comma_w("number_of_checks,after_10_steps_king_castled,after_20_steps_king_castled,number_of_attacks_on_center_before_step_20");
write_with_comma_b("number_of_checks,after_10_steps_king_castled,after_20_steps_king_castled,number_of_attacks_on_center_before_step_20");

write_with_comma_w("king_moves_before_step_20,queen_moves_before_step_20,bishop_moves_before_step_20,knight_moves_before_step_20,rook_moves_before_step_20,piece_moves_before_step_20,pawn_moves_before_step_20");
write_with_comma_b("king_moves_before_step_20,queen_moves_before_step_20,bishop_moves_before_step_20,knight_moves_before_step_20,rook_moves_before_step_20,piece_moves_before_step_20,pawn_moves_before_step_20");

write_w("\n");
write_b("\n");

for num in range(0,100000):
	white_checks=0;
	black_checks=0;
	white_castled=False;
	black_castled=False;
	white_castled_at_10=False;
	black_castled_at_10=False;
	white_castled_at_20=False;
	black_castled_at_20=False;
	white_center_attackers=0;
	black_center_attackers=0;
	white_center_attackers_until_20=0;
	black_center_attackers_until_20=0;
	white_king_moves_before_step_20=0;
	black_king_moves_before_step_20=0;
	white_queen_moves_before_step_20=0;
	black_queen_moves_before_step_20=0;
	white_bishop_moves_before_step_20=0;
	black_boshop_moves_before_step_20=0;
	white_knight_moves_before_step_20=0;
	black_knight_moves_before_step_20=0;
	white_rook_moves_before_step_20=0;
	black_rook_moves_before_step_20=0;
	white_pawn_moves_before_step_20=0;
	black_pawn_moves_before_step_20=0;
	white_piece_moves_before_step_20=0;
	black_piece_moves_before_step_20=0;
	w_pawn_moves=0
	w_piece_moves=0
	w_king_moves=0
	w_queen_moves=0
	w_knight_moves=0
	w_bishop_moves=0
	w_rook_moves=0
	b_pawn_moves=0
	b_piece_moves=0
	b_king_moves=0
	b_queen_moves=0
	b_knight_moves=0
	b_bishop_moves=0
	b_rook_moves=0
        w_pawn_moves_at_step_20=0
        w_piece_moves_at_step_20=0
        w_king_moves_at_step_20=0
        w_queen_moves_at_step_20=0
        w_knight_moves_at_step_20=0
        w_bishop_moves_at_step_20=0
        w_rook_moves_at_step_20=0
        b_pawn_moves_at_step_20=0
        b_piece_moves_at_step_20=0
        b_king_moves_at_step_20=0
        b_queen_moves_at_step_20=0
        b_knight_moves_at_step_20=0
        b_bishop_moves_at_step_20=0
        b_rook_moves_at_step_20=0

	game = chess.pgn.read_game(pgn);
	#print(game);
	node = game;
	board = node.board();
	#print("\n");

	exporter = chess.pgn.StringExporter(headers=False, variations=True, comments=False)
	pgn_string = game.accept(exporter)
	if "21." not in pgn_string: 
    	    continue

	write_w(game.headers.get('Event', 'N/A').replace(",", " ") + "," + game.headers.get('Site', 'N/A').replace(",", " ") + "," + game.headers.get('Date', 'N/A') + "," + game.headers.get('Round', 'N/A') + "," + game.headers["White"].replace(",", ".") + "," + "White" + "," + game.headers["Result"].split("-")[0] + "," + game.headers.get('WhiteElo', 'N/A') + "," + game.headers["ECO"]);
	write_b(game.headers.get('Event', 'N/A').replace(",", " ") + "," + game.headers.get('Site', 'N/A').replace(",", " ") + "," + game.headers.get('Date', 'N/A') + "," + game.headers.get('Round', 'N/A') + "," + game.headers["Black"].replace(",", ".") + "," + "Black" + "," + game.headers["Result"].split("-")[1] + "," + game.headers.get('BlackElo', 'N/A') + "," + game.headers["ECO"]);

	a = 0;
	while not node.is_end():
	    #print("White Turn: " + unicode(board.turn));
	    #print("Move pair Number: " + unicode(board.fullmove_number));
	    node = node.variation(0);
	    #print("Move: " + unicode(node.move));
	    #print("Check: " + unicode(board.is_check()));
	    #print("Checkmate: " + unicode(board.is_checkmate()));
	    #print("Game over: " + unicode(board.is_game_over()));
	    #print("can_claim_draw(): " + unicode(board.can_claim_draw()));
	    #print("Result: " + unicode(board.result()));
	    #print("Status: " + unicode(board.status()));
	    #print("is_castling: " + unicode(board.is_castling(node.move)));
	    #print("is_zeroing: " + unicode(bool(board.is_zeroing(node.move))));
	    #print("is_capture: " + unicode(bool(board.is_capture(node.move))));
	    #print("WHITE KING: " + unicode(board.king(chess.WHITE)));
	    #print("BLACK KING: " + unicode(board.king(chess.BLACK)));
	    engine.position(board);
	    #print("BLACK KING: " + unicode(board.king(chess.BLACK)));
	    #print("\n");
	    #print("\n");

	    symbol = board.piece_at(node.move.from_square).symbol();
	    if(symbol=='k'):
		b_king_moves = b_king_moves + 1;
	    elif(symbol=='q'):
		b_queen_moves = b_queen_moves + 1;
	    elif(symbol=='b'):
		b_bishop_moves = b_bishop_moves + 1;
	    elif(symbol=='n'):
		b_knight_moves = b_knight_moves + 1;
	    elif(symbol=='r'):
		b_rook_moves = b_rook_moves + 1;
	    elif(symbol=='p'):
		b_pawn_moves = b_pawn_moves + 1;
	    elif(symbol=='K'):
		w_king_moves = w_king_moves + 1;
	    elif(symbol=='Q'):
		w_queen_moves = w_queen_moves + 1;
	    elif(symbol=='B'):
		w_bishop_moves = w_bishop_moves + 1;
	    elif(symbol=='N'):
		w_knight_moves = w_knight_moves + 1;
	    elif(symbol=='R'):
		w_rook_moves = w_rook_moves + 1;
	    elif(symbol=='P'):
		w_pawn_moves = w_pawn_moves + 1;

	    if (board.is_castling(node.move)):
	        if (board.turn):
		    white_castled = True;
		else:
		    black_castled = True;
		
	    white_center_attackers = white_center_attackers + len(node.board().attackers(chess.WHITE, chess.D4)) + len(node.board().attackers(chess.WHITE, chess.D5)) + len(node.board().attackers(chess.WHITE, chess.E4)) + len(node.board().attackers(chess.WHITE, chess.E5))
	    black_center_attackers = black_center_attackers + len(node.board().attackers(chess.BLACK, chess.D4)) + len(node.board().attackers(chess.BLACK, chess.D5)) + len(node.board().attackers(chess.BLACK, chess.E4)) + len(node.board().attackers(chess.BLACK, chess.E5));

	    if (board.fullmove_number == 10 and board.turn) :
		write_with_comma_w(not bool(board.pieces(chess.QUEEN, chess.WHITE)));
		write_with_comma_w(8 - len(board.pieces(chess.PAWN, chess.WHITE)));
		write_with_comma_w(8 - (len(board.pieces(6, chess.WHITE)) + len(board.pieces(5, chess.WHITE)) + len(board.pieces(4, chess.WHITE)) + len(board.pieces(3, chess.WHITE)) + len(board.pieces(2, chess.WHITE))));
		write_with_comma_w(2 - len(board.pieces(4, chess.WHITE)));
		write_with_comma_w(2 - len(board.pieces(3, chess.WHITE)));
		write_with_comma_w(2 - len(board.pieces(2, chess.WHITE)));

		write_with_comma_b(not bool(board.pieces(chess.QUEEN, chess.BLACK)));
		write_with_comma_b(8 - len(board.pieces(chess.PAWN, chess.BLACK)));
		write_with_comma_b(8 - (len(board.pieces(6, chess.BLACK)) + len(board.pieces(5, chess.BLACK)) + len(board.pieces(4, chess.BLACK)) + len(board.pieces(3, chess.BLACK)) + len(board.pieces(2, chess.BLACK))));
		write_with_comma_b(2 - len(board.pieces(4, chess.BLACK)));
		write_with_comma_b(2 - len(board.pieces(3, chess.BLACK)));
		write_with_comma_b(2 - len(board.pieces(2, chess.BLACK)));

		white_castled_at_10=white_castled;
		black_castled_at_10=black_castled;

	    if (board.fullmove_number == 20 and board.turn) :
		write_with_comma_w(not bool(board.pieces(chess.QUEEN, chess.WHITE)));
		write_with_comma_w(8 - len(board.pieces(chess.PAWN, chess.WHITE)));
		write_with_comma_w(8 - (len(board.pieces(6, chess.WHITE)) + len(board.pieces(5, chess.WHITE)) + len(board.pieces(4, chess.WHITE)) + len(board.pieces(3, chess.WHITE)) + len(board.pieces(2, chess.WHITE))));
		write_with_comma_w(2 - len(board.pieces(4, chess.WHITE)));
		write_with_comma_w(2 - len(board.pieces(3, chess.WHITE)));
		write_with_comma_w(2 - len(board.pieces(2, chess.WHITE)));

		write_with_comma_b(not bool(board.pieces(chess.QUEEN, chess.BLACK)));
		write_with_comma_b(8 - len(board.pieces(chess.PAWN, chess.BLACK)));
		write_with_comma_b(8 - (len(board.pieces(6, chess.BLACK)) + len(board.pieces(5, chess.BLACK)) + len(board.pieces(4, chess.BLACK)) + len(board.pieces(3, chess.BLACK)) + len(board.pieces(2, chess.BLACK))));
		write_with_comma_b(2 - len(board.pieces(4, chess.BLACK)));
		write_with_comma_b(2 - len(board.pieces(3, chess.BLACK)));
		write_with_comma_b(2 - len(board.pieces(2, chess.BLACK)));

		white_castled_at_20=white_castled;
		black_castled_at_20=black_castled;

		white_center_attackers_until_20=white_center_attackers;
		black_center_attackers_until_20=black_center_attackers;

		w_pawn_moves_at_step_20=w_pawn_moves;
		w_piece_moves_at_step_20=w_king_moves+w_queen_moves+w_knight_moves+w_bishop_moves+w_rook_moves;
		w_king_moves_at_step_20=w_king_moves;
		w_queen_moves_at_step_20=w_queen_moves;
		w_knight_moves_at_step_20=w_knight_moves;
		w_bishop_moves_at_step_20=w_bishop_moves;
		w_rook_moves_at_step_20=w_rook_moves;
		b_pawn_moves_at_step_20=b_pawn_moves;
		b_piece_moves_at_step_20=b_king_moves+b_queen_moves+b_knight_moves+b_bishop_moves+b_rook_moves;
		b_king_moves_at_step_20=b_king_moves;
		b_queen_moves_at_step_20=b_queen_moves;
		b_knight_moves_at_step_20=b_knight_moves;
		b_bishop_moves_at_step_20=b_bishop_moves;
		b_rook_moves_at_step_20=b_rook_moves;

#	    if (board.fullmove_number == 30 and board.turn) :
#		write_with_comma_w(not bool(board.pieces(chess.QUEEN, chess.WHITE)));
#		write_with_comma_w(8 - len(board.pieces(chess.PAWN, chess.WHITE)));
#		write_with_comma_w(8 - (len(board.pieces(6, chess.WHITE)) + len(board.pieces(5, chess.WHITE)) + len(board.pieces(4, chess.WHITE)) + len(board.pieces(3, chess.WHITE)) + len(board.pieces(2, chess.WHITE))));
#		write_with_comma_w(2 - len(board.pieces(4, chess.WHITE)));
#		write_with_comma_w(2 - len(board.pieces(3, chess.WHITE)));
#		write_with_comma_w(2 - len(board.pieces(2, chess.WHITE)));

#		write_with_comma_b(not bool(board.pieces(chess.QUEEN, chess.BLACK)));
#		write_with_comma_b(8 - len(board.pieces(chess.PAWN, chess.BLACK)));
#		write_with_comma_b(8 - (len(board.pieces(6, chess.BLACK)) + len(board.pieces(5, chess.BLACK)) + len(board.pieces(4, chess.BLACK)) + len(board.pieces(3, chess.BLACK)) + len(board.pieces(2, chess.BLACK))));
#		write_with_comma_b(2 - len(board.pieces(4, chess.BLACK)));
#		write_with_comma_b(2 - len(board.pieces(3, chess.BLACK)));
#		write_with_comma_b(2 - len(board.pieces(2, chess.BLACK)));

	    #new board
	    board = node.board();
	    if (board.turn and board.is_check()):
		white_checks = white_checks + 1;
	    if ((not board.turn) and board.is_check()):
		black_checks = black_checks + 1;
	    #print(unicode(board));
	    a = a + 1;
	write_with_comma_w(white_checks);
	write_with_comma_w(white_castled_at_10);
	write_with_comma_w(white_castled_at_20);
	write_with_comma_w(white_center_attackers_until_20);
	write_with_comma_b(black_checks);
	write_with_comma_b(black_castled_at_10);
	write_with_comma_b(black_castled_at_20);
	write_with_comma_b(black_center_attackers_until_20);
	write_with_comma_w(w_king_moves_at_step_20);
	write_with_comma_w(w_queen_moves_at_step_20);
	write_with_comma_w(w_bishop_moves_at_step_20);
	write_with_comma_w(w_knight_moves_at_step_20);
	write_with_comma_w(w_rook_moves_at_step_20);
	write_with_comma_w(w_piece_moves_at_step_20);
	write_with_comma_w(w_pawn_moves_at_step_20);
	write_with_comma_b(b_king_moves_at_step_20);
	write_with_comma_b(b_queen_moves_at_step_20);
	write_with_comma_b(b_bishop_moves_at_step_20);
	write_with_comma_b(b_knight_moves_at_step_20);
	write_with_comma_b(b_rook_moves_at_step_20);
	write_with_comma_b(b_piece_moves_at_step_20);
	write_with_comma_b(b_pawn_moves_at_step_20);
	write_w("\n");
	write_b("\n");
	#print("\n");
	#print("Is checkmate: " + unicode(board.is_checkmate()));
	#print(board);
	#print("\n");

pgn.close();
file_white.close();
file_black.close();










