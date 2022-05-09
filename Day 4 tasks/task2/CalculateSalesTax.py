import pandas as pd
import csv
import os


class STC:
    '''
        the class contain all the required function to calculate the
        salse tax.

        1. first you need to set the path of the file have product catalog
           file and the salse tax file

        2. you can use the set_product_catalog_file_path(), set_sales_tax_file_path()
           for the same
    ''' 
    def __init__(self):
        self.product_catalog_file_path = ""
        self.sales_tax_file_path = ""

    def set_product_catalog_file_path(self, path):
        self.product_catalog_file_path = os.path.join(*path)

    def set_sales_tax_file_path(self, path):
        self.sales_tax_file_path = os.path.join(*path)

    def get_product_catalog_file_path(self):
        return self.product_catalog_file_path

    def get_sales_tax_file_path(self):
        return self.sales_tax_file_path

    def validate(self):
        """
            checks and return the True or False on the basis
            of following conditions

            1. product_catalog_file_path and sales_tax_file_path
               are set or not

            2. these two file contain the valid headers or not
        """
        
        if self.product_catalog_file_path == "" or self.sales_tax_file_path == "":
            return False
        else:
            # checking if the headers are correct
            productCatalogDf = pd.read_csv( self.product_catalog_file_path )
            salesTaxDf = pd.read_csv("SalesTax.csv")
            
        
        



# Global variables


productCatalogDf = ""
salesTaxDf = ""


def uniqueNameChecker( nameList ):
    return len(nameList) == len(set(nameList))

def taxCalculation():
    if uniqueNameChecker(salesTaxDf["Country"]):
        with open("result.csv", "w", newline="") as csvFileObject:
            thewritter = csv.writer(csvFileObject)

            thewritter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

            salseTaxDfIndex = 0

            while salseTaxDfIndex < len(salesTaxDf):
                productCatalogDfIndex = 0
                while productCatalogDfIndex < len(productCatalogDf):
                    #print( type(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]), " ", type(productCatalogDf['ProductCost'][productCatalogDfIndex]) )
                    try:
                        if( float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex]) >= 0.0 and float(productCatalogDf['ProductCost'][productCatalogDfIndex])> 0.0):
                            taxprice = (float(salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex])* float(productCatalogDf['ProductCost'][productCatalogDfIndex]))/100

                            salesprice = float(productCatalogDf['ProductCost'][productCatalogDfIndex])+taxprice
                
                            thewritter.writerow([productCatalogDf['ProductName'][productCatalogDfIndex], productCatalogDf['ProductCost'][productCatalogDfIndex], salesTaxDf['SalseTaxInPercent'][salseTaxDfIndex], taxprice, salesprice, salesTaxDf['Country'][salseTaxDfIndex]])
                            
                        else:
                            print("input file contain invalid values")
                  
                            
                    except ValueError:
                        print("input file contain characters instead of values")
                        break;
                    except:
                        print("invalid inputs")
                        break

                    finally:
                        productCatalogDfIndex+=1

                salseTaxDfIndex+=1
    else:
        print("country name repeated")
            

        

    
def headerNameValidator():
    columnNames=["ProductName","ProductCost","SalseTaxInPercent","Country"]

    for x in productCatalogDf:
        if x not in columnNames:
            return False

    for x in salesTaxDf:
        if x not in columnNames:
            return False 

    
    #print(productCatalogDf["ProductName"])
    return True



if __name__ == "__main__":
    ProductCatalogFilePath = os.path.join(".","ProductCatalog.csv")
    salesTaxFilePath = os.path.join(".","SalesTax.csv")


    if os.path.exists(ProductCatalogFilePath) and os.path.exists(salesTaxFilePath):
        print("file exist")
        
        
        productCatalogDf = pd.read_csv("ProductCatalog.csv")
        salesTaxDf = pd.read_csv("SalesTax.csv")
        
        if headerNameValidator():
            print("headers are valid")
            taxCalculation()
        else:
            print("headers are not valid")

    else:
        print("file dosen't exist")



