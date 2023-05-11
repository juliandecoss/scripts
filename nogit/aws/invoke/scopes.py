DEFAULT_ROLES_TO_ASSUME = ["openid", "profile"]
SSO_PLATFORM_CORE_RESOURCE_IDENTIFIER = "https://platform.konfio.mx/core/"
COGNITO_IDENTIFIER = "https://platform.konfio.mx/core/"
scope = f"https://platform.konfio.mx/core/"
scopes = 'admin'
""" 
scopes = "admin read write "
scopes = scopes.rstrip()
roles_to_assume = scopes.split(" ")
custom_scopes = ""
all_scopes = DEFAULT_ROLES_TO_ASSUME
for role in roles_to_assume:
    custom_scopes = COGNITO_IDENTIFIER + "profile." + role + " "
    all_scopes += custom_scopes + " " """
requesting_scopes = DEFAULT_ROLES_TO_ASSUME.copy()
granted_scopes = scopes.strip().split(" ")
for scope in granted_scopes:
    requesting_scopes.append(SSO_PLATFORM_CORE_RESOURCE_IDENTIFIER + scope)
print(requesting_scopes)
prue = " ".join(requesting_scopes)
print(prue)