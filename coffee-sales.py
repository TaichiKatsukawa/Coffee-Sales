import pprint
import sqlite3
import pandas as pd
from pprint import pprint


def main():
    conn = sqlite3.connect('coffee_data.db')
    update_dataset("ihelon/coffee-sales", "index_1.csv", conn)

    # Create view for querying
    view_name = 'view_coffee_sales'
    sql_drop_view = f"""
        DROP VIEW IF EXISTS {view_name}
    """
    sql_create_view = f"""
        CREATE VIEW {view_name} AS
        SELECT
            date, 
            datetime, 
            cash_type,
            money, 
            coffee_name
        FROM sales
        ORDER BY datetime
    """
    conn.execute(sql_drop_view)
    conn.execute(sql_create_view)

    print('View created successfully:')
    df = pd.read_sql(f"SELECT * FROM sqlite_master WHERE type='view' AND name = '{view_name}'", conn)
    pprint(df)
    

def upload_to_sql(df: pd.DataFrame, conn):
    df.to_sql('sales', conn, if_exists='replace')


def update_dataset(dataset_dir, file_path, conn):
    # Install dependencies as needed:
    # pip install kagglehub[pandas-datasets]
    import kagglehub
    from kagglehub import KaggleDatasetAdapter

    # Load the latest version
    df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    dataset_dir,
    file_path,
    # Provide any additional arguments like 
    # sql_query or pandas_kwargs. See the 
    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
    )

    upload_to_sql(df, conn)
    
def create_view_for_query(conn):
    sql = """
        CREATE VIEW view_coffee_sales AS
        SELECT date, datetime, cash_type, money, coffee_name
        FROM sales
    """
    pd.read_sql(sql, conn)


if __name__ == '__main__':
    main()