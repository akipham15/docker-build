# file_uploader.py MinIO Python SDK example

from logzero import logger
import os
import sys
from minio import Minio
from minio.error import S3Error

if len(sys.argv) > 1:
    arg = sys.argv[1]
    logger.info("This is a simple helloworld! Hello {}".format(arg))
else:
    arg = None
    logger.info("This is a simple helloworld! You did not pass an arg")


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "118.70.7.162:9000",
        access_key="er9h7SLYYRwWaJzqaYQJ",
        secret_key="m6mKWYkF6k07mxjGtpmeSRFgttHV3cyO6yRzI2NP",
    )

    if not os.path.exists("/tmp"):
        os.mkdir("/tmp")

    source_file = "/tmp/test-file.txt"

    with open(source_file, "w") as f:
        f.write(f"Hello World, {arg}!\n")

    # The destination bucket and filename on the MinIO server
    bucket_name = "locals3"
    destination_file = "my-test-file.txt"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name,
        destination_file,
        source_file,
    )
    print(
        source_file,
        "successfully uploaded as object",
        destination_file,
        "to bucket",
        bucket_name,
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
