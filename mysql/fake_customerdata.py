import pymysql.cursors
import random
import names

# Connect to the customer database
cnxCustomers = pymysql.connect(user='root', password='MongoDB2022!test2023', host='<hostname to mysql>')
cursorCustomers = cnxCustomers.cursor()


#connect to the accounts database
cnxAccounts = pymysql.connect(user='root', password='MongoDB2022!test2023', host='<hostname to mysql>')
cursorAccounts = cnxAccounts.cursor()


# Generate and insert fake customer data
for i in range(100):
    if i > 0:
        print("Creating customer {} of 100".format(i))
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        query = "INSERT INTO customers (customer_firstname, customer_lastname) VALUES (%s, %s)"
        cursorCustomers.execute(query, (first_name, last_name))
        customer_id = cursorCustomers.lastrowid
        
        #Generate and insert fake account data for this customer
        num_accounts = random.randint(1, 3)
        for j in range(num_accounts):
            account_type = random.choice(['checking', 'savings', 'credit'])
            balance = random.randint(0, 10000)
            query = "INSERT INTO accounts (customer_id, account_type, balance) VALUES (%s, %s, %s)"
            cursorAccounts.execute(query, (customer_id, account_type, balance))

        # Commit the changes to the database
        cnxCustomers.commit()
        cnxAccounts.commit()

# Close the cursor and connection
cursorCustomers.close()
cnxCustomers.close()
cursorAccounts.close()
cnxAccounts.close()
