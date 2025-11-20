import boto3
def get_dynamodb_client():
    return boto3.resource(
        "dynamodb",
        region_name="us-east-1",
        # endpoint_url="http://localhost:8000",
        # aws_access_key_id="fakeKey", # Use fake credentials for local DynamoDB
        # aws_secret_access_key="fakeSecret"
    )

def get_books_table():
    dynamodb = get_dynamodb_client()
    return dynamodb.Table("Books")