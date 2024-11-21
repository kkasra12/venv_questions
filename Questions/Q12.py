from datetime import datetime
import pytz

utc_time = datetime.utcnow()
timezone = pytz.timezone("Europe/Luxembourg")
localized_time = timezone.localize(utc_time)
print(f"UTC time: {utc_time} and Local time: {localized_time}")
print(f"Timezone: {localized_time.tzinfo}")
print(f"Timezone name: {localized_time.tzname()}")
print(f"Timezone abbreviation: {localized_time.tzname()}")
print(f"Timezone offset: {localized_time.utcoffset()}")
print(f"difference between UTC and local time: {localized_time.utcoffset().total_seconds() / 3600} hours")
