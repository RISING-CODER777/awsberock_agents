import json

def lambda_handler(event, context):
    # Log the incoming event for debugging purposes
    print("Received event: " + json.dumps(event))
    
    # Extract the API path from the event
    api_path = event['apiPath']
    
    # Handle different API paths
    if api_path == "/GetBooksInventory":
        # Return a list of book details
        response_data = [
            {"BookID": "B001", "Title": "The Silent Patient", "AvailableCopies": 3},
            {"BookID": "B002", "Title": "Educated", "AvailableCopies": 2},
            {"BookID": "B003", "Title": "The Great Gatsby", "AvailableCopies": 5},
            {"BookID": "B004", "Title": "To Kill a Mockingbird", "AvailableCopies": 4},
            {"BookID": "B005", "Title": "1984", "AvailableCopies": 6},
            {"BookID": "B006", "Title": "The Catcher in the Rye", "AvailableCopies": 3},
            {"BookID": "B007", "Title": "The Subtle Art of Not Giving a F*ck", "AvailableCopies": 7},
            {"BookID": "B008", "Title": "Sapiens: A Brief History of Humankind", "AvailableCopies": 4},
            {"BookID": "B009", "Title": "The Hobbit", "AvailableCopies": 2},
            {"BookID": "B010", "Title": "Becoming", "AvailableCopies": 5}
        ]
    
    elif api_path == "/RestockBook":
        # Return a success message for book restocking
        response_data = {"status": "Success", "message": "Books have been restocked successfully."}
    
    else:
        # Return an error message for unknown API paths
        response_data = {"message": "Unknown API Path"}
    
    # Prepare the response body
    response_body = {
        'application/json': {
            'body': json.dumps(response_data)
        }
    }
    
    # Construct the action response
    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': 200,
        'responseBody': response_body
    }
    
    # Include session attributes 
    session_attributes = event.get('sessionAttributes', {})
    prompt_session_attributes = event.get('promptSessionAttributes', {})
    
    # Construct the final API response
    api_response = {
        'messageVersion': '1.0',
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    }
    
    # Log the final API response 
    print("Returning API response: " + json.dumps(api_response))
        
    return api_response