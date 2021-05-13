from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import pandas as pd
import time

url = "https://stackoverflow.com/tags?tab=popular"
driver = webdriver.Chrome(executable_path=r"C:\Users\shrut\Downloads\chromedriver.exe")
driver.get(url)

def get_pop_tags():
    
        '''
        Collects the Popular Tags from StckoverFlow for the first 3 pages.
        Returns : A Pandas DataFrame
        
        '''
        
#       Tag Names
        tagname=[]
    
#       Tag Count
        tagcount=[]
    
#       Questions Asked Today
        q_asked_today=[]
    
#       Questions Asked This Week
        q_asked_this_week=[]
        
        k=0
        try:
            
            while(k<=2):
                
                
                soup = BeautifulSoup(driver.page_source,'html.parser')
                
#               Getting the Tag Names
                for tag in soup.findAll("a",class_="post-tag"):
                        tagname.append(tag.text)

#               Getting the Tag Count
                for i in soup.findAll("div",class_="mt-auto grid jc-space-between fs-caption fc-black-400"):

                        text=i.text.strip()
                        t_cnt=text[:text.find("quest")-1]
                        tagcount.append(t_cnt)

#               Getting the Count Questions of Questions asked Today and this Week
                for i in soup.findAll("div",class_="grid--cell s-anchors s-anchors__inherit"):

                        today=i.findAll("a")[0].text        
                        today=today[:today.find("asked")-1]
                        q_asked_today.append(int(today))

                        week=i.findAll("a")[1].text        
                        week=week[:week.find("this")-1]
                        q_asked_this_week.append(int(week))
                
                k+=1
                
#               Next Page
                nextpage = driver.find_element_by_link_text(str(k+1))
                time.sleep(2)
                nextpage.click()
                time.sleep(2)                
                                       
        except:
                pass
             
#       Creating a DataFrame
        df=pd.DataFrame({

            "Tag Name":tagname,
            "Tag Count":tagcount,
            "Asked Today":q_asked_today,
            "Asked This Week":q_asked_this_week

        })
        
        return df
        
        
df=get_pop_tags()
df.to_excel(r"C:\Users\shrut\Web_Scrapping_Projects\Stack_Overflow_Pop_Tags\PopularSOTags.xlsx")
print("Update Successful")