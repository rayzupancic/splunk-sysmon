################################################################################
# class name SplunkSearch
# purpose: class to search Splunk
# author: Ray Zupancic
################################################################################
import splunklib.results as results

class SplunkSearch:
    DEBUG = True

    def __init__(self,service):
        'create a Splunk service instance and log in' 
        self.job = ''
        self.jobs = service.jobs

    def set_blocking_search(self,query, num_results):
        'place a blocking search on jobs collection'
        # num results can be 0 for no limit, or limited by num_results

        if num_results == 0:
            search = query
        else:
            search = query + ' | head ' + str(num_results)

        if self.DEBUG:
            print ('Query: ', search)

        kwargs = {"exec_mode": "blocking"}
        self.job = self.jobs.create(search, **kwargs)

    def set_search(self,num_results):
        pass


    def get_search_results(self):
        rr = results.ResultsReader(self.job.results())
        return rr
        

