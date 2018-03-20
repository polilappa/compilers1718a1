
def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	c = words[pos]
	
	if (c == '0' or c == '1') and state == 'q0' :
		return 'HOUR_01'
	if c == '2' and state == 'q0':
		return 'HOUR_2'
	if (c >= '3' and c <= '9') and state == 'q0' :
		return 'HOUR_39'
	if (c >= '0' and c <= '9') and state == 'q1':
		return 'HOUR_09'
	if (c == '.' or c == ':') and state == 'q1':
		return 'SEPARATOR_1'
	if (c >= '0' and c <= '3') and state == 'q2':
		return 'HOUR_03'
	if (c == '.' or c == ':') and state == 'q2':
		return 'SEPARATOR_1'
	if c == '.' or c == ':' :
		return 'SEPARATOR'
	if (c >= '0' and c <= '5') and state == 'q4':
		return 'MINUTE_05'
	if (c >= '0' and c <= '9') and state == 'q5':
		return 'MINUTE_09'
	
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Modified
td = { 'q0':{ 'HOUR_01':'q1', 'HOUR_2':'q2', 'HOUR_39':'q3' },
       'q1':{ 'HOUR_09':'q3', 'SEPARATOR_1':'q4' },
       'q2':{ 'HOUR_03':'q3', 'SEPARATOR_1':'q4' },
       'q3':{ 'SEPARATOR':'q4' },
       'q4':{ 'MINUTE_05':'q5' },
       'q5':{ 'MINUTE_09':'q6' }
     } 


# the dictionary of accepting states and their
# corresponding token

# Modified
ad = { 'q6':'TIME_TOKEN' }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
