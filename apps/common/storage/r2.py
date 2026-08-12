import uuid
from urllib.parse import quote

import boto3
from django.conf import settings


def get_r2_client():
    session = boto3.session.Session()

    return session.client(
        "s3",
        region_name="auto",
        endpoint_url=settings.AWS_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )


def upload_to_r2(file, folder="uploads"):

    client = get_r2_client()

    original_name = file.name
    extension = original_name.rsplit(".", 1)[-1] if "." in original_name else ""

    unique_name = str(uuid.uuid4())

    if extension:
        file_name = f"{unique_name}.{extension}"
    else:
        file_name = unique_name

    object_key = f"{folder}/{file_name}"

    file.seek(0)

    client.upload_fileobj(
        file,
        settings.AWS_BUCKET,
        object_key,
        ExtraArgs={
            "ContentType": file.content_type,
        },
    )

    return f"{settings.AWS_PUBLIC_URL}/{quote(object_key)}"


def remove_from_r2(file_url):
    """
    Delete a file from Cloudflare R2 using its public URL.
    """

    if not file_url:
        return

    client = get_r2_client()

    public_url = settings.AWS_PUBLIC_URL.rstrip("/")

    if not file_url.startswith(public_url):
        return

    object_key = file_url[len(public_url) + 1:]

    client.delete_object(
        Bucket=settings.AWS_BUCKET,
        Key=object_key,
    )