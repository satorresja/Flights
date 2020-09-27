import sqlite3


def get_column_names(table_name, cursor):
    cursor.execute(f"pragma table_info({table_name})")
    return [row[1] for row in cursor.fetchall()]


def main():
    connector = sqlite3.connect("./vuelosDisponibles10.db")
    cursor = connector.cursor()

    table_name = "flight"
    column_names = get_column_names(table_name, cursor)

    data = []
    cursor.execute(f"SELECT * FROM {table_name}")
    for row in cursor.fetchall():
        data.append(dict(zip(column_names, row)))

    #print(data)


if __name__ == "__main__":
    main()