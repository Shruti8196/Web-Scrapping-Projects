# Scrapping Stop Words in English

## Table of Contents

1. [Overview](#overview)
2. [Libraries Used](#libraries-used)

## Collecting Stop Words in English

This project aims at getting Stop Words in English Language. Stop words are a set of commonly used words in any language. For example, in English, “the”, “is” and “and”,
would easily qualify as stop words. In NLP and text mining applications, stop words are used to eliminate unimportant words, allowing applications to focus on the 
important words instead. Such words are often avoided by search engines. Though "stop words" usually refers to the most common words in a language, 
there is no single universal list of stop words

The url used is- 

https://www.ranks.nl/stopwords

![](https://github.com/Shruti8196/Web-Scrapping-Projects/blob/master/Scrapping%20Stop%20Words/Site.jpg)


**Data Collected Contains-**
A mixed list of stopwords containing-
1. Default English Stopwords
2. MySQL Stopwords
3. Google History Stopwords
4. Long List of Stopwords

The points mentioned above are the 4 tables in the site provided. The words from 4 of them might have common stop words, so we would drop the duplicates and finally save
the stopwords into a csv file.

## Libraries Used

1. Beautiful Soup - For fetching data out of the webpage.
2. Selenium - To go to the site.
3. Pandas - For saving the data into file.

