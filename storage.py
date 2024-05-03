# file_uploader.py MinIO Python SDK example

from logzero import logger
import os
import sys
from minio import Minio
from minio.error import S3Error
from datetime import datetime

if len(sys.argv) > 1:
    arg = sys.argv[1]
    logger.info("This is a simple helloworld! Hello {}".format(arg))
else:
    arg = None
    logger.info("This is a simple helloworld! You did not pass an arg")


def upload_file_to_minio(minio_client, bucket_name, object_name, file_path):
    try:
        minio_client.fput_object(bucket_name, object_name, file_path)
        print(f"File {file_path} uploaded as {object_name} to bucket {bucket_name}.")
    except S3Error as e:
        print(f"Error uploading file: {e}")


def main():
    minio_url = os.getenv("MINIO_URL")  # Example: "minio-server:9000"
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    bucket_name = os.getenv("MINIO_BUCKET_NAME")
    file_suffix = os.getenv("FILE_SUFFIX", "default")

    # Create a client with the MinIO server playground, its access key
    # and secret key.
    logger.info(minio_url)
    logger.info(access_key)
    logger.info(secret_key)
    logger.info(bucket_name)
    logger.info(file_suffix)

    dt_string = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    logger.info(f"Today's date: {dt_string}")

    minio_client = Minio(
        minio_url, access_key=access_key, secret_key=secret_key, secure=False
    )  # Set to True if using HTTPS
    minio_client.timeout = 30


    file_path = f"/tmp/hello-{dt_string}.txt"
    object_name = os.path.basename(file_path)

    if not os.path.exists("/tmp"):
        os.mkdir("/tmp")

    with open(file_path, "w") as f:
        f.write(f"Hello World, {arg}!\n")

    # Upload to MinIO
    upload_file_to_minio(minio_client, bucket_name, object_name, file_path)


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
