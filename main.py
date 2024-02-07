import mysql.connector
from datetime import datetime
from statistics import mean
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="calorie_counter"
)
cursor = conn.cursor()

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS calorie_counter")
    cursor.execute("USE calorie_counter")

def create_food_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS food (f_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) UNIQUE, calories INT, cat varchar(255), meal varchar(255), cusine varchar(255))")
    foods = [("Apple", 52, "vitamin", "breakfast", "american"),
            ("Banana", 89, "vitamin", "breakfast", "american"),
            ("Chicken Breast", 165, "protein", "dinner", "american"),
            ("Egg", 70, "protein", "breakfast", "american"),
            ("Salmon", 208, "protein", "dinner", "american"),
            ("Pasta", 131, "carbohydrate", "lunch", "italian"),
            ("Rice", 130, "carbohydrate", "lunch", "chinese"),
            ("Broccoli", 31, "vitamin", "dinner", "american"),
            ("Avocado", 160, "fat", "breakfast", "mexican"),
            ("Almonds", 7, "fat", "snack", "american"),
            ("Yogurt", 159, "protein", "breakfast", "greek"),
            ("Spinach", 23, "vitamin", "lunch", "american"),
            ("Steak", 271, "protein", "dinner", "american"),
            ("Orange", 62, "vitamin", "breakfast", "american"),
            ("Milk", 103, "protein", "breakfast", "american"),
            ("Carrot", 41, "vitamin", "lunch", "american"),
            ("Blueberries", 85, "vitamin", "breakfast", "american"),
            ("Potato", 163, "carbohydrate", "dinner", "american"),
            ("Quinoa", 120, "carbohydrate", "lunch", "south american"),
            ("Turkey Breast", 135, "protein", "lunch", "american"),
            ("Honey", 64, "carbohydrate", "breakfast", "american"),
            ("Olive Oil", 119, "fat", "dinner", "mediterranean"),
            ("Lentils", 230, "protein", "lunch", "indian"),
            ("Tofu", 94, "protein", "dinner", "chinese"),
            ("Bread", 79, "carbohydrate", "breakfast", "american"),
            ("Peanut Butter", 188, "fat", "breakfast", "american"),
            ("Green Beans", 31, "vitamin", "dinner", "american"),
            ("Cheese", 113, "protein", "lunch", "american"),
            ("Cucumber", 16, "vitamin", "lunch", "greek"),
            ("Tomato", 18, "vitamin", "lunch", "greek"),
            ("Watermelon", 46, "vitamin", "dessert", "american"),
            ("Beef", 250, "protein", "dinner", "american"),
            ("Onion", 40, "vitamin", "dinner", "american"),
            ("Cauliflower", 25, "vitamin", "dinner", "american"),
            ("Chickpeas", 269, "protein", "lunch", "indian"),
            ("Pineapple", 50, "vitamin", "dessert", "american"),
            ("Coconut Oil", 117, "fat", "dinner", "thai"),
            ("Shrimp", 85, "protein", "dinner", "chinese"),
            ("Cashews", 155, "fat", "snack", "indian"),
            ("Peanuts", 166, "fat", "snack", "american"),
            ("Celery", 6, "vitamin", "lunch", "american"),
            ("Grapes", 69, "vitamin", "snack", "american"),
            ("Mushrooms", 15, "vitamin", "dinner", "chinese"),
            ("Soy Milk", 80, "protein", "breakfast", "chinese"),
            ("Cheddar Cheese", 402, "protein", "lunch", "american"),
            ("Oats", 68, "carbohydrate", "breakfast", "american"),
            ("Asparagus", 20, "vitamin", "dinner", "french"),
            ("Hummus", 166, "protein", "lunch", "mediterranean"),
            ("Cottage Cheese", 98, "protein", "breakfast", "american"),
            ("Sardines", 208, "protein", "lunch", "mediterranean"),
            ("Bell Pepper", 31, "vitamin", "lunch", "american"),
            ("Salad Dressing", 120, "fat", "lunch", "american"),
            ("Eggplant", 25, "vitamin", "dinner", "italian"),
            ("Sausage", 268, "protein", "breakfast", "american"),
            ("Cherries", 50, "vitamin", "dessert", "american"),
            ("Salami", 336, "protein", "lunch", "italian"),
            ("Bacon", 43, "fat", "breakfast", "american"),
            ("Peaches", 59, "vitamin", "dessert", "american"),
            ("Sour Cream", 193, "fat", "dinner", "american"),
            ("Apricots", 48, "vitamin", "breakfast", "american"),
            ("Zucchini", 20, "vitamin", "dinner", "italian"),
            ("Parmesan Cheese", 122, "protein", "dinner", "italian"),
            ("Raisins", 299, "carbohydrate", "snack", "american"),
            ("Lemon", 17, "vitamin", "breakfast", "american"),
            ("Hazelnuts", 628, "fat", "snack", "american"),
            ("Cabbage", 22, "vitamin", "dinner", "american"),
            ("Flour", 364, "carbohydrate", "baking", "american"),
            ("Whole Wheat Bread", 247, "carbohydrate", "breakfast", "american"),
            ("Chia Seeds", 486, "fat", "breakfast", "american"),
            ("Coconut Milk", 230, "fat", "dinner", "thai"),
            ("Sunflower Seeds", 584, "fat", "snack", "american"),
            ("Feta Cheese", 264, "protein", "salad", "greek"),
            ("Popcorn", 382, "carbohydrate", "snack", "american"),
            ("Tuna", 144, "protein", "lunch", "american"),
            ("Brown Rice", 112, "carbohydrate", "lunch", "chinese"),
            ("Walnuts", 654, "fat", "snack", "american"),
            ("Barley", 354, "carbohydrate", "dinner", "american"),
            ("Pumpkin Seeds", 285, "fat", "snack", "american"),
            ("Cranberries", 46, "vitamin", "breakfast", "american"),
            ("Black Beans", 339, "protein", "lunch", "mexican"),
            ("Rye Bread", 259, "carbohydrate", "breakfast", "german"),
            ("Haddock", 90, "protein", "dinner", "american"),
            ("Lima Beans", 216, "protein", "dinner", "american"),
            ("Pistachios", 562, "fat", "snack", "middle eastern"),
            ("Artichoke", 47, "vitamin", "appetizer", "mediterranean"),
            ("Dates", 282, "carbohydrate", "snack", "middle eastern"),
            ("Bulgur", 151, "carbohydrate", "lunch", "middle eastern"),
            ("Mozzarella Cheese", 280, "protein", "lunch", "italian"),
            ("Swiss Cheese", 380, "protein", "lunch", "swiss"),
            ("Macadamia Nuts", 718, "fat", "snack", "hawaiian"),
            ("Brussels Sprouts", 43, "vitamin", "dinner", "belgian"),
            ("Kidney Beans", 333, "protein", "lunch", "american"),
            ("Cottage Cheese (Low Fat)", 72, "protein", "breakfast", "american"),
            ("Gouda Cheese", 356, "protein", "lunch", "dutch"),
            ("Cantaloupe", 34, "vitamin", "breakfast", "american"),
            ("Canned Tuna", 116, "protein", "lunch", "american"),
            ("Canned Salmon", 165, "protein", "lunch", "american"),
            ("Salmon (Smoked)", 117, "protein", "lunch", "american"),
            ("Olive Oil (Extra Virgin)", 884, "fat", "dinner", "mediterranean"),
            ("Beef Jerky", 410, "protein", "snack", "american"),
            ("Chocolate (Dark)", 604, "carbohydrate", "dessert", "american"),
            ("Poppy Seeds", 525, "fat", "baking", "middle eastern"),
            ("White Rice", 129, "carbohydrate", "lunch", "chinese"),
            ("Balsamic Vinegar", 88, "vitamin", "salad", "italian"),
            ("Pork", 242, "protein", "dinner", "american"),
            ("Sesame Seeds", 573, "fat", "snack", "asian"),
            ("Peanut Oil", 884, "fat", "cooking", "american"),
            ("Maple Syrup", 260, "carbohydrate", "breakfast", "american"),
            ("Granola", 471, "carbohydrate", "breakfast", "american"),
            ("Soy Sauce", 61, "sodium", "dinner", "chinese"),
            ("Honeydew Melon", 36, "vitamin", "breakfast", "american"),
            ("Peanut Brittle", 529, "fat", "snack", "american"),
            ("Kale", 49, "vitamin", "lunch", "american"),
            ("Wheat Germ", 338, "vitamin", "breakfast", "american"),
            ("Brie Cheese", 334, "protein", "appetizer", "french"),
            ("Pesto Sauce", 303, "fat", "dinner", "italian"),
            ("Soybeans", 446, "protein", "dinner", "chinese"),
            ("Couscous", 176, "carbohydrate", "lunch", "north african"),
            ("Fig", 107, "vitamin", "snack", "mediterranean"),
            ("Lentil Soup", 143, "protein", "lunch", "indian"),
            ("Hamburger", 254, "protein", "lunch", "american"),
            ("Corn", 96, "carbohydrate", "dinner", "american"),
            ("Wheat Bread", 256, "carbohydrate", "breakfast", "american"),
            ("Pork Sausage", 321, "protein", "breakfast", "american"),
            ("Cornbread", 198, "carbohydrate", "dinner", "american"),
            ("Cheddar Cheese (Low Fat)", 173, "protein", "lunch", "american"),
            ("Beef Stew", 155, "protein", "dinner", "american"),
            ("Cereal", 379, "carbohydrate", "breakfast", "american"),
            ("Pork Chop", 185, "protein", "dinner", "american"),
            ("Guacamole", 140, "fat", "appetizer", "mexican"),
            ("Bagel", 289, "carbohydrate", "breakfast", "american"),
            ("Pita Bread", 275, "carbohydrate", "lunch", "mediterranean"),
            ("Cornflakes", 363, "carbohydrate", "breakfast", "american"),
            ("Muesli", 289, "carbohydrate", "breakfast", "swiss"),
            ("Pork Ribs", 369, "protein", "dinner", "american"),
            ("Shredded Wheat", 210, "carbohydrate", "breakfast", "american"),
            ("Cauliflower Rice", 25, "carbohydrate", "dinner", "american"),
            ("Cabbage Soup", 33, "vitamin", "lunch", "eastern european"),
            ("Pumpkin Pie", 243, "carbohydrate", "dessert", "american"),
            ("Beef Steak", 219, "protein", "dinner", "american"),
            ("Rice Cake", 35, "carbohydrate", "snack", "asian"),
            ("Beef Ribs", 318, "protein", "dinner", "american"),
            ("Chicken Soup", 63, "protein", "lunch", "american"),
            ("Taco Shell", 57, "carbohydrate", "dinner", "mexican"),
            ("Gingerbread", 343, "carbohydrate", "dessert", "german"),
            ("Chicken Leg", 209, "protein", "dinner", "american"),
            ("Chicken Thigh", 250, "protein", "dinner", "american"),
            ("Chicken Wing", 203, "protein", "appetizer", "american"),
            ("Oyster Sauce", 19, "sodium", "dinner", "chinese"),
            ("Clam", 86, "protein", "dinner", "american"),
            ("Lobster", 89, "protein", "dinner", "american"),
            ("Crab", 83, "protein", "dinner", "american"),
            ("Caviar", 264, "fat", "appetizer", "russian"),
            ("Octopus", 82, "protein", "dinner", "mediterranean"),
            ("Calamari", 80, "protein", "dinner", "italian"),
            ("Mussels", 73, "protein", "dinner", "belgian"),
            ("Scallops", 69, "protein", "dinner", "french"),
            ("Breaded Fish", 273, "carbohydrate", "dinner", "british"),
            ("Fried Fish", 232, "fat", "dinner", "southern"),
            ("Fish Fillet", 124, "protein", "dinner", "american"),
            ("Fish Stick", 237, "carbohydrate", "dinner", "american"),
            ("Sushi", 129, "protein", "dinner", "japanese"),
            ("Nori Seaweed", 7, "vitamin", "dinner", "japanese"),
            ("Ramen Noodles", 188, "carbohydrate", "lunch", "japanese"),
            ("Udon Noodles", 151, "carbohydrate", "lunch", "japanese"),
            ("Soba Noodles", 113, "carbohydrate", "lunch", "japanese"),
            ("Egg Noodles", 138, "carbohydrate", "lunch", "chinese"),
            ("Spaghetti", 157, "carbohydrate", "dinner", "italian"),
            ("Fusilli Pasta", 154, "carbohydrate", "dinner", "italian"),
            ("Macaroni Pasta", 159, "carbohydrate", "dinner", "american"),
            ("Lasagna", 133, "carbohydrate", "dinner", "italian"),
            ("Ravioli", 93, "carbohydrate", "dinner", "italian"),
            ("Tortellini", 101, "carbohydrate", "dinner", "italian"),
            ("Fettuccine", 210, "carbohydrate", "dinner", "italian"),
            ("Pizza", 266, "carbohydrate", "dinner", "italian"),
            ("Cheeseburger", 303, "protein", "lunch", "american"),
            ("Hot Dog", 151, "protein", "lunch", "american"),
            ("Fried Chicken", 266, "protein", "dinner", "southern"),
            ("Chicken Nuggets", 300, "protein", "lunch", "american"),
            ("French Fries", 312, "carbohydrate", "lunch", "american"),
            ("Onion Rings", 403, "carbohydrate", "appetizer", "american"),
            ("Potato Chips", 536, "carbohydrate", "snack", "american"),
            ("Pretzels", 386, "carbohydrate", "snack", "german"),
            ("Corn Chips", 509, "carbohydrate", "snack", "mexican"),
            ("Popcorn (Microwaved)", 387, "carbohydrate", "snack", "american"),
            ("Nachos", 393, "carbohydrate", "appetizer", "mexican"),
            ("Salsa", 36, "vitamin", "dip", "mexican"),
            ("Tartar Sauce", 120, "fat", "dip", "american"),
            ("Mayonnaise", 680, "fat", "sandwich", "american"),
            ("Ketchup", 101, "sodium", "dip", "american"),
            ("Barbecue Sauce", 234, "sugar", "marinade", "american"),
            ("Teriyaki Sauce", 89, "sodium", "marinade", "japanese"),
            ("Soybean Paste", 198, "protein", "cooking", "asian"),
            ("Worcestershire Sauce", 66, "sodium", "cooking", "british"),
            ("Tabasco Sauce", 27, "vitamin", "cooking", "american"),
            ("Hollandaise Sauce", 357, "fat", "breakfast", "french"),
            ("Tzatziki", 59, "fat", "dip", "greek"),
            ("Ranch Dressing", 457, "fat", "salad", "american"),
            ("Blue Cheese Dressing", 321, "fat", "salad", "american"),
            ("Caesar Dressing", 283, "fat", "salad", "italian"),
            ("Thousand Island Dressing", 350, "fat", "salad", "american"),
            ("Italian Dressing", 266, "fat", "salad", "italian"),
            ("French Dressing", 373, "fat", "salad", "french"),
            ("Russian Dressing", 344, "fat", "salad", "russian"),
            ("Catalina Dressing", 286, "fat", "salad", "american"),
            ("Honey Mustard Dressing", 318, "fat", "salad", "american"),
            ("Balsamic Vinaigrette", 323, "fat", "salad", "italian"),
            ("Peanut Sauce", 350, "fat", "dinner", "thai"),
            ("Sour Cream Dip", 130, "fat", "appetizer", "american"),
            ("Guacamole Dip", 152, "fat", "appetizer", "mexican"),
            ("Hummus Dip", 177, "protein", "appetizer", "mediterranean"),
            ("Bean Dip", 117, "protein", "appetizer", "mexican"),
            ("Taramasalata Dip", 180, "fat", "appetizer", "greek"),
            ("Spinach Dip", 150, "fat", "appetizer", "american"),
            ("Cheese Dip", 194, "fat", "appetizer", "american"),
            ("Salsa Dip", 36, "vitamin", "appetizer", "mexican"),
            ("Clam Dip", 150, "fat", "appetizer", "american"),
            ("Crab Dip", 170, "fat", "appetizer", "american"),
            ("Chili Dip", 168, "fat", "appetizer", "american"),
            ("Buffalo Chicken Dip", 319, "protein", "appetizer", "american"),
            ("Queso Dip", 162, "fat", "appetizer", "mexican"),
            ("Fondue", 224, "fat", "dinner", "swiss"),
            ("Chocolate Fondue", 313, "carbohydrate", "dessert", "swiss"),
            ("Caramel Sauce", 322, "carbohydrate", "dessert", "american"),
            ("Butterscotch Sauce", 332, "carbohydrate", "dessert", "british"),
            ("Chocolate Syrup", 180, "carbohydrate", "dessert", "american"),
            ("Ice Cream", 207, "carbohydrate", "dessert", "american"),
            ("Frozen Yogurt", 159, "carbohydrate", "dessert", "american"),
            ("Sorbet", 96, "carbohydrate", "dessert", "french"),
            ("Gelato", 200, "carbohydrate", "dessert", "italian"),
            ("Sherbet", 144, "carbohydrate", "dessert", "american"),
            ("Milkshake", 175, "carbohydrate", "dessert", "american"),
            ("Smoothie", 125, "vitamin", "breakfast", "american"),
            ("Chocolate Milk", 190, "carbohydrate", "beverage", "american"),
            ("Eggnog", 135, "protein", "beverage", "american"),
            ("Hot Chocolate", 192, "carbohydrate", "beverage", "american"),
            ("Coffee", 2, "vitamin", "beverage", "american"),
            ("Tea", 0, "vitamin", "beverage", "british"),
            ("Green Tea", 1, "vitamin", "beverage", "asian"),
            ("Black Tea", 1, "vitamin", "beverage", "british"),
            ("Herbal Tea", 0, "vitamin", "beverage", "asian"),
            ("Fruit Tea", 1, "vitamin", "beverage", "asian"),
            ("Milk Tea", 43, "protein", "beverage", "british"),
            ("Bubble Tea", 160, "carbohydrate", "beverage", "taiwanese"),
            ("Iced Tea", 31, "vitamin", "beverage", "american"),
            ("Cola", 105, "carbohydrate", "beverage", "american"),
            ("Soda", 44, "carbohydrate", "beverage", "american"),
            ("Lemonade", 99, "vitamin", "beverage", "american"),
            ("Orange Juice", 45, "vitamin", "beverage", "american"),
            ("Apple Juice", 45, "vitamin", "beverage", "american"),
            ("Grape Juice", 60, "vitamin", "beverage", "american"),
            ("Cranberry Juice", 46, "vitamin", "beverage", "american"),
            ("Tomato Juice", 17, "vitamin", "beverage", "american"),
            ("Pineapple Juice", 53, "vitamin", "beverage", "american"),
            ("Carrot Juice", 39, "vitamin", "beverage", "american"),
            ("Coconut Water", 19, "vitamin", "beverage", "thai"),
            ("Almond Milk", 17, "protein", "beverage", "american"),
            ("Soy Milk", 80, "protein", "beverage", "chinese"),
            ("Rice Milk", 47, "carbohydrate", "beverage", "asian"),
            ("Oat Milk", 50, "carbohydrate", "beverage", "american"),
            ("Cashew Milk", 25, "fat", "beverage", "american"),
            ("Hazelnut Milk", 28, "fat", "beverage", "american"),
            ("Coconut Milk", 230, "fat", "beverage", "thai"),
            ("Hemp Milk", 70, "fat", "beverage", "american"),
            ("Flax Milk", 50, "fat", "beverage", "american"),
            ("Quinoa Milk", 48, "carbohydrate", "beverage", "south american")]

    cursor.executemany("INSERT IGNORE INTO food (name, calories, cat, meal, cusine) VALUES (%s, %s, %s, %s, %s)", foods)

def create_user_list_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS user_list (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255))")

def create_month_table(month):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {month} (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), food_item VARCHAR(255), calories INT, time_consumed DATETIME, cat varchar(255), meal varchar(255), cusine varchar(255))")

def create_count_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS count (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), timestamp DATETIME)")

def admin_sign_in():
    admin_username = "admin"
    admin_password = "admin123"
    entered_username = input("Enter admin username: ")
    entered_password = input("Enter admin password: ")
    if entered_username == admin_username and entered_password == admin_password:
        return True
    else:
        print("Invalid admin credentials.")
        return False

def admin_report():
    print("Admin Report Options:")
    print("1. Date")
    print("2. Month")
    print("3. Year")
    admin_option = int(input("Enter option: "))
    current_month = datetime.now().strftime("%B_%Y")
    create_month_table(current_month)
    if admin_option == 1:

        date = input("Enter date (YYYY-MM-DD): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE DATE(time_consumed) = '{date}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active on {date} are {records[0][0]}")

    elif admin_option == 2:
        month = input("Enter month (MM-YYYY): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE DATE_FORMAT(time_consumed, '%m-%Y') = '{month}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active in month {month} are {records[0][0]}")

    elif admin_option == 3:
        year = input("Enter year (YYYY): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE YEAR(time_consumed) = '{year}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active in year {year} are {records[0][0]}")

def main():
    create_database()
    create_food_table()
    create_user_list_table()
    create_count_table()

    print("Welcome to the Calorie Counter!")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Admin Sign In")

    user_option = int(input("Enter option: "))

    if user_option == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        sign_in_query = f"SELECT * FROM user_list WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(sign_in_query)
        user = cursor.fetchone()
        if user:
            print("Sign In Successful!")
            current_month = datetime.now().strftime("%B_%Y")
            create_month_table(current_month)
            while True:
                print("1. Add food item")
                print("2. Update a record")
                print("3. Delete a record")
                print("4. Log Out")
                print("5. See Reports")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    food_name = input("Enter food name: ")
                    check_food_query = f"SELECT * FROM food WHERE name = '{food_name}'"
                    cursor.execute(check_food_query)
                    food = cursor.fetchone()
                    if food:
                        calories = food[2]
                        cat = food[3]
                        meal = food[4]
                        cusine = food[5]
                        time_consumed = input("Enter the time consumed (YYYY-MM-DD HH:MM:SS): ")
                        add_food_query = f"INSERT INTO {current_month} (username, food_item, calories, time_consumed, cat, meal, cusine) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(add_food_query, (username, food_name, calories, time_consumed, cat, meal, cusine))
                        conn.commit()
                        print("Food item added successfully!")
                    else:
                        print("Invalid food item.")

                elif user_choice == 2:
                    print("Update Record:")
                    view_records_query = f"SELECT id, food_item, calories, time_consumed FROM {current_month} WHERE username = '{username}'"
                    cursor.execute(view_records_query)
                    records = cursor.fetchall()

                    if records:
                        print("Existing Records:")
                        for record in records:
                            print(f"ID: {record[0]}, Food: {record[1]}, Calories: {record[2]}, Time Consumed: {record[3]}")

                        record_id = int(input("Enter the ID of the record you want to update: "))
                        new_food_name = input("Enter new food name : ")
                        new_calories = int(input("Enter new calories : "))
                        new_time_consumed = input("Enter new time consumed (YYYY-MM-DD HH:MM:SS): ")

                        update_query = f"UPDATE {current_month} SET food_item = COALESCE(%s, food_item), calories = COALESCE(%s, calories), time_consumed = COALESCE(%s, time_consumed) WHERE id = %s AND username = '{username}'"
                        cursor.execute(update_query, (new_food_name, new_calories, new_time_consumed, record_id))
                        conn.commit()
                        print("Record updated successfully!")

                    else:
                        print("No records found to update.")

                elif user_choice == 3:
                    print("Delete Record:")
                    view_records_query = f"SELECT id, food_item, calories, time_consumed FROM {current_month} WHERE username = '{username}'"
                    cursor.execute(view_records_query)
                    records = cursor.fetchall()

                    if records:
                        print("Existing Records:")
                        for record in records:
                            print(f"ID: {record[0]}, Food: {record[1]}, Calories: {record[2]}, Time Consumed: {record[3]}")

                        record_id = int(input("Enter the ID of the record you want to delete: "))
                        delete_query = f"DELETE FROM {current_month} WHERE id = %s AND username = '{username}'"
                        cursor.execute(delete_query, (record_id,))
                        conn.commit()
                        print("Record deleted successfully!")

                    else:
                        print("No records found to delete.")



                elif user_choice == 4:
                    print("Logging out...")
                    main()

                elif user_choice == 5:
                    print("Reports Options:")
                    print("1. Date")
                    print("2. Month")
                    print("3. Year")
                    print("4. Cataegory Wise")
                    report_option = int(input("Enter option: "))
                    if report_option == 1:
                        date = input("Enter date (YYYY-MM-DD): ")
                        report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE DATE(time_consumed) = '{date}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f"Food items consumed on {date}:")
                            for record in records:
                                print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                        else:
                            print(f"No records found for {date}")
                        print("-----------------")
                        print("Calorie Functions")
                        print("1. Total Calories")
                        print("2. Max Calories")
                        print("3. Min Calories")
                        print("4. Average Calories")
                        print("5. Count Food items")

                        gh = int(input("Enter function number: "))
                        ls = []
                        for record in records:
                            ls.append(record[1])
                        if gh == 1:
                            print(f"Total calories consumed on date {date} is {sum(ls)}")
                            print("-----------------")
                        elif gh == 2:
                            print(f"Maximum calories consumed on date {date} is {max(ls)}")
                            print("-----------------")
                        elif gh == 3:
                            print(f"Minimum calories consumed on date {date} is {min(ls)}")
                            print("-----------------")
                        elif gh == 4:
                            print(f"Average calories consumed on date {date} is {mean(ls)}")
                            print("-----------------")
                        elif gh == 5:
                            print(f"Total food items consumed on date {date} is {len(ls)}")
                            print("-----------------")
                        else:
                            print("Invalid")


                    elif report_option == 2:
                        month = input("Enter month (MM-YYYY): ")
                        report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE DATE_FORMAT(time_consumed, '%m-%Y') = '{month}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f"Food items consumed in {month}:")
                            for record in records:
                                print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                        else:
                            print(f"No records found for {month}")
                        print("-----------------")
                        print("Calorie Functions")
                        print("1. Total Calories")
                        print("2. Max Calories")
                        print("3. Min Calories")
                        print("4. Average Calories")
                        print("5. Count Food items")

                        gh = int(input("Enter function number: "))
                        ls = []
                        for record in records:
                            ls.append(record[1])
                        if gh == 1:
                            print(f"Total calories consumed in month {month} is {sum(ls)}")
                            print("-----------------")
                        elif gh == 2:
                            print(f"Maximum calories consumed in month {month} is {max(ls)}")
                            print("-----------------")
                        elif gh == 3:
                            print(f"Minimum calories consumed in month {month} is {min(ls)}")
                            print("-----------------")
                        elif gh == 4:
                            print(f"Average calories consumed in month {month} is {mean(ls)}")
                            print("-----------------")
                        elif gh == 5:
                            print(f"Total food items consumed in month {month} is {len(ls)}")
                            print("-----------------")
                        else:
                            print("Invalid")

                    elif report_option == 3:
                        year = input("Enter year (YYYY): ")
                        report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE YEAR(time_consumed) = '{year}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f"Food items consumed in {year}:")
                            for record in records:
                                print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")



                        else:
                            print(f"No records found for {year}")
                        print("-----------------")
                        print("Calorie Functions")
                        print("1. Total Calories")
                        print("2. Max Calories")
                        print("3. Min Calories")
                        print("4. Average Calories")
                        print("5. Count Food items")

                        gh = int(input("Enter function number: "))
                        ls = []
                        for record in records:
                            ls.append(record[1])
                        if gh == 1:
                            print(f"Total calories consumed in year {year} is {sum(ls)}")
                            print("-----------------")
                        elif gh == 2:
                            print(f"Maximum calories consumed in year {year} is {max(ls)}")
                            print("-----------------")
                        elif gh == 3:
                            print(f"Minimum calories consumed in year {year} is {min(ls)}")
                            print("-----------------")
                        elif gh == 4:
                            print(f"Average calories consumed in year {year} is {mean(ls)}")
                            print("-----------------")
                        elif gh == 5:
                            print(f"Total food items consumed in year {year} is {len(ls)}")
                            print("-----------------")
                        else:
                            print("Invalid")
                    elif report_option == 4:
                        print("Cataegory Options:")
                        print("1. See for particular Cataegory")
                        print("2. Get a diet")
                        option = int(input("Enter option: "))

                        if option == 2:
                            print("Choose Cataegory")
                            print("Carbohydrate")
                            print("Protein")
                            print("Vitamin")
                            print("Fat")
                            print("Sodium")
                            ch = input("Enter category: ")

                            print("choose cuisine: ")
                            names = ["American", "Italian", "Chinese", "Mexican", "Indian", "Thai", "Greek", "Mediterranean", "Middle Eastern", "Japanese", "French", "German", "Southern", "British", "Russian", "Belgian", "Dutch", "Swiss", "North African", "Hawaiian", "South American", "Eastern European", "Taiwanese"]
                            for name in names:
                                print(name)
                            cu=input("Enter cuisine: ")

                            print("choose meal type: ")
                            meal_types = ["Breakfast", "Lunch", "Dinner", "Dessert", "Snack", "Appetizer", "Salad", "Cooking", "Baking", "Beverage", "Sandwich", "Dip", "Marinade"]
                            for meal_type in meal_types:
                                print(meal_type)
                            me=input("Enter meal type: ")

                            sql=f"Select name from food where cat='{ch}' and cusine='{cu}' and meal='{me}'"
                            cursor.execute(sql)
                            recommendation=list(cursor.fetchall())
                            recommendation10=[]
                            if len(recommendation)<10:
                                print("recommended food items are:")
                                for i in recommendation:
                                    print(i[0])
                            else:
                                seen=[]
                                for i in range(0,10):
                                    index=random.randint(0,len(recommendation)-1)
                                    while index in seen:
                                        index=random.randint(0,len(recommendation)-1)
                                    recommendation10.append(recommendation[index])
                                    seen.append(index)
                                print("recommended food items are: ")
                                for i in recommendation10:
                                    print(i[0])

                        if option == 1:
                            print("Choose Cataegory")
                            print("1. Carbs")
                            print("2. Protein")
                            print("3. Vitamin")
                            print("4. Fat")

                            ch = int(input("Enter diet: "))
                            if ch == 1:
                                print("Carbs")
                                report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE cat = 'carbohydrate' and username = '{username}'"
                                cursor.execute(report_query)
                                records = cursor.fetchall()
                                if records:
                                    print(f"Food items consumed in 'carbohydrate':")
                                    for record in records:
                                        print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                                else:
                                    print(f"No records found for Carbs")
                            elif ch == 2:
                                print("Protein")
                                report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE cat = 'protein' and username = '{username}'"
                                cursor.execute(report_query)
                                records = cursor.fetchall()
                                if records:
                                    print(f"Food items consumed in 'protein':")
                                    for record in records:
                                        print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                                else:
                                    print(f"No records found for protein")
                            elif ch == 3:
                                print("Vitamin")
                                report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE cat = 'vitamin' and username = '{username}'"
                                cursor.execute(report_query)
                                records = cursor.fetchall()
                                if records:
                                    print(f"Food items consumed in 'vitamin':")
                                    for record in records:
                                        print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                                else:
                                    print(f"No records found for vitamin")
                            elif ch == 4:
                                print("Fat")
                                report_query = f"SELECT food_item, calories, time_consumed FROM {current_month} WHERE cat = 'fat' and username = '{username}'"
                                cursor.execute(report_query)
                                records = cursor.fetchall()
                                if records:
                                    print(f"Food items consumed in 'fat':")
                                    for record in records:
                                        print(f"Food: {record[0]}, Calories: {record[1]}, Time Consumed: {record[2]}")
                                else:
                                    print(f"No records found for fat")
                            else:
                                print("Invalid")

                    else:
                        print("Invalid option.")

                else:
                    print("Invalid choice.")

        else:
            print("Invalid username or password.")

    elif user_option == 2:
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        sign_up_query = f"INSERT INTO user_list (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(sign_up_query, (new_username, new_password))
            conn.commit()
            print("Sign up successful!")
            main()

        except mysql.connector.IntegrityError:
            print("Username already exists. Choose a different username.")
            main()

    elif user_option == 3:
        if admin_sign_in():
            def admin_options():
                print("Admin Options:")
                print("1. Change food items in the food table")
                print("2. Delete food items in the food table")
                print("3. Add records in the food item table")
                print("4. See admin report")
                print("5. Search food item in the food table")
                print("6. Admin Log Out")

            def admin_search():
                print("Search Food Items")
                view_food_items_query = "SELECT f_id, name, calories, cat, meal, cusine FROM food"
                cursor.execute(view_food_items_query)
                food_items = cursor.fetchall()
                food_search = input("Enter food item to search: ")
                food_search = food_search.capitalize()
                flag = False

                for food_item in food_items:
                        if food_item[1] == food_search:
                            print(f"f_ID: {food_item[0]}, Name: {food_item[1]}, Calories: {food_item[2]}, Cataegory: {food_item[3]}, Meal: {food_item[4]}, Cusine: {food_item[5]}")
                            flag = True
                            break
                if flag == False:
                    print("Food item not found")




            def change_food_items():
                print("Change Food Items:")
                view_food_items_query = "SELECT f_id, name, calories, cat, meal, cusine FROM food"
                cursor.execute(view_food_items_query)
                food_items = cursor.fetchall()

                if food_items:
                    print("Existing Food Items:")
                    for food_item in food_items:
                        print(f"f_ID: {food_item[0]}, Name: {food_item[1]}, Calories: {food_item[2]}, Cataegory: {food_item[3]}, Meal: {food_item[4]}, Cusine: {food_item[5]}")

                    food_id = int(input("Enter the ID of the food item you want to update: "))
                    new_food_name = input("Enter new food name : ")
                    new_calories = int(input("Enter new calories : "))
                    new_cataegory = input("Enter new cataegory: ")
                    new_meal = input("Enter new food meal: ")
                    new_cusine = input("Enter new food cuisine: ")

                    update_food_query = "UPDATE food SET name = COALESCE(%s, name), calories = COALESCE(%s, calories), cat = COALESCE(%s, cat), meal = COALESCE(%s, meal), cusine = COALESCE(%s, cusine) WHERE f_id = %s"
                    cursor.execute(update_food_query, (new_food_name, new_calories, new_cataegory, new_meal, new_cusine, food_id))
                    conn.commit()
                    print("Food item updated successfully!")

                else:
                    print("No food items found to update.")

            def delete_food_items():

                print("Delete Food Items:")
                view_food_items_query = "SELECT f_id, name, calories, cat, meal, cusine FROM food"
                cursor.execute(view_food_items_query)
                food_items = cursor.fetchall()

                if food_items:
                    print("Existing Food Items:")
                    for food_item in food_items:
                        print(f"ID: {food_item[0]}, Name: {food_item[1]}, Calories: {food_item[2]}, Cataegory: {food_item[3]}, Meal: {food_item[4]}, Cuisine: {food_item[5]}")

                    food_id = int(input("Enter the ID of the food item you want to delete: "))
                    delete_food_query = "DELETE FROM food WHERE f_id = %s"
                    cursor.execute(delete_food_query, (food_id,))
                    conn.commit()
                    print("Food item deleted successfully!")

                else:
                    print("No food items found to delete.")

            def add_food_items():
                food_name = input("Enter food name: ")
                calories = int(input("Enter calories: "))
                cat = input("Enter cataegorie: ")
                meal = input("Enter meal: ")
                cusine = input("Enter cuisine: ")
                add_food_query = "INSERT INTO food (name, calories, cat, meal, cusine) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(add_food_query, (food_name, calories, cat, meal, cusine))
                conn.commit()
                print("Food item added successfully!")

            def admin_main():
                while True:
                    admin_options()
                    admin_choice = int(input("Enter your choice: "))

                    if admin_choice == 1:
                        change_food_items()
                    elif admin_choice == 2:
                        delete_food_items()
                    elif admin_choice == 3:
                        add_food_items()
                    elif admin_choice == 4:
                        admin_report()
                    elif admin_choice == 5:
                        admin_search()
                    elif admin_choice == 6:
                        print("Admin logging out...")
                        main()
                    else:
                        print("Invalid choice.")
            admin_main()

    else:
        print("Invalid option.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
