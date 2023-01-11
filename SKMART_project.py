################################################################
#               SUPER-MARKET BILL GENERATION
################################################################

################################################################
#                   IMPORT PACKAGES
################################################################

from datetime import datetime
import random
import mysql.connector
import string
################################################################
#                   LINK DATABASE
################################################################

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "srikanth",
    database = "dmart"

)
mycursor = db.cursor()

################################################################
#        CHECK BILLING DETAILS WITH MOBILE NUMBER
################################################################

data_check = input("If you want to Check Data press 0 or 1 for buy Again : ")
print()
if data_check == "0":
    try:
        print("*"*43)
        mob_no = input("Enter Mobile Number : ")
        #finding = "SELECT *FROM dmart_bills where MOBILE_NO = %s"

        data = mycursor.execute("select *from dmart_bills where MOBILE_NO = {}".format(mob_no))
        myresult = mycursor.fetchall()
        len_of_rows = len(myresult)
        print()
        print("TOTAL ORDER -",len_of_rows)

        for index in range(len_of_rows):
            print("-"*50)
            print("ORDER-",index+1)
            print("-"*50)
            print("DATE & TIME : " ,myresult[index][1])
            print("BILL NUMBER : " ,myresult[index][0])
            print("NAME : " ,myresult[index][2])
            print("MOBILE NUMBER : " ,myresult[index][3])
            print("ITEMS : " ,myresult[index][4])
            print("GST : " ,myresult[index][5])
            print("TOTAL AMOUNT : " ,myresult[index][6])
            print()
        print("THANK YOU FOR VISITING...")
        print("*"*43)
    except:
        print("No Data Found...")

elif data_check == "1":
    
################################################################
#                   CUSTOMER INFORMATION
################################################################
    print("*"*43)
    customer_name = input("Enter Customer Name : ").upper()
    customer_mobile_no = input("Enter Customer Mobile No : ")
    print()
    print("*"*43)
################################################################
#                       ITEMS
################################################################
    print("Present Available Items:")
    store_items = {
        "RICE":45,
        "MAIDA":35,
        "OIL":185,
        "BOURBON":36,
        "SALT":30,
        "PAPAD":45,
        "POPCORN":38,
        "COLGATE":66,
        "LAMP WICKS":29,
        "BREAD":49,
        "COOKING SODA":15,
        "AJWAIN-WHOLE":17,
        "JEERA-WHOLE":22,
        "TIL-WHITE":64,
        "SUGAR":45,
        "OATS":47,
        "MOONG DAL":133,
        "TOOR DAL":137,
        "BLACK MUSTARD":32
    }

    print("*"*43)
    for i,r in store_items.items(): 
        print(i,"RS:",r)
    print("*"*43)
################################################################
#                  CUSTOMER BUYING ITEMS
################################################################
    print()
    permission = input("If you want to buy press 1 or 2 for exit : ")
    print("Enter EXIT Scanning Items Will Stoped.")
    print()
    items_db = ""
    if permission == "1":
        items = ""
        quantity = 0

        customer_items_input = {"--":0}

        for i in range(25):
            items = input("Enter Item : ").upper()
            items_db += items + " / "
            quantity = int(input("Enter Quantity : "))
            customer_items_input.update({items:quantity})
            
            if items == "EXIT":
                break
            
        SNO = 1
        total_price = 0
        customer_items_input.pop("EXIT")
        customer_items_input.pop("--")
################################################################
#                    SHOPPING BILL
################################################################
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=15))
        fssai_no = str(random.randint(1000000000000,99999999999999))
        print()
        print("------------WELLCOME TO SK-MART------------")
        print("_"*43)
        print()
        print("           AVENUE SUPERMARTS LTD            ")
        print("_"*43)
        print()
        print("       CIN :- L51900MH2000PLC126473        ")
        print("          GSTIN :",res)
        print("         FSSAI NO.",fssai_no)
        print("_"*43)
        print('''
            City Hyderabad, Lingampally, 
            Ramachandra Puram, 
            Near Cine Town Multiplex
        ''')
        print("_____________Phone : 0123456789_____________")
        print()
        print("              TAX INVOICE                ")
        print()
        date_time = str(datetime.now())
        print("Bill Dt : ",date_time)
        bill_no = str(random.randint(200000000,900000000))
        print("Bill No :",bill_no)
        print("Vou. No : s0812-679  Cashier : MJA/078175")
        print("_"*43)
        print()
        print("Name: " + customer_name.upper())
        print("Mobile: " + customer_mobile_no)
        print("_"*43)
        print()
        print("SNO   ITEMS    Qty     N/Rate     Value")
        print("_"*43)
        print()
################################################################
#                       BILLING SECTION
################################################################
        length_of_item = 0
        qty = 0

        for ITEM,QTY in customer_items_input.items():
            length_of_item = len(ITEM)

            if length_of_item == 3:

                print(SNO,"   ",ITEM,"     ",QTY,"      ",store_items[ITEM],"      ",store_items[ITEM]*QTY)

            elif length_of_item == 4:
                print(SNO,"   ",ITEM,"    ",QTY,"      ",store_items[ITEM],"       ",store_items[ITEM]*QTY)

            elif length_of_item == 5:
                print(SNO,"   ",ITEM,"   ",QTY,"      ",store_items[ITEM],"       ",store_items[ITEM]*QTY)

            elif length_of_item == 6:
                print(SNO,"   ",ITEM,"  ",QTY,"      ",store_items[ITEM],"       ",store_items[ITEM]*QTY)
            
            elif length_of_item == 7:
                print(SNO,"   ",ITEM," ",QTY,"      ",store_items[ITEM],"       ",store_items[ITEM]*QTY)

            total_price += store_items[ITEM]*QTY
            SNO +=1
            qty += QTY
        GST = (total_price*5/100)
        print("_"*43)
        print()
        print("Items :",SNO-1," | Qty:",qty," | Total Amount:",(total_price))
        print("GST :                                ",GST)
        print("="*43)
        print("Final Amount :                     ",GST + total_price)
        print("="*43)
        print("<------Amount Received From Customer------>")
        print("           Card Payment : ",total_price+GST)
        print("_"*43)
        print()
        print("___________THANK YOU FOR VISITING___________")
################################################################
#                   STORED DETAILS IN SQL
################################################################
        GST = str(GST)
        total_price = str(total_price)
        date_time = date_time[:19]
        length_of_items_db = len(items_db)
        items_db = items_db[0:length_of_items_db -9]
        sql = "INSERT INTO dmart_bills (BILL_NO,DATE_TIME,NAME,MOBILE_NO,ITEMS,GST,TOTAL) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (bill_no,date_time,customer_name,customer_mobile_no,items_db,GST,total_price)
        mycursor.execute(sql,val)
        db.commit()
        print()
    elif permission == "2":
        print("THANK YOU FOR VISITING...")
################################################################
#                           END
################################################################
