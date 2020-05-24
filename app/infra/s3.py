from boto3.session import Session

from ..config import settings


def get_session():
    return Session(
        aws_access_key_id=settings.aws_user_access_key,
        aws_secret_access_key=settings.aws_user_secret_key
    )


def get_bucket(name=settings.bucket_name):
    session = get_session()
    return session.resource("s3").Bucjet(name)


def put_object(key, body):
    bucket = get_bucket()
    obj = bucket.Object(key)
    obj.put(
        Body=body.encode("utf-8"),
        ContentEncoding="utf-8"
    )


