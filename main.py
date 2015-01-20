from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import urllib
import lxml.html




class RootWidget(ScreenManager):
    '''This the class representing your root widget.
       By default it is inherited from ScreenManager,
       you can use any other layout/widget depending on your usage.
    '''
    def post_last(self, req, result):
        try:
            self.roosvelt.text= ".........."
            data = lxml.html.fromstring(result, base_url="https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx")
            var = "Owner: " + data.cssselect("#ctl00_OnlineContent_tdOwner")[0].text_content()+"\n"*2
            var+= "Colour: "+ data.cssselect("#ctl00_OnlineContent_tdColor")[0].text_content()+"\n"*2
            var+= "Maker's Name: "+ data.cssselect("#ctl00_OnlineContent_tdMkrName")[0].text_content()+"\n"*2
            var+= "Mfg.Year: "+ data.cssselect("#ctl00_OnlineContent_tdMfgYear")[0].text_content()+"\n"*2
            var+= "Maker's Class: "+ data.cssselect("#ctl00_OnlineContent_tdMkrClass")[0].text_content()+"\n"*2
            var+= "Engine No.: " + data.cssselect("#ctl00_OnlineContent_tdEngNo")[0].text_content()+"\n"*2
            var+= "Registration Date: " + data.cssselect("#ctl00_OnlineContent_tdDOR")[0].text_content()+"\n"*2
            var+= "Chassis No: " + data.cssselect("#ctl00_OnlineContent_tdChassisno")[0].text_content()+"\n"*2
            self.roosvelt.text= var
        except Exception as e:
            print e
            self.roosvelt.text = str(e)

    def post_again(self, t):
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        params = urllib.urlencode({'__VIEWSTATE': t, 'ctl00$OnlineContent$btnGetData':"Get Data","ctl00$OnlineContent$txtInput":self.search_input.text,"ct0":"R"})
        req = UrlRequest('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx', on_success=self.post_last, req_headers=headers,req_body=params)
        self.roosvelt.text = "Loading....."

    def posted(self, req, result):
        data = lxml.html.fromstring(result, base_url="https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx")
        m = data.cssselect("#__VIEWSTATE")[0].text_content()
        self.post_again(m)
        self.roosvelt.text = "Loading.."

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
