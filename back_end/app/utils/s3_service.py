import boto3
import os


class S3Service:

    client = boto3.client(

        "s3",

        aws_access_key_id=os.getenv(

            "AWS_ACCESS_KEY_ID"

        ),

        aws_secret_access_key=os.getenv(

            "AWS_SECRET_ACCESS_KEY"

        ),

        region_name=os.getenv(

            "AWS_REGION"

        )

    )

    @staticmethod
    def upload(file, key):
        S3Service.client.upload_fileobj(

            file,

            os.getenv("AWS_BUCKET_NAME"),

            key

        )

        @staticmethod
        def generate_url(key):
            return S3Service.client.generate_presigned_url(

                "get_object",

                Params={

                    "Bucket": os.getenv(

                        "AWS_BUCKET_NAME"

                    ),

                    "Key": key

                },

                ExpiresIn=300

            )

        @staticmethod
        def generate_download_url(key):
            return S3Service.client.generate_presigned_url(

                ClientMethod="get_object",

                Params={

                    "Bucket": os.getenv("AWS_BUCKET_NAME"),

                    "Key": key

                },

                ExpiresIn=300

            )

        @staticmethod
        def delete(key):
            S3Service.client.delete_object(

                Bucket=os.getenv("AWS_BUCKET_NAME"),

                Key=key

            )