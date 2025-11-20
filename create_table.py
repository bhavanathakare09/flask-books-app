from db import get_dynamodb_client

def create_books_table():
    dynamodb = get_dynamodb_client()

    existing_tables = dynamodb.meta.client.list_tables()["TableNames"]
    
    if "Books" in existing_tables:
        print("Books table already exists")
        return

    table = dynamodb.create_table(
        TableName="Books",
        KeySchema=[
            {
                "AttributeName": "book_id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "book_id",
                "AttributeType": "S"
            }
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    print("Creating table...")
    table.wait_until_exists()
    print("Books table created successfully")

if __name__ == "__main__":
    create_books_table()