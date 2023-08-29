import aiosqlite


class Database:

    def async_with_connection(func):
        async def wrapper(*args, **kwargs):
            connection = await aiosqlite.connect('database.db')
            try:
                result = await func(connection, *args, **kwargs)
                await connection.commit()
                return result
            finally:
                await connection.close()

        return wrapper

    @async_with_connection
    async def get_tables_name(connection):
        cursor = await connection.cursor()
        await cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return await cursor.fetchall()

    @async_with_connection
    async def async_insert_user(connection, name):
        cursor = await connection.cursor()
        await cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

    @async_with_connection
    async def async_select_user(connection):
        cursor = await connection.cursor()
        await cursor.execute("SELECT name FROM users")
        return await cursor.fetchall()

# class Database:
#     def __init__(self, database):
#         self.connection = sqlite3.connect(f'{database}.db', check_same_thread=False)
#         self.cursor = self.connection.cursor()
#
#     def create_table(self, table_name):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + ''' (
#                                                             x TEXT,
#                                                             x1 TEXT,
#                                                             y TEXT,
#                                                             y1 TEXT,
#                                                             price TEXT);'''
#                             )
#         self.connection.commit()
#
#     def insert_data(self, table_name, values):
#         if table_name == 'users':
#             self.cursor.execute('INSERT INTO ' + table_name + ' VALUES (?, ?, ?);', values)
#         else:
#             self.cursor.execute('INSERT INTO ' + table_name + ' VALUES (?, ?, ?, ?, ?);', values)
#         self.connection.commit()
#
#     def get_data(self, table_name):
#         self.cursor.execute('''SELECT * FROM ''' + table_name)
#         self.connection.commit()
#         return self.cursor
#
#     def delete_data(self, table_name):
#         self.cursor.execute('''DELETE FROM ''' + table_name)
#         self.connection.commit()
#
#     def alter_table_name(self, old_name, new_name):
#         self.cursor.execute('''ALTER TABLE ''' + old_name.replace(' ', '_') + ''' RENAME TO ''' + new_name.replace(' ', '_'))
#         self.connection.commit()
#
#     def delete_empty_string(self, table_name):
#         self.cursor.execute("DELETE FROM " + table_name + " WHERE x='' and x1='' and y='' and y1='' and price='';")
#         self.connection.commit()
#
#     def get_price(self, table_name):
#         self.cursor.execute("SELECT price FROM " + table_name + " WHERE price <> '' ")
#         self.connection.commit()
#         return self.cursor
#
#     def set_price(self, table_name, value):
#         insert_query = f"UPDATE {table_name} SET price = ? WHERE rowid = 1"
#         self.cursor.execute(insert_query, (value,))
#         self.connection.commit()
#
#     def close(self):
#         self.connection.close()