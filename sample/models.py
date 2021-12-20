from django.db import models
from django_fsm import transition, FSMField

from sample.utils import can_change

# Create your models here.


class InvoiceTest(models.Model):

    DRAFT = 'Draft'
    AWAITING_SIGN_A = 'Awaiting Sign A'
    AWAITING_SIGN_B = 'Awaiting Sign B'
    AWAITING_SIGN_C = 'Awaiting Sign C'
    AWAITING_APPROVAL = 'Awaiting Approval'

    RESOLVER = {
        DRAFT: 'Draft',
        AWAITING_SIGN_A: 'Awaiting Sign A',
        AWAITING_SIGN_B: 'Awaiting Sign B',
        AWAITING_SIGN_C: 'Awaiting Sign C',
        AWAITING_APPROVAL: 'Awaiting Approval'
    }

    CHOICES = RESOLVER.items()

    name = models.CharField(max_length=100)
    state = FSMField(default=DRAFT,
                     choices=CHOICES,
                     protected=True)

    def __str__(self):
        return self.name

    @transition(
        field=state,
        source=DRAFT,
        target=AWAITING_SIGN_A,
        # custom=({'button_name': 'Approve'}),
        # permission=can_edit
    )
    def from_draft_to_sign_A(self, **kwargs):
        pass

    @transition(
        field=state,
        source=AWAITING_SIGN_A,
        target=AWAITING_SIGN_B,
        # custom=({'button_name': 'Modify'}),
    )
    def from_sign_A_to_sign_B(self, **kwargs):
        pass

    @transition(
        field=state,
        source=AWAITING_SIGN_B,
        target=AWAITING_SIGN_C,
        # custom=({'button_name': 'Re-Approve'}),
    )
    def from_sign_B_to_sign_C(self, **kwargs):
        pass

    @transition(
        field=state,
        source=AWAITING_SIGN_C,
        target=AWAITING_APPROVAL,
        # custom=({'button_name': 'Close'}),
    )
    def from_sign_C_to_approval(self, **kwargs):
        pass

    @transition(
        field=state,
        source=[AWAITING_SIGN_A, AWAITING_SIGN_B, AWAITING_SIGN_C],
        target=DRAFT,
        permission=can_change
    )
    def from_A_B_C_to_draft(self, **kwargs):
        pass
