---
{"dg-publish":true,"permalink":"/cg-oei-re/bits/game-mechanics/game-notes/"}
---


- using a state machine.


The player obj will just be one thing. Gamma, Nea, Honey, and Constantine will all be states, and the shift will be another state
vG= variable gamma just so we are clear this is an ariable
Player obj is ALWAYS in state G, N, H or C.
By default:
> {
> 	Default 
> 	set var vG = true
> }

Ex:
> if key_1 pressed, state = G{
> 	If state = G{
> 		Set var vG = true 
> 			# this is for dialogue purposes and determining who is first in party
> 			}
> 	# Code for her stats ie
	var spd = 10;
	# etc
	}
	If key_2 pressed, state = N{
		set var vN = true;
		# stats here
	}

Make sure all variables start with ‘v(char symbol)’ to differentiate it from the state. (Ie if G = true…)

Also 
> if state inair{
> 	# code to preform the air attacks
> }
> If state dash {
> 	# dash attack code
> 	}

Another state. SHIFT.


Var for shift is s(char)
IF key tab pressed, enter shift{
> # enter shift mode here 
> 
	If state = sG, {
> 	# check character
> 	# if player = Gamma then
> 		code for Gamma’s state here
> 		Gun mechanic goes here
> 	}
> 	
> 	if state = sN{
> 	# if player = Nea then
> 		Code of Nea’s shift state
> 	}
> }

Etc etc.