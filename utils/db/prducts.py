from utils.db.connect_db import curr,conn
from tabulate import tabulate
def search():
    while True:
        category = input("Qaysi Kategriya:  ")
        if not category:
            break
        with conn:
            sql_query = f"SELECT c.name,p.name,p.price,p.stock,p.discount_Precent,p.unit,p.dimensions, p.size, p.manufactured_date, p.Expiry_Date FROM Category c Join Products p ON c.id=p.category_id where c.name like '{category}%' "
            datas = curr.execute(sql_query).fetchall()

        headers = ['Category', 'Product', 'description', 'price', 'discount Precent', 'Stock', 'unit', 'dimensions',
                   'size', 'manufactured Date', 'Expiry Date', ]
        print(tabulate(datas, headers, 'grid'))
        return "Qidiruvdan chiqildi! "
def insert():
    name = input("Product name NOT NULL: ")
    if not name:
        raise ValueError("name bo'sh bo'lishi mumkin emas")

    description = input("Product desc: ")
    price = int(input("Product price: "))
    discount_precent = input("Product discount precent: ")
    stock = int(input("Product stock: "))
    unit = input('Product unit ("kg", "l", "g", "ml", "piece", "box") NOT NULL: ')
    if not unit:
        raise ValueError("uni bo'sh bo'lishi mumkin emas")

    weight = int(input('Product weight: '))
    dimensions = input('Product dimentions: ')
    size = input(
        "Product size ('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', '40', '42', '44', '46', '48', '50', '52', 'P', 'T') OR IS NULL: ")
    manufactured_date = input('Product manufactured_date: ')
    expiry_date = input('Product expiry_date: ')

    while True:
        category_name = input(f"{name} qaysi kategoriyaga mansub?: ")
        category_id = curr.execute(f"SELECT id FROM Category WHERE name like '{category_name}%'").fetchall()
        if len(category_id) > 1:
            print(f"Iltimos {name} categoriyasini aniqroq yozing!")
        else:
            print(category_id)
            category_id = category_id[0][0]
            print(category_id)
            break

    sql_query = (f"""INSERT INTO Products (category_id, name, description, price, discount_precent, stock, unit, weight, 
        dimensions, size, manufactured_date, expiry_date) VALUES ({category_id},  "{name}", "{description}", "{price}", 
        "{discount_precent}", "{stock}", "{unit}", "{weight}", "{dimensions}", "{size}", "{manufactured_date}", "{expiry_date}")""")

    with conn:
        curr.execute(sql_query)
    return  "Malumot saqlandi! "


while True:
    option=input("Qo`shish (s), Qidiruv(i),").lower()
    if not option:
        print("Operatsiya to`xtatildi! ")
        break
    elif option == 's':
        x=search()
        print(x)
        continue
    elif option == 'i':
        x=insert()
        print(x)
        continue
    else:
       print ("Noto`g`ri peratsiya tanladingiz! ")

