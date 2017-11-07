#! /opt/jython2.7/bin/jython
import random, string
from sikuli import *
import unittest

class TestFacebook(unittest.TestCase):
    def setUp(self):
        '''Récupérer une éventuelle instance de firefox déjà ouverte,
           le lancer au besoin'''
        self.app = App.focus('firefox')
        
        if not self.app.isRunning():
            self.app.open('firefox')
        else:
            self.app.focus()
        
        self.win = self.app.focusedWindow()
        win = self.win
        win.type('t', KeyModifier.CTRL)
        win.type('l', KeyModifier.CTRL)
        win.paste('www.facebook.com')
        win.type(Key.ENTER)
    
    def tearDown(self):
        win = self.win
        win.type('w', KeyModifier.CTRL)
    
    def testA_Publish(self, elements=1):
        for e in range(elements):
            win = self.win
            win.wait(Pattern("facebook_exprimez_vous.png").targetOffset(-167,-8))
            wait(2)
            win.click(Pattern("facebook_exprimez_vous.png").targetOffset(-167,-8))
            content = 'blablabla' + random.choice(string.lowercase) + random.choice(string.lowercase) + random.choice(string.lowercase)
            win.paste(content)
            wait(2)
            win.wait("facebook_publier.png", 5)
            win.click("facebook_publier.png")
            waitVanish("facebook_publier.png")
            wait(2)

    def testB_Delete(self, elements=1):
        try:
            r = Region(668,171,1189,824)
            while r.exists(Pattern("facebook_points.png"), 10):
                r.click(Pattern("facebook_points.png"))
                r.click("facebook_supprimer.png")
                r.wait("facebook_supprimer_publication.png").click()
                r.waitVanish("facebook_supprimer_publication.png")
                wait(3)
        except FindFailed:
            print('Termine !')


suite = unittest.TestLoader().loadTestsFromTestCase(TestFacebook)
unittest.TextTestRunner(verbosity=2).run(suite)
