from .models import *
import json

def getSellings():
    
    order = Order.query.all()
    responseData=[]

    for l in range(len(order)):
        date=''
        date += str(order[l].date)

        orpr = OrderProduct.query.all()
        productIds=[]
        orders=[]
        orderss = []
        totals=0
        
        order_product = OrderProduct.query.filter_by(order_id_order = order[l].id).all()
        for j in range(len(order_product)):
            productId = order_product[j].product_id_product
            productIds.append(productId)
            
        for k in range (0,len(productIds)):
            product= Product.query.filter_by(id = productIds[k]).first()
            quantity=OrderProduct.query.filter_by(product_id_product = productIds[k]).first()
            if product is not None and quantity is not None:
                total=product.price*quantity.quantity
                orders = {
                    "product" : product.product,
                    "quantity" : quantity.quantity
                }
                totals+=total
                orderss.append(orders)
            
        response = {
            "date" : date,
            "order" : [orderss],
            "total" : totals
        }

        responseData.append(response)

    # date
    # products(list)
    # quantities(list)
    # totals

    return responseData

def getProducts():
    
    product=Product.query.all()
    responseData = []
    print(product[0].product)
    for i in range(len(product)):
        pname=product[i].product
        price=product[i].price
        response = {
            "product": pname,
            "price": price
        }
        responseData.append(response)
    return responseData

def addProduct(pname,pprice):
    
    product = Product(pname, pprice,1)
    db.session.add(product)
    db.session.commit()

# def deleteProduct(pid):

#     product = Product(pid)
#     db.session.delete(product)
#     db.session.commit()

# def addOrder(uid,pid,qt):

#     order = Order(datetime.now(),uid)
#     db.session.add(order)
#     db.session.commit

# def deleteOrder(oid):

#     order = Order(oid)
#     db.session.delete(order)
#     db.session.commit()
#     orderp = OrderProduct(oid)
#     db.session.delete(orderp)
#     db.session.commit()
