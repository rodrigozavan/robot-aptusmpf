class Locators:
    '''
    This class represents a locator object.

    Attributes:
        __locator (str): The locator value.

    '''
    def __init__(self):
        self.__html_process = '#tudo'

    @property
    def html_process(self):
        '''
        Get the locator value.
        '''
        return self.__html_process
