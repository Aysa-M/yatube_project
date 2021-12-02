from django.http import HttpResponse 

# Create your views here.
def index(request):
    """Information which is showing up on the start page."""
    return HttpResponse('FROM PEOPLE TO PEOPLE. '
                        'SHARE YOUR IDEAS, '
                        'THOUGHTS, OPINIONS, ARTS OF WORDS '
                        'AND COMPLAININGS HERE! '
                        'BLOGSPOT IS WAITING FOR!')


def group_posts(request, any_slug):
    """Information for displaying on the page with posts grouped by GROUPS."""
    return HttpResponse(f'HERE YOU CAN CHOSE THE MOST LIKED TOPICS OF YOURS. '
                        f'OPEN ANY {any_slug} AND ENJOY.')
