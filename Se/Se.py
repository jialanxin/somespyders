from selenium import webdriver
from time import sleep
import codecs
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'lanxin_jia@163.com'
password = '520693SYo'
to_addr = '171541975@qq.com'
smtp_server = 'smtp.163.com' 

while True:  
    try:
        browser = webdriver.PhantomJS()
        browser.get('https://webaccess.psu.edu/')
        input_first = browser.find_element_by_id('login')
        input_first.send_keys('lxj230')
        input_second = browser.find_element_by_id('password')
        input_second.send_keys('5200693SYo')
        button = browser.find_element_by_name('thebutton')
        button.click()
        sleep(5)
        browser.find_element_by_xpath("(//a[contains(text(),'Penn State WebMail')])[2]").click()
        sleep(5)
        browser.find_element_by_xpath("//div[@id='login2']/p/a").click()
        sleep(5)
        browser.switch_to.frame(1)
        signal = browser.find_element_by_id('mailcheck').text
        print(signal)
        if signal != 'No new messages.':
            msg = MIMEText('有邮件了', 'plain', 'utf-8')
            msg['From'] = _format_addr('我的vps<%s>' % from_addr)
            msg['Subject'] = Header('有邮件了', 'utf-8').encode()
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()
        browser.close()
        sleep(600)
    except:
        pass
        print(Error)
        sleep(120)    
