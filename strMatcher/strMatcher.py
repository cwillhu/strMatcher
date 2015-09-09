
"""
Created on Sept 9, 2015

@author: Chris Williams
"""

import re
from unicodedata import normalize, category


class strMatcher(object):


    def __init__(self, refList): 
        """ 
        Normalize the list of reference strings. 
        """

        if type(refList) != list or not refList:
            raise Exception('A non-empty reference list must be provided')

        self.ref = refList

        #normalize and convert to ascii
        self.refN = [ normalize( 'NFKD', lower_strip(x) ).encode('ascii','ignore') for x in self.ref ] 
        
        
    def find(self, query):  
        """ 
        Normalize query string and search for matches in reference list.

        Return list of matches.
        """

        queryN = normalize( 'NFKD', lower_strip(query) ).encode('ascii','ignore')

        matches = []

        for i, refN in enumerate(self.refN):

            if queryN == refN:
                matches.append(self.ref[i])

        return matches



def lower_strip(aString):  
    """ 
    In input string, collapse whitespace, strip trailing whitespace, make lowercase and remove punctuation. 
    """

    aString = re.sub(r'[\s]+', ' ', unicode(aString), re.UNICODE)
    return unicode(''.join( x for x in aString if category(x) != 'Po' ).lower().strip())



