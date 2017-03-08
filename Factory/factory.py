#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Product:
    def __init__(self):
        self.productType = ''

    def getProductType(self):
        raise NotImplementError("Product")

    def doUse(self):
        raise NotImplementError("Product")


class ProductA(Product):
    def __init__(self):
        self.productType = "ProductA"
        self.productParameter = "A"

    def getProductType(self):
        return self.productType;

    def getParameter(self):
        return self.productParameter

    def doUse(self):
        print ("这是ProductA实现的功能")


class ProductB(Product):
    def __init__(self):
        self.productType = "ProductB"
        self.productParameter = "B"

    def getProductType(self):
        return self.productType;

    def getParameter(self):
        return self.productParameter

    def doUse(self):
        print ("这是ProductB实现的功能")


class Company:
    def bulidProduct(self, Parameter):
        raise NotImplementError("Company")


class CompanyA(Company):
    def __init__(self):
        self.product = ''

    def bulidProduct(self, Parameter):
        if Parameter == "A":
            self.product = ProductA()
            return self.product
        elif Parameter == "B":
            self.product = ProductB()
            return self.product
        else:
            return null;


def main():
    print("———这是factorymethod的输出开始———");
    # 根据传入的参数得到ProductA产品
    product = CompanyA().bulidProduct("A")
    product.doUse()

    # 根据传入的参数得到ProductB产品
    # c = CompanyB()
    product = CompanyA().bulidProduct("B")
    product.doUse()

    print("———这是factorymethod的输出结束———");


if __name__ == '__main__':
    main()
