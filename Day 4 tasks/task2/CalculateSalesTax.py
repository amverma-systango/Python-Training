import pandas as pd
import csv
import logging
from util.utility import unique_name_check, path_join


log = logging.getLogger()


class SalseTaxCalculator:

    '''
        the class contain all the required function to calculate the
        salse tax.

        1. first you need to set the path of the file have product catalog
           file and the salse tax file

        2. you can use the set_product_catalog_file_path(), set_sales_tax_file_path()
           for the same
    ''' 

    def __init__(self, product_catalog_file_path, sales_tax_file_path):
        self.product_catalog_file_path = product_catalog_file_path
        self.sales_tax_file_path = sales_tax_file_path

        self.product_catalog_df = None
        self.sales_tax_df = None


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

        if self.product_catalog_file_path == "" or self.sales_tax_file_path == "" :
            return False
        
        else:
            self.product_catalog_df = pd.read_csv( self.product_catalog_file_path )
            self.sales_tax_df = pd.read_csv( self.sales_tax_file_path )
            
            valid_column_name = ["ProductName","ProductCost","SalseTaxInPercent","Country"]

            for column_name in self.product_catalog_df:
                if column_name not in valid_column_name:
                    return False

            for column_name in self.sales_tax_df:
                if column_name not in valid_column_name:
                    return False

            return True
    

    def calculate_tax( self ):
        """
            this method calculate the tax corresponding
            to each product in every country and write 
            them into the result.csv file
        """
        
        if self.validate() and unique_name_check(self.sales_tax_df["Country"]):
            
            with open("result.csv", "w", newline="") as csv_File_Object:
                the_writter = csv.writer(csv_File_Object)

                the_writter.writerow(["Product-Name", "Product-CostPrice", "Product-SalesTax", "Product-SalesTaxAmount", "Product-FinalPrice", "Country"])

                sales_tax_df_index = 0

                while sales_tax_df_index < len(self.sales_tax_df):
                    product_catalog_df_index = 0
                    
                    while product_catalog_df_index < len(self.product_catalog_df):              
                        try:
                            if( float(self.sales_tax_df['SalseTaxInPercent'][sales_tax_df_index]) >= 0.0 and float(self.product_catalog_df['ProductCost'][product_catalog_df_index])> 0.0):
                                tax_price = (float(self.sales_tax_df['SalseTaxInPercent'][sales_tax_df_index])* float(self.product_catalog_df['ProductCost'][product_catalog_df_index]))/100

                                sales_price = float(self.product_catalog_df['ProductCost'][product_catalog_df_index])+tax_price
                    
                                the_writter.writerow([self.product_catalog_df['ProductName'][product_catalog_df_index], self.product_catalog_df['ProductCost'][product_catalog_df_index], self.sales_tax_df['SalseTaxInPercent'][sales_tax_df_index], tax_price, sales_price, self.sales_tax_df['Country'][sales_tax_df_index]])
                                
                            else:
                                log.warning("input file contain invalid values")
                      
                                
                        except ValueError:
                            log.warning("input file contain characters instead of values")
                            break
                        except Exception as e:
                            log.warning(e)
                            log.warning("invalid inputs")
                            break

                        finally:
                            product_catalog_df_index+=1

                    sales_tax_df_index+=1
            
        else:
            log.warning("country name repeated")
            
        
if __name__ == "__main__":

    obj = SalseTaxCalculator(path_join(["." , "ProductCatalog.csv"]),path_join(["." , "SalesTax.csv"]))
    obj.calculate_tax()
    
