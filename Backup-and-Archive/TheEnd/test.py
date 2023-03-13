# flowFile = session.get()
# if flowFile != None:
#     message =" update!"
#     flowFile = session.putAttribute(flowFile, "message", message)
#     flowFile = session.putAllAttributes(flowFile, {
#         "attribute.one": flowFile.getAttribute('file.size'),
#         "attribute.two": flowFile.getAttribute('file.creationTime')
#     })
#     print(flowFile.getAttribute('filename'))
#     print(flowFile.getAttribute('file.size'))
#     print(flowFile.getAttribute('file.creationTime'))
# session.transfer(flowFile, REL_SUCCESS)

# from minio import Minio
# from minio.commonconfig import ENABLED, Filter
# from minio.lifecycleconfig import Expiration, LifecycleConfig, Rule, Transition
# client = Minio(
# 		"192.168.56.105:9000",
# 		access_key = "admin",
# 		secret_key = "password@31",
# 		secure = False,
# 	)


# config = LifecycleConfig(
#     [
#         Rule(
#             ENABLED,
#             rule_filter=Filter(prefix="users-uploads/"),
#             rule_id="Removing all old versions",
#             expiration=Expiration(days=365),
#         ),

#     ],
# )
# client.set_bucket_lifecycle("bucket1", config)


# from ftplib import FTP

# ftp_ip = "192.168.56.105"
# ftp_usr = "kien"
# ftp_pwd = "tanhong"


# ftp_client = FTP(ftp_ip)
# ftp_client.login(user=ftp_usr, passwd = ftp_pwd)
# ftp_client.cwd("\home\kien\Downloads/")
# print(ftp_client.size("Sample-Spreadsheet-1000-rows.csv"))

from datetime import datetime, timedelta

from minio import Minio
from minio.commonconfig import GOVERNANCE
from minio.retention import Retention

client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)
config = Retention(GOVERNANCE, datetime.utcnow() + timedelta(days=20))
client.set_object_retention("bucket1", "DSC_4679.JPG", config)
# try:
    
#     response = client.get_object("test123", "DSC_4679.JPG")
#     s=response.__dict__['headers']['ETag']
#     print(s[1:(len(s)-1)])
#     print(s[1:(len(s)-1)]==response.__dict__['headers']['x-amz-meta-s3.hashvalue'])
#     # Read data from response.
# finally:
#     response.close()
#     response.release_conn()

# from asyncio.windows_events import NULL
# import os
# import sys
# from hashlib import md5
# from argparse import ArgumentParser

# parser = ArgumentParser(description='Compare an S3 etag to a local file')
# parser.add_argument('inputfile', help='The local file')
# parser.add_argument('etag', help='The etag from s3')
# args = parser.parse_args()

# def factor_of_1MB(filesize, num_parts):
#     x = filesize / int(num_parts)
#     y = x % 1048576
#     return int(x + 1048576 - y)

# def calc_etag(inputfile, partsize):
#     md5_digests = []
#     with open(inputfile, 'rb') as f:
#         for chunk in iter(lambda: f.read(partsize), b''):
#             md5_digests.append(md5(chunk).digest())
#     return md5(b''.join(md5_digests)).hexdigest() + '-' + str(len(md5_digests))

# def possible_partsizes(filesize, num_parts):
#     return lambda partsize: partsize < filesize and (float(filesize) / float(partsize)) <= num_parts

# def main():
#     filesize  = os.path.getsize(args.inputfile)
#     num_parts = int(args.etag.split('-')[1])

#     partsizes = [ ## Default Partsizes Map
#         8388608, # aws_cli/boto3
#         15728640, # s3cmd
#         factor_of_1MB(filesize, num_parts) # Used by many clients to upload large files
#     ]

#     for partsize in filter(possible_partsizes(filesize, num_parts), partsizes):
#         if args.etag == calc_etag(args.inputfile, partsize):
#             print('Local file matches')
#             sys.exit(0)

#     print('Couldn\'t validate etag')
#     sys.exit(1)

# if __name__ == "__main__":
#     main()



