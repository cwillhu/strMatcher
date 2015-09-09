# -*- coding: utf-8 -*-

"""
Created on Sept 9, 2015

@author: Chris Williams
"""

import unittest
from strMatcher import strMatcher

class TestMatcher(unittest.TestCase):


    def setUp(self):
        self.refList = [ u'à la façon',
                         u'08.09.2015',
                         u'21h43',
                         u'21:43',
                         u"l'Édition",
                         u'à bientôt !',
                         u'Bien fait.',
                         u'85 meters',
                         u'date',
                         u'daté',
                         u'Una nación',
                         u'un estado_catalán',
                         u'la decisión',
                         u'José Ramón',
                         u'The Ramones',
                         u'Recreación de la vida',
                         u'Ölgemälde „Das Eingreifen“',
                         u'Sie sind "enttäuscht".',
                         u'Die Länder in Europa.',
                         u'Brüssel',
                         u'Brussels',
                         u'brussel sprouts' ]


        self.testQueries =  [ dict(query = 'date',                        expected = [u'date', u'daté']),
                              dict(query = '21:43',                       expected = [u'21:43']),
                              dict(query = '2143',                        expected = [u'21:43']),
                              dict(query = 'a bientot.',                  expected = [u'à bientôt !']),
                              dict(query = u'À Bientôt!!',                expected = [u'à bientôt !']),
                              dict(query = u'a bientot',                  expected = [u'à bientôt !']),
                              dict(query = u' à bientôt ! ',              expected = [u'à bientôt !']),
                              dict(query = u"L'Edition..",                expected = [u"l'Édition"]),
                              dict(query = 'Brussel',                     expected = [u'Brüssel']),
                              dict(query = u'Brüssel',                    expected = [u'Brüssel']),
                              dict(query = u'brussel',                    expected = [u'Brüssel']),
                              dict(query = 'olgemalde das eingreifen',    expected = [u'Ölgemälde „Das Eingreifen“']),
                              dict(query = u'olgemalde das eingreifen',   expected = [u'Ölgemälde „Das Eingreifen“']),
                              dict(query = u'Ölgemälde „Das Eingreifen“', expected = [u'Ölgemälde „Das Eingreifen“']),
                              dict(query = '08/09/2015',                  expected = [u'08.09.2015']),
                              dict(query = u'08/09/2015',                 expected = [u'08.09.2015']),
                              dict(query = u'08092015',                   expected = [u'08.09.2015']),

                              dict(query = u'un estado catalán',          expected = []),
                              dict(query = u'Ölgemälde',                  expected = []),
                              dict(query = 'dates',                       expected = []),
                              dict(query = u'dates',                      expected = []),
                              dict(query = 'joseramon',                   expected = []),
                              dict(query = u'joseramon',                  expected = []),
                              dict(query = u'JoséRamón',                  expected = []),
                              dict(query = u'85',                         expected = []) ]


    def testQuerySet(self):

        matcher = strMatcher(self.refList)

        for queryDict in self.testQueries:
            
            queryString = queryDict['query']

            matches = matcher.find( queryString )

            self.assertEqual( matches, queryDict['expected'], 'Unexpected match(es) for query "%s": %s' % (queryString, matches) )



if __name__ == "__main__":

    unittest.main() 
