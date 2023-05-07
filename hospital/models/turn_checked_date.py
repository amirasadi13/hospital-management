import datetime
from django.db import models

from base.base_model import BaseModel
from constants import constants


class TurnCheckedDate(BaseModel):
    STATUS = (
        (constants.CANCELED, constants.CANCELED),
        (constants.PAID, constants.PAID),
        (constants.SUBMITTED, constants.SUBMITTED)
    )

    patient = models.ForeignKey('users.Patient', on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey('users.Doctor', on_delete=models.CASCADE, null=True, blank=True)
    checked_date = models.DateTimeField(null=True, blank=True)
    checked_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default=SUBMITTED)

    class Meta:
        ordering = ['-created_time']

    @classmethod
    def cancel_not_referred_turns_status(cls):
        # cancel all the turns those are not paid and not referred to doctor and their time are less than now
        cls.objects.filter(checked_date__lte=datetime.datetime.now(), status=cls.SUBMITTED).update(status=cls.CANCELED)
        # TODO send a notification or email or sms to patients, because of the turn is canceled
        # send_email()
        # send_sms()
        # send_notification()
        # ...

    @classmethod
    def remind_one_day_before_turns(cls):
        # remind the paid turns, those are close to visit day, one day before alert
        cls.objects.filter(checked_date__lte=datetime.date.today() - datetime.timedelta(days=1), status=cls.PAID)
        # TODO send a notification or email or sms to patients to remind the turn date
        # send_email()
        # send_sms()
        # send_notification()
        # ...
