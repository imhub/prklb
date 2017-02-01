from .settings import PORTAL_URL

def musicbandsite_proc(request):
    return {'PORTAL_URL': PORTAL_URL}
