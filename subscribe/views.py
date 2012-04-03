from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from sm.subscribe.forms import SubscribeForm

from mailsnake import MailSnake

from django.conf.settings import MAILCHIMP_API_KEY


class SubscribeView(FormView):
    form_class = SubscribeForm
    template_name = 'sm/subscribe/subscribe.html'

    def form_valid(self, form):

        ms = MailSnake(MAILCHIMP_API_KEY)
        ms.ListSubscribe()

        return HttpResponseRedirect(reverse('subscribe_success'))

class SuccessView(TemplateView):
    template_name = 'sm/subscribe/success.html'