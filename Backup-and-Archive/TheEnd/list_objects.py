from operator import length_hint
from minio import Minio
import datetime
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
objects = client.list_objects("bucket1")
for obj in objects:
	s=client.stat_object("bucket1",obj.object_name)
	# print(dict(s.metadata.items()))
s1=client.stat_object("test123","DSC_4679.JPG")
print(dict(s1.metadata.items()))
s222=len(dict(s1.metadata.items())['ETag'])
s333=len(dict(s1.metadata.items())['x-amz-meta-s3.hashvalue'])
print(s222)
print(s333)
