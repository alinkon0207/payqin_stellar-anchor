from rest_framework.request import Request

def return_toml_contents(request, *args, **kwargs):
    return {
        "DOCUMENTATION": {
            "ORG_NAME": "Anchor Inc.",
            "ORG_URL": "...",
            "ORG_LOGO": "...",
            "ORG_DESCRIPTION": "...",
            "ORG_OFFICIAL_EMAIL": "...",
            "ORG_SUPPORT_EMAIL": "..."
        },
    }