from google.cloud import storage

def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created.")

if __name__ == "__main__":
    create_bucket("bucket-using-github")

