###############################################################################
### Rohde & Schwarz SCPI Driver Software Test
###
### Purpose: Import Library-->Create Object-->Catch obvious typos.
###          Tests do not require instrument.
### Author:  mclim
### Date:    2018.06.13
###############################################################################
### Code Start
###############################################################################
import unittest

class TestGeneral(unittest.TestCase):
    def setUp(self):                                #Run before each test
        from guiblox import theme
        self.GUI = theme().addColor()                            #Create GUI object
        print("",end="")
        pass

    def tearDown(self):                             #Run after each test
        pass

###############################################################################
### <Test>
###############################################################################
    def test_DebugTool(self):
        import projects.DebugTool

    def test_helloworld(self):
        import projects.helloworld

    def test_helloworld_tkinter(self):
        import projects.helloworld_tkinter

    def test_IQConvert(self):
        import projects.IQConvert

    def test_Unity(self):
        import projects.Unity_K144

    def test_VSA_VSG_Sweep(self):
        import projects.VSA_VSG_Sweep


###############################################################################
### </Test>
###############################################################################
if __name__ == '__main__':
    if 0:     #Run w/o test names
        unittest.main()
    else:     #Verbose run
        suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneral)
        unittest.TextTestRunner(verbosity=2).run(suite)
