# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage.
# Copyright (C) 2016 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from minio import Minio

client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)

# Example anonymous read-only bucket policy.
# policy = {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Principal": {"AWS": "*"},
#             "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
#             "Resource": "arn:aws:s3:::my-bucket",
#         },
#         {
#             "Effect": "Allow",
#             "Principal": {"AWS": "*"},
#             "Action": "s3:GetObject",
#             "Resource": "arn:aws:s3:::my-bucket/*",
#         },
#     ],
# }
# client.set_bucket_policy("my-bucket", json.dumps(policy))

# Example anonymous read-write bucket policy.
s="bucket1"
# policy = {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Principal": {"AWS": "*"},
#             "Action": [
#                 "s3:GetBucketLocation",
#                 "s3:ListBucket",
#                 "s3:ListBucketMultipartUploads",
#             ],
#             "Resource": "arn:aws:s3:::"+s,
#         },
#         {
#             "Effect": "Allow",
#             "Principal": {"AWS": "*"},
#             "Action": [
#                 "s3:GetObject",
#                 "s3:PutObject",
#                 "s3:DeleteObject",
#                 "s3:ListMultipartUploadParts",
#                 "s3:AbortMultipartUpload",
#             ],
#             "Resource": "arn:aws:s3:::"+ s +"/*",
#         },
#     ],
# }
s="bucket08"
policy ={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteBucket"
            ],
            "Resource": [
                "arn:aws:s3:::"+ s+"/*",
                "arn:aws:s3:::"+s
            ]
        },
        {
            "Sid": "AllowObjectLockConfiguration",
            "Effect": "Allow",
            "Action": "s3:GetBucketObjectLockConfiguration",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
client.set_bucket_policy("bucket08", json.dumps(policy))
