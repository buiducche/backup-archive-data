from minio import Minio
from minio.sse import SseCustomerKey
import urllib3
import datetime
import sys
import hashlib
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
# Download data of an object.
client.fget_object("test123", "DSC_4680.JPG", r"C:\Users\Admin\Downloads\DSC_4680.JPG")
print("Download Success")

#read metadata
s=client.stat_object("test123","DSC_4680.JPG")
HashMetadataObject=dict(s.metadata.items())["ETag"]
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

#check hash
md5 = hashlib.md5()
sFile=r'C:\Users\Admin\Downloads\Kien\DSC_4680.JPG'
with open(sFile, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
HashCodeDL=md5.hexdigest()
if HashCodeDL == HashMetadataObject[1:(len(HashMetadataObject)-1)]:
	print("Backup success")
else:
	print("Backup error")

