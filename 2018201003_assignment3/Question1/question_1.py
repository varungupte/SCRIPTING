import pickle,os

class Admin:

    def __init__(self,Name):
        self.__id=1
        self.__Name=Name

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def getName(self):
        return self.__Name
    
    def setName(self,Name):
        self.__Name=Name
    
    def AddProduct(self):
        try:
            print("Please enter the below details related to the product to be added(Price must be in integer):- ")
            Name = raw_input("Name:- ")
            Price = int(raw_input("Price:- "))
            Group = raw_input("Group:- ")
            Subgroup = raw_input("Subgroup:- ")

            p = Products(Name,Group,Subgroup,Price)

            products_metadata = {}
            # products_metadata.clear()
            
            if os.path.isfile("db_product.pickle"):
                try:
                    db_current = open("db_product.pickle","rb")
                    products_metadata = pickle.load(db_current)
                    db_current.close()
                    products_metadata[p.getId()] = p
                    db_current = open("db_product.pickle","wb")
                    pickle.dump(products_metadata,db_current)
                    db_current.close()
                except:
                    products_metadata[p.getId()] = p
                    db_current = open("db_product.pickle", 'wb')
                    pickle.dump(products_metadata,db_current)
                    db_current.close()

            else:
                products_metadata[p.getId()] = p
                db_current = open("db_product.pickle", 'wb')
                pickle.dump(products_metadata,db_current)
                db_current.close()

            print "Product added successfully"
        except:
            print "Price must be in integer"

    def ViewProduct(self):

        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()

                if products_metadata:
                    print "<<<<<<<PRODUCT LIST>>>>>>>"
                    print "ID NAME PRICE GROUP SUBGROUP"
                    for i in products_metadata:
                        print products_metadata[i].getId(),products_metadata[i].getName(),products_metadata[i].getPrice(),products_metadata[i].getGroup(),products_metadata[i].getSubgroup()

                    print " "

                else:
                    print "No entries related to the products."
            except:
                print "No entries related to the products."
        else:
            print "No entries related to the products."


    def DeleteProduct(self):

        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()
                if products_metadata:
                    try:
                        id=int(raw_input("Please enter product id to be delete:-"))
                        if id in products_metadata:
                            del products_metadata[id]
                            db_current = open("db_product.pickle","wb")
                            pickle.dump(products_metadata,db_current)
                            db_current.close()
                            print "Product deleted successfully"

                        else:
                            print "There is no product with id = ",id
                    except:
                        print "Entered id is not correct."
                else:
                   print "No related entries in the database."
            except:
                print "No related entries in the database."
        else:
            print "No related entries in the database."
            

    def ModifyProduct(self):

        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()
                if products_metadata:
                    try:
                        id = int(raw_input("Enter ID of a product you want to Update"))
                        
                        if id in products_metadata:
                            try:
                                Name = raw_input("Enter Name of Product")
                                Price = int(raw_input("Enter Price"))
                                Group = raw_input("Enter Group")
                                Subgroup = raw_input("Enter Subgroup")
                                #p = Products(Name,Group,Subgroup,Price)
                                p=products_metadata[id]
                                p.setName(Name)
                                p.setPrice(Price)
                                p.setGroup(Group)
                                p.setSubgroup(Subgroup)
                                products_metadata[id]=p
                                db_current = open("db_product.pickle","wb")
                                pickle.dump(products_metadata,db_current)
                                db_current.close()
                                print "Product modified successfully"
                            except:
                                print "Price must be in integer"

                        else:
                            print "There is no product with id = ",id
                    except:
                        print "Entered id is not correct."
                else:
                   print "No related entries in the database to modify."
            except:
                print "No related entries in the database to modify."
        else:
            print "No related entries in the database to modify."
            


class Customer:
    
    def __init__(self,Name,Address,PhnNo):
        if os.path.isfile("db_customer.pickle"):
            try:
                db_current = open("db_customer.pickle","rb")
                customer_metadata = pickle.load(db_current)
                db_current.close()
                ids = customer_metadata.keys()
                self.__id=max(ids)+1
            except:
                self.__id=1
        else:
            self.__id=1
        self._Name=Name
        self._Address=Address
        self._PhnNo=PhnNo

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def setName(self,Name):
        self._Name=Name

    def getName(self):
        return self._Name

    def setAddress(self,Address):
        self._Address = Address

    def getAddress(self):
        return self._Address

    def setPhnNo(self,PhnNo):
        self._PhnNo = PhnNo

    def getPhnNo(self):
        return self._PhnNo

    def BuyProducts(self):
        
        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()
                try:
	                id = int(raw_input("Please enter the product id you want to buy:- "))
	                if id in products_metadata:
	                    self.MakePayment(id,products_metadata)
	                else:
	                    print "There is no product with id = ",id
                except:
                    print "No related entries in the database."
            except:
                print "No related entries in the database."
        else:
            print "No related entries in the database."

    def ViewProduct(self):

        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()

                if products_metadata:
                    print "<<<<<<<PRODUCT LIST>>>>>>>"
                    print "ID NAME PRICE GROUP SUBGROUP"
                    for i in products_metadata:
                        print products_metadata[i].getId(),products_metadata[i].getName(),products_metadata[i].getPrice(),products_metadata[i].getGroup(),products_metadata[i].getSubgroup()

                    print " "

                else:
                    print "No Product Found"
            except:
                print "No Product Found"
        else:
            print "No Product Found"

    def MakePayment(self,id,products_metadata):
        print "Please pay ",products_metadata[id].getPrice()," Amount"
        CT = raw_input("Enter CardType")
        CNO = raw_input("Enter CardNo")

        py = Payment(products_metadata[id].getName(),CT,CNO)
        if os.path.isfile("payment.pickle"):
            try:
                db_current = open("payment.pickle","rb")
                list_pay = pickle.load(db_current)
                db_current.close()
                paylist  = list_pay[self.__id]
                paylist.append(py)
                list_pay[self.__id] = paylist
                db_current = open("payment.pickle","wb")
                pickle.dump(list_pay,db_current)
                db_current.close()
                print "Payment Completed"
            except:
                pay = []
                pay.append(py)
                list_pay = {1:pay}
                list_pay.clear()
                list_pay[self.__id] = pay
                db_current = open("payment.pickle","wb")
                pickle.dump(list_pay,db_current)
                db_current.close()
                print "Payment Completed"
        else:
            pay = []
            pay.append(py)
            list_pay = {1:pay}
            list_pay.clear()
            list_pay[self.__id] = pay
            db_current = open("payment.pickle","wb")
            pickle.dump(list_pay,db_current)
            db_current.close()
            print "Payment Completed"

        if os.path.isfile("cart.pickle"):
            try:
                db_current = open("cart.pickle","rb")
                list_cart = pickle.load(db_current)
                db_current.close()     
                ct = list_cart[self.__id]
                pList = ct.getProductList()
                f=0
                for item in pList:
                    if item.getId() == id:
                        f=1
                        break
                if f==1:
                    self.DeleteFromCart(id)
            except:
                pass


    def ViewCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                db_current = open("cart.pickle","rb")
                list_cart = pickle.load(db_current)
                db_current.close()
                if list_cart:
                    ct = list_cart[self.__id]
                    x = ct.getProductList()
                    if x:
                        print "<<<<<<<CART PRODUCT LIST>>>>>>>"
                        print "ID NAME PRICE GROUP SUBGROUP"
                        for i in x:
                            print i.getId(),i.getName(),i.getGroup(),i.getSubgroup(),i.getPrice()
                        print "Total = ",ct.getTotal()
                        print " "
                    else:
                        print "No related entries in the cart."
                else:
                    print "No related entries in the cart."
            except:
                print "No related entries in the cart."
        else:
            print "No related entries in the cart."

    def AddToCart(self):
        
        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()
                x = []
                list_cart = {}
                # list_cart.clear()
                if products_metadata:
                    try:
                        id = int(raw_input("Enter Id of a product you want to add"))
                        if id in products_metadata:
                            p = products_metadata[id]
                            if os.path.isfile("cart.pickle"):
                                try:
                                    db_current = open("cart.pickle","rb")
                                    list_cart = pickle.load(db_current)
                                    db_current.close()
                                    if list_cart:
                                        ct = list_cart[self.__id]
                                        x = ct.getProductList()
                                        total = ct.getTotal() + p.getPrice()
                                        Number = ct.getNumberOfProducts()+1
                                        x.append(p)
                                        ct.setProductList(x)
                                        ct.setTotal(total)
                                        ct.setNumberOfProducts(Number)
                                        list_cart[self.__id] = ct
                                        db_current = open("cart.pickle","wb")
                                        pickle.dump(list_cart,db_current)
                                        db_current.close()
                                    else:
                                        x.append(p)
                                        total = p.getPrice()
                                        ct = Cart(1,total,x,self.__id)
                                        list_cart[self.__id] = ct
                                        db_current = open("cart.pickle","wb")
                                        pickle.dump(list_cart,db_current)
                                        db_current.close()
                                except:
                                    x.append(p)
                                    total = p.getPrice()
                                    ct = Cart(1,total,x,self.__id)
                                    list_cart[self.__id] = ct
                                    db_current = open("cart.pickle","wb")
                                    pickle.dump(list_cart,db_current)
                                    db_current.close()
                            else:
                                x.append(p)
                                total = p.getPrice()
                                ct = Cart(1,total,x,self.__id)
                                list_cart[self.__id] = ct
                                db_current = open("cart.pickle","wb")
                                pickle.dump(list_cart,db_current)
                                db_current.close()
                        else:
                            print "There is no product with id = ",id
                    except:
                        print "No related entries in the cart."
                else:
                    print "No related entries in the cart."
            except:
                print "No related entries in the cart."

        else:
            print "No product found"

    def DeleteFromCart(self,id=0):
        if os.path.isfile("cart.pickle"):
            try:
                db_current = open("cart.pickle","rb")
                list_cart = pickle.load(db_current)
                db_current.close()
                if list_cart:
                    ct = list_cart[self.__id]
                    x = ct.getProductList()
                    if x:
                        try:
                            if id==0:
                                id = int(raw_input("Please enter the id of the product you want to delete:- "))
                            f=0
                            for item in x:
                                if item.getId() == id:
                                    p=item
                                    f=1
                                    break
                            if f>0:
                                x.remove(p)
                                number = ct.getNumberOfProducts()-1
                                total = ct.getTotal() - p.getPrice()
                                ct.setTotal(total)
                                ct.setNumberOfProducts(number)
                                ct.setProductList(x)
                                list_cart[self.__id] = ct
                                db_current = open("cart.pickle","wb")
                                pickle.dump(list_cart,db_current)
                                db_current.close()

                            else:
                                print "There is no product with id = ",id
                        except:
                            print "No related entries in the cart."
                    else:
                        print "No related entries in the cart."
                else:
                    print "No related entries in the cart."
            except:
                print "No related entries in the cart."
        else:
            print "No related entries in the cart."

    def BuyCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                db_current = open("cart.pickle","rb")
                list_cart = pickle.load(db_current)
                db_current.close()
                if list_cart:
                    if list_cart[self.__id]:
                        ct = list_cart[self.__id]
                        print "Total amount to be paid:- ",ct.getTotal(),"Rs"
                        CT = raw_input("Enter CardType:- ")
                        CNO = raw_input("Enter CardNo:- ")
                        plist = ct.getProductList()
                        listname=""
                        for pname in plist:
                            if listname=="":
                                listname = pname.getName()
                            else:
                                listname = listname +","+ pname.getName()
                        py = Payment(listname,CT,CNO)
                        if os.path.isfile("payment.pickle"):
                        	try:
	                            db_current = open("payment.pickle","rb")
	                            list_pay = pickle.load(db_current)
	                            db_current.close()
	                            paylist  = list_pay[self.__id]
	                            paylist.append(py)
	                            list_pay[self.__id] = paylist
	                            db_current = open("payment.pickle","wb")
	                            pickle.dump(list_pay,db_current)
	                            db_current.close()
	                            print "Payment Completed"
	                            
	                        except:
			                    	pay = []
			                        pay.append(py)
			                        list_pay = {}
			                        list_pay[self.__id] = pay
			                        db_current = open("payment.pickle","wb")
			                        pickle.dump(list_pay,db_current)
			                        db_current.close()
			                        print "Payment Completed"
                        else:
                            pay = []
                            pay.append(py)
                            list_pay = {}
                            # list_pay.clear()
                            list_pay[self.__id] = pay
                            db_current = open("payment.pickle","wb")
                            pickle.dump(list_pay,db_current)
                            db_current.close()
                            print "Payment Completed"
                        del list_cart[self.__id]
                        db_current = open("cart.pickle","wb")
                        pickle.dump(list_cart,db_current)
                        db_current.close()
                    else:
                        print "No product found in cart"
                else:
                    print "No product found in cart"
            except:
                print "No product found in cart"
        else:
            print "No product found in cart"
    
    def history(self):
        if os.path.isfile("payment.pickle"):
            try:
                db_current = open("payment.pickle","rb")
                list_pay = pickle.load(db_current)
                db_current.close()
                paylist  = list_pay[self.__id]
                if paylist:
                    print"<<<<<<< History Of Transactions >>>>>>>"
                    for item in paylist:
                        print item.getName(),item.getCardType(),item.getCardNo()
                    print " "
                else:
                    print "No history found"
            except:
                print "No history found"
        else:
            print "No history found"
class Products:

    def __init__(self,Name,Group,Subgroup,Price):
        
        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()
                ids = products_metadata.keys()
                self.__id = max(ids) + 1
            except:
                self.__id=1
        else:
            self.__id=1
        self._Name=Name
        self._Group=Group
        self._Subgroup=Subgroup
        self._Price=Price

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def setName(self,Name):
        self._Name=Name

    def getName(self):
        return self._Name
    
    def setGroup(self,Group):
        self._Group=Group

    def getGroup(self):
        return self._Group

    def setSubgroup(self,Subgroup):
        self._Subgroup=Subgroup

    def getSubgroup(self):
        return self._Subgroup
    def setPrice(self,Price):
        self._Price=Price

    def getPrice(self):
        return self._Price


class Cart:
    
    def __init__(self,NumberOfProducts,Total,ProductList,customer_id):
        self.__id=1
        self.customer_id=customer_id
        self._NumberOfProducts = NumberOfProducts
        self._Total = Total
        self.ProductList=ProductList

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setNumberOfProducts(self,NumberOfProducts):
        self._NumberOfProducts = NumberOfProducts

    def getNumberOfProducts(self):
        return self._NumberOfProducts

    def setTotal(self,Total):
        self._Total = Total

    def getTotal(self):
        return self._Total

    def setProductList(self,ProductList):
        self._ProductList = ProductList

    def getProductList(self):
        return self.ProductList


class Payment:
    
    def __init__(self,Name,CardType,CardNo):
        self.__id=1
        self.Name = Name
        self.__CardType = CardType
        self.__CardNo = CardNo

    def setId(self,id):
        self.__id=id

    def getId(self):
        return self.__id

    def setName(self,Name):
        self.__Name=Name

    def getName(self):
        return self.Name

    def setCardType(self,CardType):
        self.__CardType=CardType

    def getCardType(self):
        return self.__CardType

    def setCardNo(self,CardNo):
        self.__CardNo=CardNo

    def getCardNo(self):
        return self.__CardNo

class Guest:
    
    def ViewProducts(self):

        if os.path.isfile("db_product.pickle"):
            try:
                db_current = open("db_product.pickle","rb")
                products_metadata = pickle.load(db_current)
                db_current.close()

                if products_metadata:
                    print "<<<<<<<PRODUCT LIST>>>>>>>"
                    print "ID NAME PRICE GROUP SUBGROUP"
                    for i in products_metadata:
                        print products_metadata[i].getId(),products_metadata[i].getName(),products_metadata[i].getPrice(),products_metadata[i].getGroup(),products_metadata[i].getSubgroup()

                    print ""

                else:
                    print "No Product Found"
            except:
                print "No Product Found"
        else:
            print "No Product Found"

    def GetRegistered(self):
        print "Please enter the below details:-"
        Name = raw_input("Name:- ")
        PhnNo = raw_input("Phone number:-")
        Address = raw_input("Address:-")

        c = Customer(Name,Address,PhnNo)
        customer_metadata = {}
        
        
        if os.path.isfile("db_customer.pickle"):
            db_current = open("db_customer.pickle","rb")
            customer_metadata = pickle.load(db_current)
            db_current.close()
            customer_metadata[c.getId()] = c
            db_current = open("db_customer.pickle","wb")
            pickle.dump(customer_metadata,db_current)
            db_current.close()

        else:
            customer_metadata[c.getId()] = c
            db_current = open("db_customer.pickle", 'wb')
            pickle.dump(customer_metadata,db_current)
            db_current.close()

        print  "Your ID - ",c.getId()
        print "Must Remember"
        
while 1:
    print "1:-Admin"
    print "2:-Customer"
    print "3:-Guest"
    print "0:-Exit"
    try:
        choice = int(raw_input())
        if choice == 1:
            name = raw_input("Enter the name of the admin user:- ")
            if name != "admin":
                print "Please provide correct credentials for admin."
                # continue
            else:    # break
                admin = Admin(name)
    	        while 1:
    	            print "1:-AddProduct "
    	            print "2:-ViewProduct "
    	            print "3:-DeleteProduct "
    	            print "4:-ModifyProduct "
    	            print "0:-Exit"
    	            # print "5 to MakeShipment"
    	            # print "6 to ConfirmDelivery"
    	            choice1=int(raw_input())

    	            if choice1 == 1:
    	                admin.AddProduct()
    	            elif choice1 == 2:
    	                admin.ViewProduct()
    	            elif choice1 == 3:
    	                admin.ViewProduct()
    	                admin.DeleteProduct()
    	            elif choice1 == 4:
    	                admin.ViewProduct()
    	                admin.ModifyProduct()
    	            elif choice1 == 0:
    	                break
    	            else:
    	                print "Please enter the correct choice."

        elif choice == 2:
	        id = int(raw_input("Enter Customer Id:-"))
	        db_current = open("db_customer.pickle","rb")
	        customer_metadata = pickle.load(db_current)
	        db_current.close()
	        c = customer_metadata[id]
	        if c:
	            while 1:
	                print "1:-BuyProducts:-"
	                print "2:-ViewProduct:-"
	                print "3:-AddToCart:-"
	                print "4:-DeleteFromCart:-"
	                print "5:-BuyCart:-"
	                print "6:-History:-"
	                print "7:-ViewCart:-"
	                print "0:-Exit"
	                choice2 = int(raw_input())
	                if choice2 == 1:
	                    c.ViewProduct()
	                    c.BuyProducts()
	                elif choice2 == 2:
	                    c.ViewProduct()
	                elif choice2 == 3:
	                    c.ViewProduct()
	                    c.AddToCart()
	                elif choice2 == 4:
	                    c.ViewCart()
	                    c.DeleteFromCart()
	                elif choice2 == 5:
	                    c.ViewCart()
	                    c.BuyCart()
	                elif choice2 == 6:
	                    c.history()
	                elif choice2 == 7:
	                    c.ViewCart()
	                elif choice2 == 0:
	                    break
	                else:
	                    print "Please enter the correct choice"
	        else:
	            print "Unauthorized Customer"

        elif choice == 3:
	        g = Guest()
	        while 1:
	            print "1:-ViewProducts"
	            print "2:-GetRegistered"
	            print "0:-Exit"
	            choice3 = int(raw_input())
	            if choice3 == 1:
	                g.ViewProducts()
	            elif choice3 == 2:
	                g.GetRegistered()
	                break
	            elif choice3 == 0:
	                break
	            else:
	                print "Please enter the correct choice."
        elif choice == 0:
	        break
        else:
	        print "Please enter the correct choice."
    except:
        print "Please enter the correct choice."
