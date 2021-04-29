from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

def scrape_SO_tags():
    
    '''Downloads a csv file that consist of colums:
    -Tag Names : Tag Names of the Popular Tags
    -Tag Count : Count of particular Tags
    -Asked_Today : Count of questions asked today with that tag
    -Asked_This_Week: Count of questions asked over a week with that tag
    '''
   
    site= "https://stackoverflow.com/tags?tab=popular"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    
    #Getting data into a dictionary
    dictionary={"Tag Names":[],"Tag_Count":[], "Asked_Today":[], "Asked_This_Week":[]}
    
    #Extracting The Popular Tags
    for tag in soup.find_all("a",class_="post-tag"): 
        dictionary["Tag Names"].append(tag.text)
    
    #Extracting The Counts
    for tag_count in soup.find_all("div",class_="mt-auto grid jc-space-between fs-caption fc-black-400"):
        
        
        x=tag_count.text
        string_split=x.split()

        #Getting the Tag_Count
        dictionary["Tag_Count"].append(int(string_split[0]))
        
        #Questions asked today with this tag
        dictionary["Asked_Today"].append((string_split[2]))
        
        #Questions asked over a week with this tag
        dictionary["Asked_This_Week"].append(int(string_split[5]))
 
    
    #Returning a DataFrame
    df=pd.DataFrame(dictionary)
    df.index+=1
    
    return df

df=scrape_SO_tags()
df.to_excel(r"C:\Users\shrut\Web_Scrapping_Projects\Stack_Overflow_Popular_Tags\PopularSOTags.xlsx")
print("Update Successful")