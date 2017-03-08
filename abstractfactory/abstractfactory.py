#!/usr/bin/python
# -*- coding: UTF-8 -*-
from StdSuites import null


class Computer:
    def doUse(self):
        raise NotImplementedError("Computer")

class NotebookComputer(Computer):
    def doUse(self):
        print ("这是笔记本电脑的功能")

class PersonalComputer(Computer):
    def doUse(self):
        print ("这是私人电脑的功能")

class Telephone:
    def doUse(self):
        raise NotImplementedError("Telephone");

class DesktopPhone(Telephone):
    def doUse(self):
        print ("这是座机电话的功能")

class Mobile(Telephone):
    def doUse(self):
        print ("这是手机的功能")

class Company:
    def buildProduct(self, Parameter):
        raise NotImplementedError("Company")

class CompanyA(Company):
    def buildComputer(self, Parameter):
        if Parameter == "个人电脑":
            return PersonalComputer();
        elif Parameter == "笔记本电脑":
            return NotebookComputer();
        else:
            return null;

    def buildTelephone(self, Parameter):
        if Parameter == "座机电话":
            return DesktopPhone()
        elif Parameter == "手机":
            return Mobile()
        else:
            return null;

def main():
    print ("abstract factory 输出开始")
    computer1 = CompanyA().buildComputer("个人电脑")
    computer1.doUse();

    computer2 = CompanyA().buildComputer("笔记本电脑")
    computer2.doUse()

    phone1 = CompanyA().buildTelephone("座机电话")
    phone1.doUse()

    phone2 = CompanyA().buildTelephone("手机")
    phone2.doUse()

    print ("output stop")


if __name__ == '__main__':
    main()

