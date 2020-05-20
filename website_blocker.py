######### WEBSITE BLOCKER #############
# Check out the README first. 
# Case Use: To block distracting websites during working hours of the day (Like 8AM to 4PM). 

import time
from datetime import datetime as dt

#HOST PATH FILE LOCATION
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
#REDIRECT IP
redirect="127.0.0.1"
#WEBSITE LIST *Use both non & www versions of the site*
website_list=["www.facebook.com","facebook.com","www.zillow.com","zillow.com"]

# while the computer is functioning
while True:
    # if the datetime is between 8am - 4pm
    if dt(dt.now().year,dt.now().month,dt.now().day,15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): 
        print ("Working hours...")
        
        #Open and read the content of the hosts file
        with open(hosts_path,"r+") as file:
            content=file.read()
            
            #for every website in the website list
            for website in website_list:
                #if the website is within hosts file, pass
                if website in content:
                    pass
                #else add the redirect & website name to the file along with a break
                else:
                    file.write(redirect+" "+ website+"\n")
    
    # if the date time is not between work hours
    else: 
        
        #open and read the content of the hosts file starting at the 0 index - beginning
        with open(hosts_path,'r+') as file:  
            content=file.readlines()
            file.seek(0)
            
            # for every line within the file, if there is no website listed on the line, write a new line of the content. 
            for line in content: 
                if not any (website in line for website in website_list):
                    file.write(line)
            
            #delete any existing duplicate host information. 
            file.truncate()
    
        print ("Fun hours...")
    time.sleep(5)