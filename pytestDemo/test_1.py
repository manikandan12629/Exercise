import logging

import pytest

from Baseclass import Baseclass


class Testsam(Baseclass):

    def test_1(self):
        x = 10
        y = 10
        log = self.getLogger()
        log.info("test1")
        assert x == y

    def test_5(self, crossBrowser):
        log = self.getLogger()
        log.info(crossBrowser)
        print(crossBrowser)

    def test_10(self):
        x = "manikandan"
        y = "kandan"
        log = self.getLogger()
        log.info("test10")
        assert y in x
