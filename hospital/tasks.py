from celery import shared_task

from hospital.models.turn_checked_date import TurnCheckedDate


@shared_task
def cancel_turns_status():
    """

        cancel all the turns those are not paid and not referred to doctor

    """
    TurnCheckedDate.cancel_not_referred_turns_status()


@shared_task
def remind_one_day_before_turns():
    """

        remind the paid turns, those are close to visit day (one day before alert)

    """
    TurnCheckedDate.remind_one_day_before_turns()
