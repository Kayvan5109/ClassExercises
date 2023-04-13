from google.cloud import storage 

def read_bucket_contents(request): 
    #request_json = request.get_json()
    storage_client = storage.Client()
    #use the bucket name you created in cloud storage 
    blobs = storage_client.list_blobs('kayvan')
    print('List of files in bucket:', 'kayvan')
    for blob in blobs: 
            print('File:', blob.name)
    return ''