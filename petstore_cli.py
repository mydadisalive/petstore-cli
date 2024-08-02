import argparse
import logging
from openapi_client import ApiClient, Configuration
from openapi_client.api.pet_api import PetApi
from openapi_client.models.pet import Pet
from openapi_client.models.category import Category

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_pets(status, limit=None):
    """
    List pets by status.

    :param status: The status of pets to list (e.g., 'available', 'pending', 'sold').
    :param limit: Optional limit on the number of pets to return.
    """
    config = Configuration()
    config.api_key['api_key'] = 'special-key'  # Set the API key
    with ApiClient(config) as api_client:
        api_instance = PetApi(api_client)
        try:
            logging.info(f"Fetching pets with status '{status}'...")
            pets = api_instance.find_pets_by_status(status=[status])
            for i, pet in enumerate(pets):
                if limit and i >= limit:
                    break
                print(f"ID: {pet.id}, Name: {pet.name}, Status: {pet.status}")
        except Exception as e:
            logging.error(f"Error retrieving pets: {e}")

def find_pet(pet_id):
    """
    Find a pet by its ID.

    :param pet_id: The ID of the pet to find.
    """
    config = Configuration()
    config.api_key['api_key'] = 'special-key'  # Set the API key
    with ApiClient(config) as api_client:
        api_instance = PetApi(api_client)
        try:
            logging.info(f"Fetching pet with ID '{pet_id}'...")
            pet = api_instance.get_pet_by_id(pet_id)
            print(f"ID: {pet.id}, Name: {pet.name}, Status: {pet.status}")
        except Exception as e:
            logging.error(f"Pet not found: {e}")

def add_pet(name, status, photo_urls=None):
    """
    Add a new pet.

    :param name: The name of the pet.
    :param status: The status of the pet (e.g., 'available', 'pending', 'sold').
    :param photo_urls: Optional list of photo URLs for the pet.
    """
    if photo_urls is None:
        photo_urls = ["https://example.com/photo.jpg"]  # Default photo URL
    config = Configuration()
    config.api_key['api_key'] = 'special-key'  # Set the API key
    config.debug = True  # Enable debugging to see the request details
    with ApiClient(config) as api_client:
        api_instance = PetApi(api_client)
        new_pet = Pet(name=name, status=status, photo_urls=photo_urls, category=Category(id=1, name="Default"))
        try:
            logging.info(f"Adding a new pet: {new_pet}")
            created_pet = api_instance.add_pet(new_pet)
            if created_pet:
                print(f"Added pet with ID: {created_pet.id}")
            else:
                logging.warning("The pet was added, but the response is empty.")
            logging.debug(f"API Response Object: {created_pet}")
        except Exception as e:
            logging.error(f"Failed to add pet: {e}")
            # Print debug information
            logging.debug(f"Pet object: {new_pet}")
            # Additional details if available
            if hasattr(e, 'status'):
                logging.debug(f"HTTP Status: {e.status}")
            if hasattr(e, 'body'):
                logging.debug(f"Response body: {e.body}")

def main():
    """
    Main function to parse command-line arguments and execute commands.
    """
    parser = argparse.ArgumentParser(description="CLI for Petstore API")
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Command to list pets
    list_parser = subparsers.add_parser('list', help='List pets')
    list_parser.add_argument('--status', choices=['available', 'pending', 'sold'], help='Filter by pet status')
    list_parser.add_argument('--limit', type=int, help='Limit the number of results')

    # Command to find pet by ID
    find_parser = subparsers.add_parser('find', help='Find pet by ID')
    find_parser.add_argument('pet_id', type=int, help='ID of the pet to find')

    # Command to add a new pet
    add_parser = subparsers.add_parser('add', help='Add a new pet')
    add_parser.add_argument('name', type=str, help='Name of the pet')
    add_parser.add_argument('--status', choices=['available', 'pending', 'sold'], default='available', help='Status of the pet')
    add_parser.add_argument('--photo-urls', nargs='+', help='List of photo URLs for the pet')

    args = parser.parse_args()

    if args.command == 'list':
        list_pets(args.status, args.limit)
    elif args.command == 'find':
        find_pet(args.pet_id)
    elif args.command == 'add':
        add_pet(args.name, args.status, args.photo_urls)

if __name__ == '__main__':
    main()
