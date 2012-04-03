from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.conf import settings

from sm.subscribe.forms import SubscribeForm
from mailsnake import MailSnake


class SubscribeView(FormView):
    form_class = SubscribeForm
    template_name = 'sm/subscribe/subscribe.html'

    def form_valid(self, form):


        ms = MailSnake(settings.MAILCHIMP_API_KEY)

        ms.listSubscribe(
            id = settings.MAILCHIMP_LIST_ID,
            email_address = form.cleaned_data['email'],
            merge_vars = {
                'FNAME': form.cleaned_data['first_name'],
                'GROUPINGS': [{'name':'typeofreaders','groups':'bcseoguide'}],
                },
            update_existing = True,
            double_optin = True,
        )
        return HttpResponseRedirect(reverse('subscribe_success'))

class SuccessView(TemplateView):
    template_name = 'sm/subscribe/success.html'