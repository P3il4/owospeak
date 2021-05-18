import os
import time
import random
try:
	import keyboard
	from win32api import GetKeyState 
	from win32con import VK_CAPITAL
except ImportError:
	print('press any key to install dependencies')
	os.system('pause')
	os.system('pip install -r requirements.txt --user')
	import keyboard
	from win32api import GetKeyState 
	from win32con import VK_CAPITAL

random.seed()

to_record = ['enter', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

enter_press = [
	'UwU',
	'OwO',
	'>w<',
	'-w-',
	';w;'
]

dupe_set = False

## how it should work:
# capture key
# analyze typed text
# return (type) modified text
# made by SharkOfGod#8424
'''

	current owo-config:
	
	on enter press 50% chance pick a random string from enter_press and append it before the enter

	r and l -> w

	after pressing space 33% chance of duplicating prev char (h-hello)

	x -> ks

	c -> k


'''


# keyname = actual key
# keyname_c(heck) = key for checking
def on_press(key):
	global dupe_set
	keyname = key.name
	keyname_c = key.name.lower()

	if keyname_c == 'enter':
		if random.randint(1, 2) == 1:
			keyboard.write(' ' + enter_press[random.randint(0, len(enter_press)-1)])

	if keyname_c == 'r' or keyname_c == 'l':
		keyname = 'w'

	if keyname_c == 'x':
		keyname = 'k'

	if keyname_c == 'c':
		keyname = 'k'

	if keyname == 'space':
		dupe_set = True
	elif dupe_set:
		if random.randint(1, 3) == 1:
			keyboard.write(keyname[0] + '-')
		dupe_set = False

	if keyname_c == 'x':
		keyboard.write('k')
		keyname = 's'

	if keyname.lower() != keyname or keyboard.is_pressed('shift') or GetKeyState(VK_CAPITAL):
		if GetKeyState(VK_CAPITAL):
			keyboard.press_and_release(keyname.lower())
		else:
			keyboard.press_and_release('shift+'+keyname.lower())
	else:
		keyboard.press_and_release(keyname)

for keys in to_record:
	keyboard.on_press_key(keys, on_press, suppress=True)

print('owospeak active!')
print('press any key to exit\n')

os.system('pause')