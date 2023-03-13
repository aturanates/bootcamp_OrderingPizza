"""
Turan Ates
aturanatess@gmail.com

"""
import pizza_ordering
import datetime
import csv
import time


menu_file = open("menu.txt","r",encoding="utf-8")
print(menu_file.read())
cost = 0
name = str()
while True:
    print("""
    ***ADA Pizza***
    1:Menu
    2:Çıkış
    ***************
    """)
    choice = input("Hoşgeldiniz. İşlem seçiniz:")
    if choice == "1":
        menu_file = open("menu.txt", "r", encoding="utf-8")
        print(menu_file.read())
        print("Size ne ikram edebiliriz?:")
        choice_menu = input()
        if choice_menu == "1":
            pizza = pizza_ordering.Classic()
            print(pizza_ordering.Classic)
            cost += pizza.get_cost()
            name += pizza.get_description()
            print(menu_file.read())
            print("Eklemek istediğiniz Sosu Seçin")
            choice_souce = input()
            try:
                if choice_souce == "11":
                    name = pizza_ordering.Olives.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "12":
                    name = pizza_ordering.Mushrooms.get_description()
                    cost += pizza_ordering.Mushrooms.get_cost()
                elif choice_souce == "13":
                    name = pizza_ordering.GoatCheese.get_description()
                    cost += pizza_ordering.GoatCheese.get_cost()
                elif choice_souce == "14":
                    name = pizza_ordering.Meat.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "15":
                    name = pizza_ordering.Onions.get_description()
                    cost += pizza_ordering.Onions.get_cost()
                elif choice_souce == "16":
                    name = pizza_ordering.Corn.get_description()
                    cost += pizza_ordering.Corn.get_cost()
                print("Ödemeye Geçmek İçin Bilgilerinizi Girin:")
                cust_name = input("İsminizi girin:")
                cust_tc = input("TC girin:")
                cust_kart = input("Kredi Kartı No girin:")
                cust_sifre = input("Şifre Girin:")

                with open('Orders_Database.csv', 'w', newline='') as csvfile:
                    fieldnames = ["Tarih","Isim", "TC","Kredi Karti No","Sifre","Pizza","Tutar"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow({'Tarih': datetime.date, 'Isim': cust_name, "TC": cust_tc, "Kredi Karti No": cust_kart, "Sifre": cust_sifre, "Pizza": name, "Tutar": cost})
            except:
                print("Sistem Arızası...")
                time.sleep(5)
                print("Bu işlem biraz sürebilir..")
                time.sleep(10)
        if choice_menu == "2":
            pizza = pizza_ordering.Margherita()
            print(pizza_ordering.Margherita)
            name += pizza.get_description()
            cost += pizza.get_cost()
            print(menu_file.read())
            print("Eklemek istediğiniz Sosu Seçin")
            choice_souce = input()
            try:
                if choice_souce == "11":
                    name = pizza_ordering.Olives.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "12":
                    name = pizza_ordering.Mushrooms.get_description()
                    cost += pizza_ordering.Mushrooms.get_cost()
                elif choice_souce == "13":
                    name = pizza_ordering.GoatCheese.get_description()
                    cost += pizza_ordering.GoatCheese.get_cost()
                elif choice_souce == "14":
                    name = pizza_ordering.Meat.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "15":
                    name = pizza_ordering.Onions.get_description()
                    cost += pizza_ordering.Onions.get_cost()
                elif choice_souce == "16":
                    name = pizza_ordering.Corn.get_description()
                    cost += pizza_ordering.Corn.get_cost()
                print("Ödemeye Geçmek İçin Bilgilerinizi Girin:")
                cust_name = input("İsminizi girin:")
                cust_tc = input("TC girin:")
                cust_kart = input("Kredi Kartı No girin:")
                cust_sifre = input("Şifre Girin:")

                with open('Orders_Database.csv', 'w', newline='') as csvfile:
                    fieldnames = ["Tarih", "Isim", "TC", "Kredi Karti No", "Sifre", "Pizza", "Tutar"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow(
                        {'Tarih': datetime.date, 'Isim': cust_name, "TC": cust_tc, "Kredi Karti No": cust_kart,
                         "Sifre": cust_sifre, "Pizza": name, "Tutar": cost})
            except:
                print("Sistem Arızası...")
                time.sleep(5)
                print("Bu işlem biraz sürebilir..")
                time.sleep(10)
        if choice_menu == "3":
            pizza = pizza_ordering.TurkishPizza()
            print(pizza_ordering.TurkishPizza)
            name += pizza.get_description()
            cost += pizza.get_cost()
            print(menu_file.read())
            print("Eklemek istediğiniz Sosu Seçin")
            choice_souce = input()
            try:
                if choice_souce == "11":
                    name = pizza_ordering.Olives.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "12":
                    name = pizza_ordering.Mushrooms.get_description()
                    cost += pizza_ordering.Mushrooms.get_cost()
                elif choice_souce == "13":
                    name = pizza_ordering.GoatCheese.get_description()
                    cost += pizza_ordering.GoatCheese.get_cost()
                elif choice_souce == "14":
                    name = pizza_ordering.Meat.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "15":
                    name = pizza_ordering.Onions.get_description()
                    cost += pizza_ordering.Onions.get_cost()
                elif choice_souce == "16":
                    name = pizza_ordering.Corn.get_description()
                    cost += pizza_ordering.Corn.get_cost()
                print("Ödemeye Geçmek İçin Bilgilerinizi Girin:")
                cust_name = input("İsminizi girin:")
                cust_tc = input("TC girin:")
                cust_kart = input("Kredi Kartı No girin:")
                cust_sifre = input("Şifre Girin:")

                with open('Orders_Database.csv', 'w', newline='') as csvfile:
                    fieldnames = ["Tarih", "Isim", "TC", "Kredi Karti No", "Sifre", "Pizza", "Tutar"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow(
                        {'Tarih': datetime.date, 'Isim': cust_name, "TC": cust_tc, "Kredi Karti No": cust_kart,
                         "Sifre": cust_sifre, "Pizza": name, "Tutar": cost})
            except:
                print("Sistem Arızası...")
                time.sleep(5)
                print("Bu işlem biraz sürebilir..")
                time.sleep(10)
        if choice_menu == "4":
            pizza = pizza_ordering.DominosPizza()
            print(pizza_ordering.DominosPizza)
            name += pizza.get_description()
            cost += pizza.get_cost()
            print(menu_file.read())
            print("Eklemek istediğiniz Sosu Seçin")
            choice_souce = input()
            try:
                if choice_souce == "11":
                    name = pizza_ordering.Olives.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "12":
                    name = pizza_ordering.Mushrooms.get_description()
                    cost += pizza_ordering.Mushrooms.get_cost()
                elif choice_souce == "13":
                    name = pizza_ordering.GoatCheese.get_description()
                    cost += pizza_ordering.GoatCheese.get_cost()
                elif choice_souce == "14":
                    name = pizza_ordering.Meat.get_description()
                    cost += pizza_ordering.Olives.get_cost()
                elif choice_souce == "15":
                    name = pizza_ordering.Onions.get_description()
                    cost += pizza_ordering.Onions.get_cost()
                elif choice_souce == "16":
                    name = pizza_ordering.Corn.get_description()
                    cost += pizza_ordering.Corn.get_cost()
                print("Ödemeye Geçmek İçin Bilgilerinizi Girin:")
                cust_name = input("İsminizi girin:")
                cust_tc = input("TC girin:")
                cust_kart = input("Kredi Kartı No girin:")
                cust_sifre = input("Şifre Girin:")

                with open('Orders_Database.csv', 'w', newline='') as csvfile:
                    fieldnames = ["Tarih", "Isim", "TC", "Kredi Karti No", "Sifre", "Pizza", "Tutar"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerow(
                        {'Tarih': datetime.date, 'Isim': cust_name, "TC": cust_tc, "Kredi Karti No": cust_kart,
                         "Sifre": cust_sifre, "Pizza": name, "Tutar": cost})
                    break
            except:
                print("Sistem Arızası...")
                time.sleep(5)
                print("Bu işlem biraz sürebilir..")
                time.sleep(10)
                break


    elif choice == "2":
        print("Yine bekleriz.")
        break
    else:
        print("Geçersiz İşlem")
        continue


