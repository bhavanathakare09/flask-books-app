* For developers

* A simple REST API built with Flask, using AWS DynamoDB for data storage.
    * Supports full CRUD operations:
	    Create books
	    Read books
	    Update books
	    Delete books
    * Dependencies :
        Install dependencies using:
            pip install -r requirements.txt
    * Required Python Packages:
        Flask
        boto3
        python-dotenv   
    * Running the App Locally:
        source venv/bin/activate
        python3 app.py
    * Test API using curl:
        Create a book:
            curl -X POST http://127.0.0.1:5000/books \
            -H "Content-Type: application/json" \
            -d '{"title":"XYZ","author":"JKR","year":"2025","genre":"ABC"}'
        Get all books:
            curl http://127.0.0.1:5000/books
        Update a book:
            curl -X PUT http://127.0.0.1:5000/books/<BOOK_ID> \
            -H "Content-Type: application/json" \
            -d '{"genre":"<enter_genre>"}'
        Delete a book:
            curl -X DELETE http://127.0.0.1:5000/books/<BOOK_ID>


* AWS DynamoDB Setup
    1.	Create table: Books
	2.	Partition key: book_id (String)
	3.	Update db.py to use boto3 without local endpoint
	4.	Configure AWS CLI using:
        aws configure
* Project Structure
    flask-books-app/
    │── app.py
    │── db.py
    │── create_table.py
    │── requirements.txt
    │── README.md
    │── venv/


-------------------------------------------------------------------------------------------------------------------------------------------------------
* For reader 

* Flask Books API — AWS DynamoDB CRUD Application

    1. Clone This Repository
        git clone https://github.com/YOUR_USERNAME/flask-books-app.git
        cd flask-books-app
    2. Set Up Virtual Environment
        python3 -m venv venv
        source venv/bin/activate
    3. Install Dependencies
        pip install -r requirements.txt
    4. AWS Setup (Required for DynamoDB)
        This project uses real AWS DynamoDB, not local DynamoDB.
        You MUST configure AWS credentials on your machine.
        Step A — Install AWS CLI 
            brew install awscli
        Step B — Configure AWS Credentials
            aws configure
        When prompted:
	        AWS Access Key ID: paste your key
	        AWS Secret Access Key: paste your secret
	        Default region name: us-east-1
            Default output format: json
        Step C — DynamoDB Table Requirements
            Create a DynamoDB table in AWS Console:
	        Table name: Books
	        Partition key: book_id (String)
	        Billing mode: On-demand
    5. Run the Flask Application
            Start the server: python3 app.py
            Flask will start on: http://127.0.0.1:5000/
    6. Test the API
        Follow steps from line no 19 











