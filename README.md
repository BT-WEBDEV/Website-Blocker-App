# Website-Blocker-App

Case Use: To block distracting websites during working hours of the day (IE: 8am-4pm). This is done by accessing the HOSTS file via Python.  Once accessed, the script modifies the HOSTS file by telling Windows to redirect desired URLS to the localhost, thus blocking the website. 

PLEASE READ THIS FIRST - This script does change the information on your HOSTS file locally on your machine. It is recommended that you create a backup of this file FIRST before using this script. 

To Run The Script: 

1) Implement your hosts path variable in the script - here is the default windows path: 
  "C:\Windows\System32\drivers\etc\hosts"

2) Implement your redirect - here is the default IP for the redirect: 
  "127.0.0.1"
  
3) Implement your Website List - Use both www & non-www versions of site: 
  "www.facebook.com","facebook.com","www.zillow.com","zillow.com"
  
4) Run Script 
