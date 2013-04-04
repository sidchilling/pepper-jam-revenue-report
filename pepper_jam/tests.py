'''This is the test file for the pepper jam library
'''

from datetime import datetime
from pprint import pprint
from pepper_jam import PepperJam

if __name__ == '__main__':
    api_key = '<your-api-key>'
    start_date = datetime.strptime('2012-05-01', '%Y-%m-%d')
    end_date = datetime.strptime('2013-04-04', '%Y-%m-%d')
    print 'start_date: %s' %(start_date.strftime('%d %b, %Y'))
    print 'end_date: %s' %(end_date.strftime('%d %b, %Y'))
    pepper_jam = PepperJam(api_key = api_key, start_date = start_date, 
	    end_date = end_date)

    pprint(pepper_jam.get())
