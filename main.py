from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import urllib
import re





class RootWidget(ScreenManager):
    '''This the class representing your root widget.
       By default it is inherited from ScreenManager,
       you can use any other layout/widget depending on your usage.
    '''
    def post_last(self, req, result):

    	self.roosvelt.text = "Loading............"
        try:
        	self.roosvelt.text ="Owner Name: "+ re.findall(r'"ctl00_OnlineContent_tdOwner" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*\s*[^<])<', result)[0]+"\n"*2
        except:
        	self.roosvelt.text = "404 error, Number not found"
        try:
        	self.roosvelt.text += "Colour: "+ re.findall(r'"ctl00_OnlineContent_tdColor" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:	
        	self.roosvelt.text += "Vehicle type: "+ re.findall(r'"ctl00_OnlineContent_tdVehClass" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:	
        	self.roosvelt.text += "Maker Name: "+ re.findall(r'"ctl00_OnlineContent_tdMkrName" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:	
        	self.roosvelt.text += "Fuel type: "+ re.findall(r'"ctl00_OnlineContent_tdFuelType" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:	
        	self.roosvelt.text += "Registered date: "+ re.findall(r'"ctl00_OnlineContent_tdDOR" align="left" colspan="2">([^>]\d*/*\d*/*\d*[^<])<', result)[0]+"\n"*2
        except:
        	pass
        try:	
        	self.roosvelt.text += "Engine number: "+ re.findall(r'"ctl00_OnlineContent_tdEngNo" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:	
        	self.roosvelt.text += "Chassis No: "+ re.findall(r'"ctl00_OnlineContent_tdChassisno" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass	
        try:
        	self.roosvelt.text += "Status: "+ re.findall(r'"ctl00_OnlineContent_tdStatus" align="left" colspan="2">([^>]\w*\s*\w*\s*\w*[^<])<', result)[0]+"\n"*2
        except:
        	pass


    def post_again(self, t):
    	self.roosvelt.text = "Loading......."
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        params = urllib.urlencode({'__VIEWSTATE': t, 'ctl00$OnlineContent$btnGetData':"Get Data","ctl00$OnlineContent$txtInput":self.search_input.text,"ct0":"R"})
        req = UrlRequest('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx', on_success=self.post_last, req_headers=headers,req_body=params,on_error=self.error,on_redirect=self.error ,on_failure=self.error)
        

    def posted(self, req, result):
        self.roosvelt.text = "Loading..."
        print result
        t= re.findall(r'"__VIEWSTATE" value="(/.+)"', result)
        print t
        self.post_again(t[0])
    
    def error(self,req, result):
    	self.roosvelt.text = str(result)
        
    def postbug(self):
        self.roosvelt.text = "Loading"
        headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        req = UrlRequest('https://aptransport.in/APCFSTONLINE/Reports/VehicleRegistrationSearch.aspx', on_success=self.posted,on_error=self.error,on_redirect=self.error ,on_failure=self.error ,req_headers=headers)
        
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
