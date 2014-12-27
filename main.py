from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from bs4 import BeautifulSoup
import urllib



class RootWidget(ScreenManager):
    '''This the class representing your root widget.
       By default it is inherited from ScreenManager,
       you can use any other layout/widget depending on your usage.
    '''
    def post_last(self, req, result):
        try:
            soup = BeautifulSoup(result)
            var ="Owner: "+ soup.find(id="ctl00_OnlineContent_tdOwner").text+"\n"*2
            var+= "Vehicle Class: "+ soup.find(id="ctl00_OnlineContent_tdVehClass").text+"\n"*2
            var+= "Colour: "+ soup.find(id="ctl00_OnlineContent_tdColor").text+"\n"*2
            var+= "Maker's Name: "+ soup.find(id="ctl00_OnlineContent_tdMkrName").text+"\n"*2
            var+= "Mfg.Year: "+ soup.find(id="ctl00_OnlineContent_tdMfgYear").text+"\n"*2
            var+= "Maker's Class: " + soup.find(id="ctl00_OnlineContent_tdMkrClass").text+"\n"*2
            var+= "Engine No.: " + soup.find(id="ctl00_OnlineContent_tdEngNo").text+"\n"*2
            var+= "Registration Date: " + soup.find(id="ctl00_OnlineContent_tdDOR").text+"\n"*2
            var+= "Chassis No: " + soup.find(id="ctl00_OnlineContent_tdChassisno").text+"\n"*2
            self.roosvelt.text= var    
        except Exception, e:
            self.roosvelt.text= "Invalid input, Try again!"

    def post_again(self, t):
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        params = urllib.urlencode({'__VIEWSTATE': t, 'ctl00$OnlineContent$btnGetData':"Get Data","ctl00$OnlineContent$txtInput":self.search_input.text,"ct0":"R"})
        req = UrlRequest('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx', on_success=self.post_last, req_headers=headers,req_body=params)

    def posted(self, req, result):
        soup = BeautifulSoup(result)
        print soup
        m= soup.find(id= "__VIEWSTATE")
        t= m.get('value')
        self.post_again(t)

    def postbug(self):
		    
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        req = UrlRequest('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx', on_success=self.posted, req_headers=headers)
    
    pass

class MainApp(App):
    '''This is the main class of your app.
       Define any app wide entities here.
       This class can be accessed anywhere inside the kivy app as,
       in python::

         app = App.get_running_app()
         print (app.title)

       in kv language::

         on_release: print(app.title)
       Name of the .kv file that is auto-loaded is derived from the name of this cass::

         MainApp = main.kv
         MainClass = mainclass.kv

       The App part is auto removed and the whole name is lowercased.
    '''
    def build(self):
        '''Your app will be build from here.
           Return your widget here.
        '''

        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
