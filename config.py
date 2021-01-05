class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    CLIENT_SECRET = "7O4C~r3hIX.23XMi1H7~B3D_Dha3ddS-rp"

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "4c8b3ff2-ec8e-496c-85b8-53929f1ae2db"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL,
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session