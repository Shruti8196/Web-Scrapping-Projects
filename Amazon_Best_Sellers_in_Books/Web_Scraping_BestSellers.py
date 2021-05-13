from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def job():
    
    #Scrapping the top 50 best sellers books from amazon
    site = "https://www.amazon.in/gp/bestsellers/books"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    
    #Collecting record for each book
    rank = []
    name = []
    price = []
    rating = []
    num_ratings = []

    for i in soup.find_all("div", class_="a-section a-spacing-none aok-relative"):

        #Rank
        rank.append(int(i.find("span", class_="zg-badge-text").string[1:]))
        
        #Getting the title of the book
        name.append(i.find("img", alt=True)['alt'])
        
        #Fetching Price
        price.append(i.find("span", class_="p13n-sc-price").text)
        
        #Getting individual rating
        r = i.find("span", class_="a-icon-alt")
        
        #Finding total no. of ratings received for each book
        n_r = i.find("a", class_="a-size-small a-link-normal")
        
        
        if n_r == None: #If data not available
            num_ratings.append(n_r)
        else:
            val= i.find("a", class_="a-size-small a-link-normal").text
            val= val.replace(',','')
            num_ratings.append(int(val))
            
        if r == None: #If data not available
            rating.append(r)
        else:
            rating.append(float(r.text[:4]))
    
    #Putting the data collected into an Excel(.xlsx) file
    Top_50_BestSellers=pd.DataFrame({
    "Rank":rank,
    "Book Title":name,
    "Price":price,
    "Rating":rating,
    "#Num of Ratings":num_ratings

        })
    Top_50_BestSellers.set_index("Rank",inplace=True)
    Top_50_BestSellers.to_excel(r"C:\Users\shrut\Web_Scrapping_Projects\Amazon_Best_Sellers_in_Books\Top_50_BestSellers.xlsx")

    print("Update Successful")

job()
