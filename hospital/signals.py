from django.db.models.signals import post_save
from django.dispatch import receiver

from hospital.models.turn_checked_date import TurnCheckedDate


@receiver(post_save, sender=TurnCheckedDate)
def new_turn_create(sender, instance, created, **kwargs):
    # TODO send a notification or email or sms to patient and dotor that a new turn is booked for you
    # send_email()
    # send_sms()
    # send_notification()
    # ...
    pass
