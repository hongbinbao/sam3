#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from devicewrapper.android import device as d

class PhoneTest(unittest.TestCase):
    def setUp(self):
        super(PhoneTest, self).setUp()
        d.wakeup()
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        d.press('back')\
         .press('back')\
         .press('home')

    def tearDown(self):
        super(PhoneTest, self).tearDown()
        d.press('back')\
         .press('back')\
         .press('back')\
         .press('home')

    def testCall(self):
        assert d.exists(text='Phone') 
        assert d.exists(text='Apps')
        d(text='Phone').click.wait()
        d(description='One').click()
        d(description='Zero').click()
        d(description='Zero').click()
        d(description='Eight').click()
        d(description='Six').click()
        assert d.exists(text="10086")
        d(description='Dial').click.wait()
        assert d(text="Hold").wait.exists(timeout=10000), 'not connected in 10 secs'
        #assert d.exists(text='Hold'), 'not connected in 8 secs'
        assert d(text="00:10").wait.exists(timeout=20000), 'call duration should be 10 secs'
        assert d.exists(text='End call'), 'no End call button'
        d(text='End call').click.wait()
        assert d(text="Hold").wait.gone(timeout=10000), 'not connected in 10 secs'
      

        #sys.stderr.write(str(d(text="Settings").click()))
        #d.click(100, 200, waittime=2)
        #d.start_activity(action='android.intent.action.DIAL', data='tel:13581739891', flags=0x04000000)
        #d.click('a.png', waittime=1, threshold=0.01)\
        # .expect('no_msg.png')\
        # .click('create_btn.png')#
        #if d.find('input_label.png'):
        #    d.click('input_label.png')\
        #     .click('content_label.png')
        #d.expect('send_btn.png')
        #assert d.exists(text='New message')
            


