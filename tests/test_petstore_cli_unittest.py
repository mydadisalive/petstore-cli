import unittest
from unittest.mock import patch
from openapi_client.models.pet import Pet
from petstore_cli import list_pets, find_pet, add_pet

class TestPetstoreCLI(unittest.TestCase):

    @patch('petstore_cli.PetApi')
    def test_list_pets(self, MockPetApi):
        # Mock the PetApi instance
        mock_pet_api = MockPetApi.return_value

        # Setup mock response
        mock_pet_api.find_pets_by_status.return_value = [
            Pet(id=1, name="Buddy", status="available", photo_urls=["https://example.com/photo1.jpg"]),
            Pet(id=2, name="Milo", status="available", photo_urls=["https://example.com/photo2.jpg"])
        ]

        # Call the function
        with patch('builtins.print') as mock_print:
            list_pets(status='available', limit=2)

        # Assert print statements
        mock_print.assert_any_call('ID: 1, Name: Buddy, Status: available')
        mock_print.assert_any_call('ID: 2, Name: Milo, Status: available')

    @patch('petstore_cli.PetApi')
    def test_find_pet(self, MockPetApi):
        # Mock the PetApi instance
        mock_pet_api = MockPetApi.return_value

        # Setup mock response
        mock_pet_api.get_pet_by_id.return_value = Pet(id=1, name="Buddy", status="available", photo_urls=["https://example.com/photo1.jpg"])

        # Call the function
        with patch('builtins.print') as mock_print:
            find_pet(pet_id=1)

        # Assert print statement
        mock_print.assert_called_with('ID: 1, Name: Buddy, Status: available')

    @patch('petstore_cli.PetApi')
    def test_add_pet(self, MockPetApi):
        # Mock the PetApi instance
        mock_pet_api = MockPetApi.return_value

        # Setup mock response
        mock_pet_api.add_pet.return_value = Pet(id=3, name="Buddy", status="available", photo_urls=["https://example.com/photo1.jpg"])

        # Call the function
        with patch('builtins.print') as mock_print:
            add_pet(name="Buddy", status="available", photo_urls=["https://example.com/photo1.jpg"])

        # Assert print statement
        mock_print.assert_called_with('Added pet with ID: 3')

if __name__ == '__main__':
    unittest.main()
