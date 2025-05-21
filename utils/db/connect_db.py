import sqlite3


from aiohttp.web_routedef import delete

url= "/Users/pcmci-tech/bot.uz/bot.uz.db"
conn= sqlite3.connect(url)
curr=conn.cursor()

def get_all():
    sql_query = f'SELECT * FROM User'
    datas = curr.execute(sql_query).fetchall()
    return datas


def who_is_by_id(id):
    sql_query = f"SELECT * FROM User WHERE id=?;"
    data = curr.execute(sql_query, (id, )).fetchall()
    return data

def who_is(first_name):
    sql_query = f"SELECT * FROM User WHERE first_name='{first_name}';"
    data = curr.execute(sql_query).fetchall()
    return data




# Uyga Vaizfa:
# 1. Kitobni yoki Userni like operatori orqali o'xshashlarini qiridradigan query yozish.
# 2. Databasega Yangi foydalanuvchini python orqali qo'shadigan qilish
# 3. Databasedagi biror bir userni ma'lumotini yangilaydigan query yozish
# 4. Userni yoki Books ni o'chiradigan query yozish.

# 1 Uy ishi
# char = input("Qaysi harf bilan boshlanuvchi ismlar kerak?\nBelgi:")
#
# sql_query = f"SELECT * FROM User WHERE first_name like '{char}%';"
# datas = curr.execute(sql_query).fetchall()
#
# for data in datas:
#     print(data)
#
# if not datas:
#     print("Foydalunvchilar topilmadi!")


# sql_query = """INSERT INTO User (first_name, last_name, phone, birthday, address, email, passport)
# VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');
# """ % (first_name, last_name, phone, birthday, address, email, passport)

# sql_query = """INSERT INTO User (first_name, last_name, phone, birthday, address, email, passport)
# VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}');
# """.format(first_name, last_name, phone, birthday, address, email, passport)
#

# 2-uy ishi

def insert_user(first_name, last_name, phone, birthday, address, email, passport):
    sql_query = f"""INSERT INTO User (first_name, last_name, phone, birthday, address, email, passport)
     VALUES ('{first_name}', '{last_name}', '{phone}', '{birthday}', '{address}', '{email}', '{passport}');
    """
    curr.execute(sql_query)
    conn.commit()
    curr.close()
    print('Ma`lumot saqlandi!')


def delete_user(id):
    user =who_is_by_id(id)
    if user:
        print(user)
        confirm= input("O`chirilgan tasdiqlaysizmi? (y/n):")
        match confirm.lower():
            case 'y':
                sql_query="""DELETE FROM User WHERE id=?"""
                with conn:
                   curr.execute(sql_query,(id,))
                print(f"{id} li user muvoffaqiyatli o`chiriladi!")
            case 'n':
                print("Buyruq bekor qilindi!")
            case _:
                print("Bunday operatsiya mavjud emas! ")
    else:
        print(f"{id}-id lik shaxs topilmadi!")

def update_user(id, first_name):
    user = who_is_by_id(id,)
    if user:
        print(user)
        confirm = input("O`zgartirish kiritasizmi? (t/f):")
        match confirm.lower():
            case 't':
                sql_query = """UPDATE User SET first_name=? WHERE id=?"""
                with conn:
                    curr.execute(sql_query, (first_name, id))
                print(f"{id} li user muvoffaqiyatli o`zgartiriladi!")
            case 'f':
                print("Buyruq bekor qilindi!")
            case _:
                print("Bunday operatsiya mavjud emas! ")
    else:
        print(f"{id}-id lik shaxs topilmadi!")




# sql_query = """SELECT COUNT(*) FROM User;"""
# followers = curr.execute(sql_query).fetchone()
# followers = followers[0] if followers else 0
# print(f"User jadvalda {followers} ta obunachi bor.")


if __name__ =='__main__':
   # ------ BARCHA MA'LUMOTNI OLISH
   #  datas = get_all()
   #  print(datas)
   #
   #  # ------ ISM QIDIRISH
   #  who = input("Kim?: ")
   #  data = who_is_by_id(id)
   #  print(data)
   #  #
   #  # # ----- INSERT INTO
   #  # # ----- START
   #  first_name = input("First name?: ")
    # last_name = input("Last name?: ")
    # phone = input("Phone?: ")
    # birthday = input("Birthday (dd.mm.yyyy)?: ")
    # address = input("Address?: ")
    # email = input("Email?: ")
    # passport = input("Passport?: ")
    # insert_user(first_name, last_name, phone, birthday, address, email, passport)
    # ----- END```
    update_user(5,"ubaydullayev")
