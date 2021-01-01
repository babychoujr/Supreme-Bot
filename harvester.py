import logging

from threading import Thread
from harvester import Harvester


logging.getLogger('harvester').setLevel(logging.CRITICAL)

#create a harvester instance
harvester = Harvester()

tokens = harvester.intercept_recaptcha_v2(
    domain = 'google.com',
    sitekey = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
)

#next, we run the server in a sepearate thread to keep from blocking rest of the program

server_thread = Thread(target = harvester.serve, daemon = True)

server_thread.start()

#launch a browser instance where we can solve the captchas
harvester.launch_browser()


try:
    while True:
        #block until we get captcha token
        token = tokens.get()
        print('We received a token: ', token)
except KeyboardInterrupt:
    print('Token not received')
