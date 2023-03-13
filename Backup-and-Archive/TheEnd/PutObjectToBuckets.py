from minio import Minio
from minio.error import S3Error
import sys
import json

#read content from Nifi
a = sys.stdin.readline()
HT=json.loads(a)

# Create a client with the MinIO server playground, its access key
# and secret key.
client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)

# tail of name file
Nameoffile = HT["filename"]
NameoffileEnd=Nameoffile.split('.')
tail=NameoffileEnd[len(NameoffileEnd)-1]
def CheckTail(duoi):
    abc="BucketTest1"
    if duoi =='JPG':
        found = client.bucket_exists(abc)
        if not found:
            client.make_bucket(abc)
    else:
        abc="BucketTest2"
        found = client.bucket_exists(abc)
        if not found:
            client.make_bucket(abc)
    return abc  

def main():


    metadata = {'HashValue': HT["hash.value"]}
    # Upload object name

    client.fput_object(
        CheckTail(tail), HT["filename"],HT["absolute.path"]+HT["filename"],metadata=metadata,
    )
    sys.stdout.write(" successfully uploaded file "+ HT["filename"])



if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)