from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    content = models.TextField()
    author_email =models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0,blank=True)
    ratins = models.IntegerField(default=0,blank=True)
    is_approved =models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return self.subject


class UserMessage(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = models.TextField()
    email =models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title




# def special_data_table( number_of_slots, values, find_item ) :
#     ####### DO NOT MODIFY BELOW #######
#     myTable = MySpecialTable(number_of_slots)
#     for val in values:
#         myTable.add_item(val)

#     return myTable.find_item(find_item)
#     ####### DO NOT MODIFY ABOVE #######

# # class MySpecialTable():
# #         def __init__(self, slots):
# #             self.slots = slots
# #             self.table = []
# #             self.create_table()

# #         def hash_key(self, value):
# #             return value%self.slots

# #         def create_table(self):
#             for i in slots:
#                 self.table.append([])

#         def add_item(self, value):
#             self.slots.insert(hash_key(value))

#         def find_item(self, item):
#             pass
