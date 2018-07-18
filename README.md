# Ubuntu Notifier Tool ---

----- Description -----

This is an utility tool for Ubuntu OS employing Web Scraping using python libraries Beautiful Soup and notify2.

The tool periodically displays Desktop notifications of Breaking News, recent top news, Cricket Scores and Indian Stock Market benchmark Indices.


----- Requirements -----

1. Libraries : 
  a) Beautiful Soup (Ver. 4.0+)
  b) urllib2 
  c) notify2
  d) time and datetime 

2. System root access to enable automatic script running on startup


----- Installation Guide -----

1. Run the following commands in the terminal-
    a) easy_install pip  
    b) pip install BeautifulSoup4
    c) pip install notify2
    d) pip install time
    e) pip install datetime
    
2. Automatic Execution :  (Source - https://goo.gl/LQRxe3)
    a) Copy the python file to /bin:
          sudo cp -i /path/to/your_script.py /bin
    b) Add A New Cron Job:
          sudo crontab -e
    c) Scroll to the bottom and add the following line (after all the #'s):
          @reboot python /bin/your_script.py &
    d) Run it:
          sudo reboot

3. Manual Execution :
  a) Run the command in terminal of the directory "Ubuntu Notifier Tool" : "python main.py" (without quotes)
  
4. Termination of Manual Script : 
  a) CTRL + 'C' in script terminal

------------------------------------------------------------------------------------------------------------------------

Share your valuable feedback on the Email : ubuntunotifiertool@gmail.com
