#!/usr/bin/env python3
from locale import atoi
import os

from bottle import route, run, template, request, redirect, response, FormsDict
from bottle import static_file
from db import Data


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='F:\progMy\cifrovik')


@route("/contacts")
def contacts():
    content = template("contacts.tpl")
    return template("template.tpl", title='Про мене', content=content)


@route('/:name', method="GET")
def show_product(name):
    if request.GET.get("save", "").strip():
        name_c = request.GET.get("comment_name", '').strip().encode('latin1').decode('utf8')
        text = request.GET.get("comment_text", '').strip().encode('latin1').decode('utf8')
        dat = Data("templates/products.db")
        dat.ins_com(name, name_c, text)
        dat.con.commit()
        dat.con.close()
        redirect('/' + name)
    data = Data("templates/products.db")
    name = str(name)
    data.select(name)
    img, name, price, about = data.rows[4], data.rows[1], data.rows[2], data.rows[3]
    comments = template('comments.tpl', app=name)
    content = template('product.tpl', img=img, name=name, price=price, about=about, other=comments)
    data.con.close()
    return template("template.tpl", title=name, content=content)


# @route('/:name', method="GET")
# def set_comment(name):
#     if request.GET.get("save", "").strip():
#         name_c = request.GET.get("name", "").strip()
#         text = request.GET.get("text", "").strip()
#         data = Data("templates/products.db")
#         data.ins_com(name_c, text)
#         redirect("/" + name)


@route('/products', method="GET")
def index():
    if request.GET.get("filter", "").strip():
        price_from = atoi(request.GET.get("from", '').strip())
        price_to = atoi(request.GET.get("to", '').strip())
        nik = "Nikon" if request.GET.get("Nikon", '').strip() else "*/*////***/*"
        can = "Canon" if request.GET.get("Canon", '').strip() else "*/*////***/*"
        sams = "Samsung" if request.GET.get("Samsung", '').strip() else "*/*////***/*"
        if not price_to:
            price_to = 65536
        price = [price_from, price_to]
        firms = [price_to, nik, can, sams]
        content = template('products_filtered.tpl', firms=firms, price=price)
        return template("template.tpl", title='Товари', content=content)
    if request.GET.get("search", "").strip():
        print("greger rwth wh hethweh h w5hyw56yh")
        word = request.GET.get("search", '').strip()
        content = template('products_search.tpl', word=word)
        return template("template.tpl", title='Товари', content=content)
    content = template('products.tpl')
    return template("template.tpl", title='Товари', content=content)


if __name__ == "__main__":
    run(host='127.0.0.1', port=8080)
