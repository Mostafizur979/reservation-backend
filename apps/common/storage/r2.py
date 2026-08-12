import uuid
from urllib.parse import quote

import boto3
from django.conf import settings


def get_r2_client():
    session = boto3.session.Session()

    return session.client(
        "s3",
        region_name="auto",
        endpoint_url="https://6a212d8be3277e3bfad2c5c045d93242.r2.cloudflarestorage.com",
        aws_access_key_id="2e0121fc07f7f908e575030d76306642",
        aws_secret_access_key="88cee7c95464305d3f0c72f4affbb79967b6819024fb949c92a5945efa37bb82",
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
        "ecommerce",
        object_key,
        ExtraArgs={
            "ContentType": file.content_type,
        },
    )

    return f"{"https://pub-6f0a5190b9134becbdbeee087f020a55.r2.dev"}/{quote(object_key)}"


def remove_from_r2(file_url):
    """
    Delete a file from Cloudflare R2 using its public URL.
    """

    if not file_url:
        return

    client = get_r2_client()

    public_url = settings.R2_PUBLIC_URL.rstrip("/")

    if not file_url.startswith(public_url):
        return

    object_key = file_url[len(public_url) + 1:]

    client.delete_object(
        Bucket=settings.R2_BUCKET,
        Key=object_key,
    )