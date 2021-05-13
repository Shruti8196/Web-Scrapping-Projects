# Scrapping the Amazon Best Sellers in Books

## Table of Contents

1. [Overview](#overview)
2. [Libraries Used](#libraries-used)
3. [Tableau Dashboard](#tableau-dashboard)

## Overview

This project aims at fetching 50 Amazon Best Sellers in Books. There is an application inside the dist folder which on double click executes the script and updates the file
that contains the information collected on books.

The url used is- 

https://www.amazon.in/gp/bestsellers/books

![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Amazon_Best_Sellers_in_Books/Amazon%20Best%20Sellers.jpg)


**Data Collected Contains-**

1. Rank
2. Book Title
3. Ratings out of 5
4. #Num of Ratings Received

The data is collected into an excel file.
![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Amazon_Best_Sellers_in_Books/Excel_Data.jpg)

## Libraries Used

1. Beautiful Soup - For getting data out of the webpage.
2. UrlLib - For URL Handling
3. Pandas - For saving the data into file.

## Tableau Dashboard

The data collected was connected as a data source to tableau.

(May 2021)
![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Amazon_Best_Sellers_in_Books/Dashboard(May-2021).jpg)

