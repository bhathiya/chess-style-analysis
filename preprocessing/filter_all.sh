#!/bin/bash

./filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Anatoly -l Karpov, -i A. >> output/karpov.pgn
./filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Garry -l Kasparov, -i G. >> output/kasparov.pgn
./filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Peter -l Leko, -i P. >> output/leko.pgn
./filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Mikhail -l Tal, -i M. >> output/tal.pgn
./filter_pgn_by_player.py -p /other/millionbase-2.22.pgn -f Tigran -l Petrosian, -i T. >> output/petrosian.pgn
