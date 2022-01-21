import os
import webbrowser
class open_thing:
    def open_things(self, query):
        if query == "my documents":
            os.startfile("C:/Users/jayar/Documents")
            pass
        elif query == "my downloads":
            os.startfile("C:/Users/jayar/Downloads")
            pass
        elif query == "user folder":
            os.startfile("C:/Users/jayar")
        elif query == "desktop":
            os.startfile("C:/Users/jayar/Desktop")
        elif query == "notepad":
            os.system("Notepad")
        elif query == "task manager":
            os.startfile("C:\Windows\System32\Taskmgr.exe")
        elif query == "calculator":
            os.startfile("C:\Windows\System32\calc.exe")
        elif query == "command prompt":
            os.startfile("C:\Windows\System32\cmd.exe")
        elif query == "chrome" or "chrome browser":
            url = "http://www.google.com"
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        else:
            pass