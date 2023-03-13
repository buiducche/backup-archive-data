from minio import Minio

client = Minio(
		"172.18.0.2:9000",
		access_key = "minioadmin",
		secret_key = "minioadmin",
		secure = False,
	)
found = client.bucket_exists("che")
if not found:
    client.make_bucket("che")
