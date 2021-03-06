#http://www.apilayer.net/api/live?access_key=0bf55c1bfb56b4ccc67bed85426233b2&format=1   #a look at the json object returned by the API
# Would need to code the response funciton according to the dialouge flow of the conversation workspace

from urllib.request import urlopen
import json



# ruppee to foreign currency
def currency_convertor(arg1, USD_currency, EUR_currency, DRM_currency,json_obj):  #arg1 in INR #set rest of the arguments as boolean contexts from the dataflow nodes

	result_USD = arg1/json_obj["quotes"]["USDINR"]

	if(USD_currency):
		result_USD = float("{0:.2f}".format(result_USD))
		return(str(result_USD) + " $")

	elif(EUR_currency):
		result_EUR = result_USD*json_obj["quotes"]["USDEUR"]
		result_EUR = float("{0:.2f}".format(result_EUR))
		return(str(result_EUR) + " Euros")

	elif(DRM_currency):
		result_DRM = result_USD*json_obj["quotes"]["USDAED"]
		return(str(result_DRM) + " Dirhams")



#foreign to indian
def currency_convertor2(USD_currency, EUR_currency, DRM_currency,json_obj): #arguments contain currency value.

	USD_INR_ratio = json_obj["quotes"]["USDINR"]

	if(USD_currency):
		return float("{0:.2f}".format(USD_currency * USD_INR_ratio))

	elif(EUR_currency):
		result_EUR = (EUR_currency/json_obj["quotes"]["USDEUR"])*USD_INR_ratio
		result_EUR = float("{0:.2f}".format(result_EUR))
		return (result_EUR)

	elif(DRM_currency):
		result_DRM = (DRM_currency/json_obj["quotes"]["USDAED"])*USD_INR_ratio
		return (result_DRM)



def trans_to(amount,to_cur,json_obj):
	if(to_cur == "euro"):
		return currency_convertor(amount,False,True,False,json_obj)

	if(to_cur == "dollar"):
		return currency_convertor(amount,True,False,False,json_obj)

	return amount

def translate(amount,from_cur,to_cur):


	access_key = "0bf55c1bfb56b4ccc67bed85426233b2" # 1000 requestsallowed per acess_key
	format = 1
	returned_json = urlopen("http://apilayer.net/api/live" + "?access_key=" + access_key + "&format")
	str_result = returned_json.read().decode('utf-8')
	json_obj = json.loads(str_result)


	if(from_cur == 'rupee'):
		return trans_to(amount,to_cur,json_obj)
	if(from_cur == "euro"):
		newAmount = currency_convertor2(False,amount,False,json_obj)
		return trans_to(newAmount,to_cur,json_obj)
	if(from_cur == "dollar"):
		newAmount = currency_convertor2(amount,False,False,json_obj)
		return trans_to(newAmount,to_cur,json_obj)
