'''
Created on Mar 10, 2016

@author: miedwards
'''
import unittest


class AdderServerTestCase1(unittest.TestCase):


    def setUp(self):
        import AdderServer
        request_handler = AdderServer.AdderRequestHandler
        self.server = AdderServer.AdderServer(('localhost', 7780),
                                              handler_class=request_handler,
                                              others_list=[],
                                              server_id=1,
                                              my_value=1
                                              )
        self.server.serve_forever()        


    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()


    def testHandler(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()