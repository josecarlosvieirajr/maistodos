import hashlib
from datetime import datetime, timedelta


def hashable(value):
    hash_object = hashlib.sha256()
    hash_object.update(value.encode())
    return hash_object.hexdigest()


def datetime_validator(value: str) -> str:
    input_format = "%m/%Y"
    output_format = "%Y-%m-%d"
    today = datetime.now().date()

    parsed_date = datetime.strptime(value, input_format).date()

    if parsed_date < today:
        raise ValueError("The input date is not earlier than today.")

    last_day_of_month = (parsed_date.replace(day=1) + timedelta(days=32)).replace(
        day=1
    ) - timedelta(days=1)
    return last_day_of_month.strftime(output_format)
