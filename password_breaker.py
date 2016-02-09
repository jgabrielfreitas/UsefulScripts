import sys
from itertools import product
import time
import datetime
import zipfile

def refresh_line(message_to_show):
    sys.stdout.write(message_to_show + " \r")
    sys.stdout.flush()

# your_list = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%&*()_+={-}[]\|?/'
your_list = 'abcdefghijklmnopqrstuvwxyz' # test just letters, this reduce the time of processing, but decreases the chances
attempt_count = 0

# if you just clone the repo, type: get.zip

zip_path = raw_input("Type the zip path: ")
finish = False
start = time.time()
for length in range(17): # passwords with 16 characters
    to_attempt = product(your_list, repeat=length)
    for attempt in to_attempt:
        current_attempt = ''.join(attempt)
        #  start brutal force
        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(pwd=current_attempt)
            print('\nPassword found: ' + current_attempt)
            finish = True
            end = time.time()
            break
        except:
            refresh_line(' Trying: {0}'.format(current_attempt))
            attempt_count += 1

        if finish == True:
            break

print("Runtime: {0}".format(datetime.timedelta(seconds=end - start)))
print("Attempts: {0}".format(attempt_count))
