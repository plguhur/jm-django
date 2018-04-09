from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from sesame import utils

from vote.models import *
from election.forms import *
from jmapp.settings import DEFAULT_FROM_EMAIL



def find_election(id_election):
    """
    find election given its id or create a new one
    """

    # FIXME check whether the user is allowed or not to manage the election
    election = get_object_or_404(Election, pk=id_election)
    return election


def send_invite(voter):
    """
    Send a mail to the voter for an election
    """

    email = voter.user.email
    login_token = utils.get_parameters(voter.user)
    login_link = "http://127.0.0.1:8000/vote/{}/?url_auth_token={}".format(voter.election.id, login_token['url_auth_token'] )

    html_message = """
    <p>Hello {},</p>
    <p>Vous avez été invité(e) à participer au vote <a href="{}">{}</a> </p>
    <p>Merci,</p>
    <p>Mieux Voter</p>
    """.format(voter.user.last_name, login_link, voter.election.name)


    send_mail(
        'Mieux Voter',
        html_message,
        DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
        html_message = html_message
    )