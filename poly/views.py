# coding=utf-8
from django.views.generic import TemplateView


# @login_required(login_url='/login/')
class IndexView(TemplateView):

    """ Docs IndexView"""
    template_name = 'Index.html'


class NextStepView(TemplateView):

    """ Docs NextStepView"""
    next_step_locals = locals()
    template_name = "NextStep.html"

    def get_context_data(self, **kwargs):
        kwargs.setdefault("helper", "help message")
        return super(NextStepView, self).get_context_data(**kwargs)

    def render_to_response(self, context, **response_kwargs):
        return super(NextStepView, self).render_to_response(context=context, **response_kwargs)
