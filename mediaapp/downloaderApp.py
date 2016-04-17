import abc
 
class downloaderApp(object):
    __metaclass__ = abc.ABCMeta    
    @abc.abstractmethod
    def get_clean_payload(self):
        return    

    @abc.abstractmethod
    def get_ID(self):
        return    

    @abc.abstractmethod
    def do(self):
        return