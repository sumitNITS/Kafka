import random 
import string 

sender_ids = list(range(1, 11))
receiver_ids = list(range(1, 11))

def generate_message() -> dict:
    random_sender_id = random.choice(sender_ids)

    # Copy the recipients array
    receiver_ids_copy = receiver_ids.copy()

    # User can't send message to himself
    receiver_ids_copy.remove(random_sender_id)
    random_receiver_id = random.choice(receiver_ids_copy)

    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(9))

    return {
        'user_id': random_sender_id,
        'recipient_id': random_receiver_id,
        'message': message
    }