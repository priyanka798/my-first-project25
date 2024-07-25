from google.cloud import storage

def create_bucket(priyanka_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(priyanka_name)
    print(f"Bucket {bucket.name} created.")

if _name_ == "_main_":
    create_bucket("bucket-using-github")
