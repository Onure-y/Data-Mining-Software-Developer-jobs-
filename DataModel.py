class DataModel:
    def __init__(self):
        self.allGlasses = []

    def addNewGlassesToAllGlasses(self, gBand, gPrice, gD1, gD2, gD3, ):
        try:
            glasses = {}
            glasses['gBand'] = gBand
            glasses['gPrice'] = self.getExactPrice(gPrice)
            glasses['gD1'] = self.getExactValue(gD1)
            glasses['gD2'] = self.getExactValue(gD2)
            glasses['gD3'] = self.getExactValue(gD3)
        except:
            print('error wrong data type')
            glasses['gBand'] = gBand
            glasses['gPrice'] = ""
            glasses['gD1'] = ""
            glasses['gD2'] = ""
            glasses['gD3'] = ""
        finally:
            self.allGlasses.append(glasses)

    def getLength(self):
        print(len(self.allGlasses))

    def getExactPrice(self, price):
        if len(price) > 9:
            price = price.split('.')
            price = price[0] + price[1]
        price = price.split(',')
        price = price[0]
        return price

    def getExactValue(self,value):
        value = value.split(' ')
        value = value[0]
        return value

    def printAllData(self):
        for glasses in self.allGlasses:
            print(glasses)
