# Instagram Giveaway Bot

# **Requirements**
- Python 3.6+
- Selenium

## How To Install?
##### Step One
Selenium needs to be installed first for the code to work. 

`pip install selenium`

Selenium has Webdriver in it, I used it for Chrome, you can adapt it by changing the `self.browser = webdriver.Chrome()` part of the code in browser.py

##### Step Two
Replace the codes in userdata.py with your own information.

##### Notes
Check the css part in the followers = `self.browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")` section of browser.py, it may differ for everyone.
