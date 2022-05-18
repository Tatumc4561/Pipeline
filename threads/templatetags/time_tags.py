# import datetime
# from django import template
# from django.conf import settings


# register = template.Library()


# # Custom template tag to convert published date to a format that shows hours from when originally posted


# @register.simple_tag
# def HoursFrom(self):
#     current = str(datetime.datetime.now())
#     post_date = str(self)
#     date_format_str = "%Y-%m-%d %H:%M:%S.%f"
#     start = datetime.datetime.strptime(current, date_format_str)
#     end = datetime.datetime.strptime(post_date, date_format_str)
#     # Get interval between two timstamps as timedelta object
#     diff = start - end
#     # # Get interval between two timstamps in hours
#     # diff_in_hours = diff.total_seconds() / 3600

#     return f"{current}||||| {post_date} {diff}"
