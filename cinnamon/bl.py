from .models import *
import json
from datetime import datetime
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

def getSellings():
    
    order = Order.query.filter_by(status=1).all()
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


def getSellingsByDate(today,tomorrow):

    order = db.session.query(Order).filter(Order.date >= today, Order.date < tomorrow, Order.status==1).all()
    responseData = []

    for l in range(len(order)):
        date = ''
        date += str(order[l].date)

        orpr = OrderProduct.query.all()
        productIds = []
        orders = []
        id = order[l].id
        orderss = []
        totals = 0

        order_product = OrderProduct.query.filter_by(order_id_order=order[l].id).all()
        for j in range(len(order_product)):
            productId = order_product[j].product_id_product
            productIds.append(productId)

        for k in range(0, len(productIds)):
            product = Product.query.filter_by(id=productIds[k]).first()
            quantity = OrderProduct.query.filter_by(
                product_id_product=productIds[k]).first()
            if product is not None and quantity is not None:
                total = product.price*quantity.quantity
                orders = {
                    "product": product.product,
                    "quantity": quantity.quantity
                }
                totals += total
                orderss.append(orders)

        response = {
            "id": id,
            "date": date,
            "order": [orderss],
            "total": totals
        }

        responseData.append(response)

    # date
    # products(list)
    # quantities(list)
    # totals

    return responseData

def getProducts():
    
    product = Product.query.filter_by(status=1).all()
    responseData = []
    print(product[0].product)
    for i in range(len(product)):
        id = product[i].id
        pname=product[i].product
        price=product[i].price
        response = {
            "id": id,
            "product": pname,
            "price": price
        }
        responseData.append(response)
    return responseData

def addProduct(pname,pprice):
    
    product = Product(product=pname,price=pprice,status=1)
    db.session.add(product)
    db.session.commit()


def modifyProduct(pid, pname, pprice):
    # product = Product.query.filter_by(id=pid).first()
    product = Product.query.filter_by(id=pid).update(dict(product=pname, price=pprice))
    # product.product = pname
    # product.price=pprice
    db.session.commit()

def deleteProduct(pid):

    product = Product.query.filter_by(id=pid).update(dict(status=0))
    db.session.commit()

def addOrder(uid, cash_o, ordi):

    order = Order(user_id_user=uid,date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),status=1, cash=cash_o)
    db.session.add(order)
    db.session.commit()
    for i in range(len(ordi)):

        prod=json.loads(ordi[i].replace("'",'"'))
        print(prod["id_product"])
        product=Product.query.filter_by(id=prod["id_product"]).first()
        order_product = OrderProduct(product_id_product=prod["id_product"],order_id_order=order.id,quantity=prod["quantity"],price=product.price)
        db.session.add(order_product)
    db.session.commit()

def deleteOrder(oid):

    order = Order.query.filter_by(id=oid).update(dict(status=0))
    
    order_product = OrderProduct.query.filter_by(order_id_order=oid).update(dict(status=0))
    
    db.session.commit()
