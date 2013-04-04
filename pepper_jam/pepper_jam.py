'''pepper_jam: Python library to extract revenue data from Pepper Jam
'''

__version__ = '1.0'
__author__ = 'Siddharth Saha (sidchilling@gmail.com)'

import requests
try:
    import json
except:
    import simplejson as json

class PepperJam(object):

    _BASE_URL = 'http://api.pepperjamnetwork.com/20120402/'
    _resource = 'publisher/report/transaction-details'
    _format = 'json'

    api_key = None
    start_date = None
    end_date = None

    def __init__(self, api_key, start_date, end_date):
	assert api_key, 'api key is missing'
	assert start_date, 'start date is missing'
	assert end_date, 'end date is missing'
	self.api_key = api_key
	self.start_date = start_date
	self.end_date = end_date
    
    def _make_url(self):
	return '%s%s' %(self._BASE_URL, self._resource)
    
    def _make_params(self):
	return {
		'startDate' : self.start_date.strftime('%Y-%m-%d'),
		'apiKey' : self.api_key,
		'endDate' : self.end_date.strftime('%Y-%m-%d'),
		'format' : self._format
	       }

    def get(self):
	'''This method needs to be called to get the revenue report
	Returns data in the format - 
	{
	    '<advertiser-id>' : {
		'advertiser-name' : '<advertiser-name>',
		'commission-amount' : <commission-amount-in-cents>
	    }
	}
		
	'''
	r = requests.get(url = self._make_url(), params = self._make_params())
	if r.ok:
	    content = json.loads(r.content)
	    if 'data' in content:
		res = {}
		for transaction in content.get('data'):
		    if transaction.get('program_id') in res:
			res[transaction.get('program_id')]['commission-amount'] = \
				res[transaction.get('program_id')]['commission-amount'] + \
				int(float(transaction.get('commission')) * 100)
		    else:
			res[transaction.get('program_id')] = {
				'advertiser-name' : transaction.get('program_name'),
				'commission-amount' : int(float(transaction.get('commission')) * 100)
				}
		return res
	    else:
		raise Exception('error in getting data from pepper jam')
	else:
	    raise Exception('cannot connect to pepper jam')
	
