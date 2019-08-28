################################################################################
# class name SplunkConnection
# purpose: class to create splunk connection instances for use in searches, etc
# author: Ray Zupancic
################################################################################

import splunklib.client as splunkclient

class SplunkConnection:
    DEBUG = False

    def __init__(self):
        'create a Splunk service instance and log in' 
        self.service = ""
        self.kwargs = self.get_credentials_from_rc()
        if self.DEBUG:
            print (self.kwargs)
        # connect requires keywords not positional args
        self.service = splunkclient.connect(**self.kwargs)
        if self.DEBUG:
            print ('service: ' , self.service)

    def get_credentials_from_rc(self):
        'read connection parameters from an rc file'
        '''to use: create a splunkrc file that has username, host, etc:
           username = somename
           host = myhost
           password = somepass
           ...
        '''
        kwargs = {}
        with open(".splunkrc") as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                # by convention python comm likes to use kwargs as the 
                # name of key word sweeper dictionary
                kwargs[name] = var.rstrip()
        return kwargs

    def get_app_names(self):
        'print installed apps to the console to verify login'
        app_list = []
        for app in self.service.apps:
            app_list.append(app.name)
        return app_list
