from turtle import *
import sys

def add(t1,t2):
	return (t1[0]+t2[0], t1[1]+t2[1])

def setpos(l,pos):
	for triomino in l:
		triomino[0] = add(triomino[0],pos)
		triomino[1] = add(triomino[1],pos)
	return l

def tile(n, absent_tile_pos):
	"""
	returns a list of triominoes such that the grid of 2^n x 2^n sans absent_tile_pos
	is tiled with these triominoes. A triomino is represented by the position 
	of the top left 2x2 square and the tile that is absent from the 2x2 square
	enclosed by the triomino
	"""
	if (n == 1):
		return [[(0,0), absent_tile_pos]]
	
	# find out in which quadrant the absent tile lies
	if (absent_tile_pos[0] < 2**(n-1) and absent_tile_pos[1] < 2**(n-1)):
		# first quadrant
		return ( tile(n-1,absent_tile_pos) + 
				setpos(tile(n-1,(0,0)),(2**(n-1),2**(n-1))) +
				setpos(tile(n-1,(2**(n-1)-1,0)),(0,2**(n-1))) +
				setpos(tile(n-1,(0,2**(n-1)-1)),(2**(n-1),0)) +
				[[(2**(n-1)-1,2**(n-1)-1), (2**(n-1)-1,2**(n-1)-1)]] )
	elif (absent_tile_pos[0] >= 2**(n-1) and absent_tile_pos[1] < 2**(n-1)):
		# second quadrant
		return (setpos(tile(n-1,(2**(n-1)-1,2**(n-1)-1)),(0,0)) + 
				setpos(tile(n-1,(0,0)),(2**(n-1),2**(n-1))) +
				setpos(tile(n-1,(2**(n-1)-1,0)),(0,2**(n-1))) +
				setpos(tile(n-1,add(absent_tile_pos,(-2**(n-1),0))),(2**(n-1),0)) +
				[[(2**(n-1)-1,2**(n-1)-1), (2**(n-1),2**(n-1)-1)]] )
	elif (absent_tile_pos[0] >= 2**(n-1) and absent_tile_pos[1] >= 2**(n-1)):
		# third quadrant
		return (setpos(tile(n-1,(2**(n-1)-1,2**(n-1)-1)),(0,0)) + 
				setpos(tile(n-1,add(absent_tile_pos,(-2**(n-1),-2**(n-1)))),(2**(n-1),2**(n-1))) +
				setpos(tile(n-1,(2**(n-1)-1,0)),(0,2**(n-1))) +
				setpos(tile(n-1,(0,2**(n-1)-1)),(2**(n-1),0)) +
				[[(2**(n-1)-1,2**(n-1)-1), (2**(n-1),2**(n-1))]] )
	elif (absent_tile_pos[0] < 2**(n-1) and absent_tile_pos[1] >= 2**(n-1)):
		# fourth quadrant
		return (setpos(tile(n-1,(2**(n-1)-1,2**(n-1)-1)),(0,0)) + 
				setpos(tile(n-1,(0,0)),(2**(n-1),2**(n-1))) +
				setpos(tile(n-1,add(absent_tile_pos,(0,-2**(n-1)))),(0,2**(n-1))) +
				setpos(tile(n-1,(0,2**(n-1)-1)),(2**(n-1),0)) +
				[[(2**(n-1)-1,2**(n-1)-1), (2**(n-1)-1,2**(n-1))]] )

def render_triomino(triomino):
	
	pu()
	goto(triomino[0][0]*10,-triomino[0][1]*10)
	pd()
	if (triomino[1][0] > triomino[0][0] and triomino[1][1] > triomino[0][1]):
		#  _____
		# |     |
		# |   __|
		# |  |
		# |__|
		#
		seth(0)
		fd(20)
		rt(90)
		fd(10)
		rt(90)
		fd(10)
		lt(90)
		fd(10)
		rt(90)
		fd(10)
		rt(90)
		fd(20)
	elif (triomino[1][0] > triomino[0][0] and triomino[1][1] == triomino[0][1]):
		#  __
		# |  |  
		# |  |__
		# |     |
		# |_____|
		#
		seth(0)
		fd(10)
		rt(90)
		fd(10)
		lt(90)
		fd(10)
		rt(90)
		fd(10)
		rt(90)
		fd(20)
		rt(90)
		fd(20)
	elif (triomino[1][0] == triomino[0][0] and triomino[1][1] > triomino[0][1]):
		#  _____
		# |     |
		# |__   |
		#    |  |
		#    |__|
		#
		seth(0)
		fd(20)
		rt(90)
		fd(20)
		rt(90)
		fd(10)
		rt(90)
		fd(10)
		lt(90)
		fd(10)
		rt(90)
		fd(10)	
	elif (triomino[1][0] == triomino[0][0] and triomino[1][1] == triomino[0][1]):
		#     __ 
		#    |  |
		#  __|  |
		# |     |
		# |_____|
		#
		seth(0)
		pu()
		fd(10)
		pd()
		fd(10)
		rt(90)
		fd(20)
		rt(90)
		fd(20)
		rt(90)
		fd(10)
		rt(90)
		fd(10)
		lt(90)
		fd(10)

def render_triominoes(triominoes):
	
	for triomino in triominoes:
		render_triomino(triomino)

def render_rmsq(rmsq):
	
	pu()
	goto(rmsq[0]*10, -rmsq[1]*10)
	pd()
	begin_fill()
	seth(0)
	for i in range(4):
		fd(10)
		rt(90)
	end_fill()

speed('fastest')
ht()
rmsq = int(sys.argv[2]),int(sys.argv[3])
tiles = tile(int(sys.argv[1]),rmsq)
print(tiles)
render_rmsq(rmsq)
render_triominoes(tiles)
done()
