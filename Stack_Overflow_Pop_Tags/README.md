# Scrapping most popular Stack Overflow tags

## Table of Contents

1. [Overview](#overview)
2. [Libraries Used](#libraries-used)
3. [Tableau Story](#tableau-story)

## Overview

This project aims at fetching the most popular Stack Overflow tags. A tag is a keyword or label that categorizes your question with other, 
similar questions. Tags help others find your question and answer it. Few Examples of Tags are python, java, javascript etc.

The url used is- 

https://stackoverflow.com/tags?tab=popular

![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Stack_Overflow_Pop_Tags/SO_Site.jpg)


**Data Collected Contains-**

1. Tag Count
2. Count of Questions Asked Today with that particular Tag
3. Count of Questions Asked Throughout a Week with that particular Tag

The data is collected into an excel file.
![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Stack_Overflow_Pop_Tags/Excel_Data.jpg)

## Libraries Used

1. Beautiful Soup - For getting data out of the webpage.
2. Selenium - For Web Automation
3. UrlLib - For URL Handling
4. Pandas - For saving the data into file.

## Tableau Story

The data collected was connected as a data source to tableau.

Tag Count | Asked Today | Asked This Week
--------- | ----------- | ---------------
![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Stack_Overflow_Pop_Tags/Top%2010%20Highest%20Tag%20Counts(Tableau%20Story).jpg) | ![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Stack_Overflow_Pop_Tags/Top%2010%20Tags%20of%20the%20Day(Tableau%20Story).jpg) | ![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Stack_Overflow_Pop_Tags/Top%2010%20Tags%20of%20the%20Week(Tableau%20Story).jpg)
