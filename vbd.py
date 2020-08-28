
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
from datetime import date

# Change the terms to show results
searchTerms = [ 'malaria cases' , 'dengue cases', 'japanese encephalitis cases' ,
				'malaria deaths' , 'dengue deaths', 'japanese encephalitis deaths' ,
				'malaria outbreak' , 'dengue outbreak', 'japanese encephalitis outbreak' ,
				'vector borne disease' ]    
# searchTerms = ['malaria cases']

# SET UP THE FILE to store data
filename="NEWS " + str(date.today()) +".csv"  
f=open(filename,"w", encoding = 'utf-8')
headers="Disease,Source,Statement,Content, Date, Link\n"
f.write(headers)
                
print('NATIONAL VECTOR BORNE DISEASE CONTROL PROGRAMME')
print('VECTOR BORNE DISEASE SEARCH-ENGINE')

pagesToGet= 1


#  TOI, Hindustan Times, Aaj Tak hindi, Indian Express , The Hindu , Finanacial Express , Hindu BussinessLine, NDTV , tribune ,  patrika, jagran


for term in searchTerms:
    #######################
    # Times of India
    ####################
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://timesofindia.indiatimes.com/topic/' + term +'/'+str(pageNo)
        print(url)
        

        try:
            page=requests.get(url)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(1)         

         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('li', attrs={'class': 'article'} )
        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links: 
            Disease = term.capitalize()
            Source = 'Times of India'
            Statement = j.find("meta", attrs={'itemprop': 'name'})['content'].strip()
            Link = j.find('meta', attrs={'itemprop': 'url'})['content'].strip()
            Content = j.find('div', attrs={'class': 'content'}).find('a').find('p').text.strip()
            Date = j.find('div', attrs={'class': 'content'}).find('a').find('span', attrs={'class' : 'meta'}).text.strip()
            
            f.write(Disease + "," +Source + "," + Statement.replace(',', '|') + "," + Content.replace(',', '|') + "," + Date.replace(',', '|') + "," + Link + "\n")
     


    # # # #######################
    # # # Hindustan Times
    # # # #######################
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.hindustantimes.com/search?q='+ term #+ "&pageno=" +str(pageNo)
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(1)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class': 'media-body'} )

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links: 
            Disease = term.capitalize()
            Source = 'Hindustan Times'
            if(j.find('div', attrs={'class': 'media-heading'})):
                Statement = j.find('div', attrs={'class': 'media-heading'}).find("a").text.strip()
            else:
                continue
            if (j.find('div', attrs={'class': 'media-heading'})):
                Link = j.find('div', attrs={'class': 'media-heading'}).find("a")['href'].strip()
            else:
                Link = " "
            if(j.find('div', attrs={'class': 'para-txt'})):
                Content = j.find('div', attrs={'class': 'para-txt'}).text.strip()
            else:
                Content= " "
            if(j.find('span', attrs={'class': 'time-dt'})):
                Date = j.find('span', attrs={'class': 'time-dt'}).text.strip()
            else:
                Date = " "
            # print(Source, Statement, Link, Content, Date)
            f.write(Disease + "," + Source + "," +  Statement.replace(',', '|') + "," + Content.replace(',', '|') + "," + Date.replace(',', '|') + "," + Link + "\n")
     

    # # #######################
    # # Aaj Tak HOINDIII
    # # #######################
    pagesToGet = 2
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://aajtak.intoday.in/topic/'+ term + "-page-"+ str(pageNo) + ".html"
        print(url)
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url)#,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(1)         
        # print(page.text)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class': 'scc_kv_st'} )

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links: 
            Disease = term.capitalize()
            Source = 'AAJ TAK HINDI'
            Statement = j.find('div', attrs={'class': 'scc_kv_all'}).find('h3').find("a").text
            Link = j.find('div', attrs={'class': 'scc_kv_all'}).find('h3').find("a")['href'].strip()
            Content = j.find('span', attrs={'class':'scc_st'}).text
            Date = j.find('div', attrs={'class': 'scc_kv_all'}).find('cite').text
            
            # print(Source, Statement, Link, Content, Date)
            f.write(Disease + "," + Source + "," +  ' '.join(Statement.replace(',', ' ').split()) + "," + ' '.join(Content.replace(',', ' ').split()) + "," + Date.replace(',', ' ') + "," + Link + "\n")

    # # #######################
    # # INdian Express
    # # #######################
    pagesToGet = 2
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://indianexpress.com/?s='+ term
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(1)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class': 'details'} )

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links: 
            Disease = term.capitalize()
            Source = 'Indian Express'
            Statement = j.find('h3').find('a').text.strip()
            Link = j.find('h3').find("a")['href'].strip()
            Content = j.find('p').text.strip()
            Date = j.find('time').text.split(';')[-1].strip()
            
            # print(Source, Statement, Link, Content, Date)
            f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

    # # #######################
    # # THE HINDU
    # # #######################
    pagesToGet = 2
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.thehindu.com/search/?q=' + term + '&order=DESC&sort=publishdate'
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(1)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class': 'story-card-news'} )

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links:
            Disease = term.capitalize()
            Source = 'The Hindu'
            Statement = j.find("a", attrs={'class' : 'story-card75x1-text'}).text.strip()
            Link = j.find("a", attrs={'class' : 'story-card75x1-text'})['href']
            Content = j.find('span', attrs={'class': 'light-gray-color'}).text.strip()
            Date = j.find('span', attrs={'class': ''}).find('span', attrs={'class' : 'dateline'}).text.strip()
            
            # print( Source, Statement, Link, Content, Date)
            f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")
    

        # # #######################
	    # # NDTV NEWS
	    # # #######################
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.ndtv.com/search?searchtext=' + term
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('li')

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links:
            # print(j.get('style'))
            # print(j)
            if j.get('style') == "padding: 5px;":
	            try:
		            Disease = term.capitalize()
		            Source = 'NDTV NEWS'
		            Statement = j.find("p", attrs={'class' : 'header fbld'}).find('a')['title'].strip()
		            Link = j.find("p", attrs={'class' : 'header fbld'}).find('a')['href'].strip()
		            Content = j.find('p', attrs={'class': 'intro'}).text.strip()
		            Date = j.find('p', attrs={'class': 'list_dateline'}).text.split('|')[2]
		            f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")
	            except:
		            continue


		
    	# # #######################
	    # #  The Hindu BussinessLine
	    # # #######################
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.thehindubusinessline.com/search/?q='+term+'&order=DESC&sort=publishdate'
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class' : 'col-sm-9 col-sm-8'})

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links:
	        Disease = term.capitalize()
	        Source = 'THE HINDU BUSSINESSLINE'
	        Statement = j.find("h3").find('a').text.strip()
	        Link = j.find("h3").find('a')['href'].strip()
	        Content = j.find_all('a')[1].find('p', attrs={'class' : 'ltext hidden-xs'}).text.strip()
	        Date = j.find('span', attrs={'class': 'artdate'}).find('span').text.strip()
        	# print(Statement, Link, Date, Content)
        	f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

    
    ############################
    ## THE FINANCIAL EXPRESS
    #############################
    
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.financialexpress.com/?search_scope=1&s='+term
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class' : 'content-list'})

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links:
	        Disease = term.capitalize()
	        Source = 'THE FINANCIAL EXPRESS'
	        Statement = j.find("h3").find('a').text.strip()
	        Link = j.find("h3").find('a')['href'].strip()
	        Content = j.find("h4").text.strip()
	        Date = j.find('span', attrs={'class': 'byline'}).find('span').text.strip()
        	# print(Statement, Link, Date, Content)
        	f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")


    #############################
    ### THE TRIBUNE
    #############################
    
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        url = 'https://www.google.com/search?domains=www.tribuneindia.com&sitesearch=www.tribuneindia.com&q='+term
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class' : 'rc'})

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


        for j in links:
	        try :
		        Disease = term.capitalize()
		        Source = 'THE TRIBUNE'
		        Statement = j.find('div', attrs={'class' : 'r'}).find("a").find('h3').text.strip()
		        Link = j.find('div', attrs={'class' : 'r'}).find("a")['href'].strip()
		        Content = j.find('div', attrs={'class' : 's'}).find('div').find('span', attrs={'class' : 'st'}).text.strip()
		        Date = j.find('div', attrs={'class' : 's'}).find('div').find('span', attrs={'class' : 'st'}).find('span', attrs={'class' : 'f'}).text.strip()
	        	# print(Statement, Link, Date, Content)
	        	f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

	        except: 
	        	pass

	############################
    ### PATRIKA
    #############################
    
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        sterm = urllib.parse.quote_plus(term)

        url = 'https://www.google.com/search?q='+sterm+'+site:www.patrika.com&domains=www.patrika.com&source=lnms&tbm=nws'
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class' : 'dbsr'})

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")
        # print(links)

        for j in links:
        
	        Disease = term.capitalize()
	        Source = 'PATRIKA'
	        Statement = j.find('div').find('div', attrs={'class' : 'hI5pFf'}).find('div', attrs={'class' : 'JheGif nDgy9d'}).text.strip()
	        Link = j.find('a')['href'].strip()
	        Content = j.find('div').find('div', attrs={'class' : 'hI5pFf'}).find('div', attrs={'class' : 'yJHHTd'}).find('div', attrs={'class' : 'Y3v8qd'}).text.strip()
	        Date = j.find('div').find('div', attrs={'class' : 'hI5pFf'}).find('div', attrs={'class' : 'yJHHTd'}).find('div', attrs={'class' : 'wxp1Sb'}).find('span', attrs={'class' : 'YCV9ed isfR2'}).find('span', attrs={'class' : 'WG9SHc'}).find('span').text.strip()
        	# print(Statement, Link, Date, Content)
        	f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

    #############################
    # ### JAGRAN
    # #############################
    
    pagesToGet = 1
    for pageNo in range(1,pagesToGet+1):
        print('processing page :', pageNo)
        # term = urllib.parse.quote_plus(term)

        url = 'https://www.jagran.com/search/'+term
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


        try:
            page=requests.get(url,headers=headers)                           
        
        except Exception as e:                                   # this describes what to do if an exception is thrown
            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
            continue 

         # Wait for 2 seconds 
        time.sleep(2)         
        print(page)
         # Get page links 
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all('div', attrs={'class' : 'protxt fr'})

        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")
        # print(links)

        for j in links:
        
	        Disease = term.capitalize()
	        Source = 'JAGRAN'
	        Statement = j.find('h3').find('a').text.strip()
	        Link = j.find('h3').find('a')['href'].strip()
	        Content = j.find('p').find('a').text.strip()
	        Date = j.find('div', attrs={'class' : 'catBox'}).find('span', attrs={'class' : 'catDate'}).text.strip()
        	# print(Statement, Link, Date, Content)
        	f.write(Disease + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

	       





	    

print('\n MADE BY GAJANAN SUNIL GITTE. MIT LICENSE 2020')
time.sleep(2);
#  THE END
f.close()



# MIT License

# Copyright (c) 2020 Gajanan Gitte

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
