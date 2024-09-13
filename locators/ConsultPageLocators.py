class Locators:
    '''
    This class represents a locator object.

    Attributes:
        __locator (str): The locator value.

    '''
    def __init__(self):
        self.__links_process = 'a[href*="detalhe"]'
        self.__input_process = 'input[id="q"]'

    @property
    def input_process(self):
        '''
        Get the locator value.
        '''
        return self.__input_process

    @property
    def links_process(self):
        '''
        Get the locator value.
        '''
        return self.__links_process
