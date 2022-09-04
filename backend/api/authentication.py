from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'


class TokenScheme(OpenApiAuthenticationExtension):
    target_class = 'TokenAuthentication'
    name = 'tokenAuth'
    match_subclasses = True
    priority = 1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name='Authorization',
            token_prefix=self.target.keyword,
        )
