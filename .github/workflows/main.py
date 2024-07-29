from google.cloud import storage
from google.api_core.exceptions import Conflict

def create_bucket(bucket_name, location='US'):
    """Creates a new Google Cloud Storage bucket."""

    # Initialize a storage client
    storage_client = storage.Client()

    # Create a new bucket
    bucket = storage_client.bucket(bucket_name)
    try:
        bucket.location = location
        bucket.create()
        print(f'Bucket {bucket_name} created successfully.')
    except Conflict:
        print(f'Bucket {bucket_name} already exists.')

if __name__ == "__main__":
    # Replace with your bucket name and location
    bucket_name = 'your-unique-bucket-name'
    location = 'US'  # Or any other region like 'EU', 'asia-east1', etc.

    create_bucket(bucket_name, location)

