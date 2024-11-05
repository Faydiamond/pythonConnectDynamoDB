import boto3
def lambda_handler(event:any,contect:any):
    user = event["user"]
    visit_count : int = 0
    session = boto3.Session(region_name='us-east-1')
    dynamoDB = session.resource('dynamodb')
    table_name = "countTable"
    table = dynamoDB.Table(table_name)
    response = table.get_item(Key={"user":user})
    print("responde " ,response)
    if "Item" in response:
        visit_count = response["Item"]["count"] +1
        print("Que " , visit_count)
    table.put_item(Item={"user":user, "count":visit_count })
    message = f"hello {user}, how are you?, yo have visited this web {visit_count} times."
    return { "message" : message }

if __name__ == "__main__":
    event = {"user":"Feibian"}
    print(lambda_handler(event,None))