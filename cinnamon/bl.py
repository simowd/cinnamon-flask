from .models import *
import json

def getSellings():
    
    order = Order.query.all()
    responseData=[]
    for l in range(0,len(order)):
        date = order[l].date
        orpr = OrderProduct.query.all()
        productIds=[]
        products=[]
        quantities=[]
        totals=0
        
        for i in range(0,len(orpr)):
            order_product = OrderProduct.query.filter_by(order_id_order = order.id_order[l]).first()
            productId = order_product.id_product
            productIds.append(productId)

        for j in range(0,len(productIds)):
            product= Product.query.filter_by(id_product=productIds[i]).first()
            products.append(product.product)

        for k in range (0,len(productIds)):
            product= Product.query.filter_by(id_product=productIds[i]).first()
            quantity=OrderProduct.query.filter_by(product_id_product = productIds[i]).first()
            total=product.price*quantity.quantity
            quantities.append(quantity.quantity)
            totals+=total

        response = {
            "date" : str(date),
            "products" : [products],
            "quantities" : [quantities],
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
    for i in range(0,len(product)):
        pname=product[i].product
        price=product[i].price
        response = {
            "product": pname,
            "price": price
        }
    responseData.append(response)
    return responseData

# def addProduct(pname,pprice):
    
#     product = Product(pname, pprice,1)
#     db.session.add(product)
#     db.session.commit()

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
