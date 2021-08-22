import sys
import string
import os
import random
import requests
from threading import Thread

os.system("title Imgur Scraper - Icmpoff")
GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[37m"
PURPLE = "\033[35m"

logo = '''
________                                ________                                        
____  _/______ __________ ____  __________  ___/__________________ _____________________
 __  / __  __ `__ \_  __ `/  / / /_  ___/____ \_  ___/_  ___/  __ `/__  __ \  _ \_  ___/
__/ /  _  / / / / /  /_/ // /_/ /_  /   ____/ // /__ _  /   / /_/ /__  /_/ /  __/  /    
/___/  /_/ /_/ /_/_\__, / \__,_/ /_/    /____/ \___/ /_/    \__,_/ _  .___/\___//_/     
                  /____/                                           /_/                   
'''
disclaimer = '''
                            Author: Icmpoff
                               Version: 0.1
############################### DISCLAIMER ################################
| All images are publicly available and are public. The parser simply     |
| generates random links and, if the image exists, downloads it.          |                             
###########################################################################
'''
print("{}{}".format(PURPLE,logo))
print("{}{}".format(RED, disclaimer))
print('{}Images will be download to /imgur_pics'.format(WHITE))
VALID_PATH = "imgur_pics"
if not os.path.exists(VALID_PATH):
	os.makedirs(VALID_PATH)
k = input('Enter the number of threads:')
k = int(k)
print('')

#
#
def scraper(ls):
	while True:
		try:
			random.shuffle(ls)
			img = ''.join([random.choice(ls) for x in range(5)])
			urrl = 'https://' + 'i.imgur.com' + '/' + img + '.jpg'
			response = requests.head(urrl, allow_redirects=False)
			response.raise_for_status()
			if response.status_code == 200:
				r = requests.get(urrl, stream=True)  # stream for partial download
				print('{} [VALID LINK FOUND]-{}'.format(GREEN, urrl))
				with open(os.path.join(VALID_PATH, img)+".jpg", 'bw') as f:
					for chunk in r.iter_content(8192):
						f.write(chunk)
			pass
		except requests.exceptions.HTTPError as err:
			print('NOT valid[-]:'+urrl)
			pass
ls = list(string.ascii_letters + string.digits)
for i in range(k):
    Thread(target=scraper, args=(ls,)).start()