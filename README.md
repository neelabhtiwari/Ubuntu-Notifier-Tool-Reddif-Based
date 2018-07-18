#                      ---    Ubuntu Notifier Tool ---

----- Description -----

This is an utility tool for Ubuntu OS employing Web Scraping using python libraries Beautiful Soup and notify2.

The tool periodically displays Desktop notifications of Breaking News, recent top news, Cricket Scores and Indian Stock Market benchmark Indices.


----- Requirements -----

1. Libraries : <br/>
  a) Beautiful Soup (Ver. 4.0+) <br/>
  b) urllib2 <br/>
  c) notify2 <br/>
  d) time and datetime <br/> 

2. System root access to enable automatic script running on startup


----- Installation Guide -----

1. Run the following commands in the terminal- <br/>
    a) easy_install pip  <br/>
    b) pip install BeautifulSoup4 <br/>
    c) pip install notify2 <br/>
    d) pip install time <br/>
    e) pip install datetime <br/>
    
2. Automatic Execution :  (Source - https://goo.gl/LQRxe3) <br/> 
    a) Copy the python file to /bin: <br/>
          sudo cp -i /path/to/your_script.py /bin <br/>
    b) Add A New Cron Job: <br/>
          sudo crontab -e <br/>
    c) Scroll to the bottom and add the following line (after all the #'s): <br/>
          @reboot python /bin/your_script.py & <br/>
    d) Run it: <br/>
          sudo reboot <br/>

3. Manual Execution : <br/>
  a) Run the command in terminal of the directory "Ubuntu Notifier Tool" : "python main.py" (without quotes) <br/>
  
4. Termination of Manual Script :  <br/>
  a) CTRL + 'C' in script terminal <br/>

------------------------------------------------------------------------------------------------------------------------

Share your valuable feedback on the Email : ubuntunotifiertool@gmail.com
