
from minio import Minio
import urllib3
import datetime
# client = Minio(
#     "192.168.56.105:9000",
#     access_key="admin",
#     secret_key="password@31"
# )
try:
	client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)
	print("Checking at ", datetime.datetime.now())
	client.bucket_exists("bucket_name")
except Exception as e:
	print(f"Error checking bucket. {e}. Error at ", datetime.datetime.now())
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)
