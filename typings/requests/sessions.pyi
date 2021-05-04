import time
from ._internal_utils import to_native_string as to_native_string
from .adapters import HTTPAdapter as HTTPAdapter
from .compat import Mapping as Mapping, cookielib as cookielib, is_py3 as is_py3, urljoin as urljoin, urlparse as urlparse
from .cookies import RequestsCookieJar as RequestsCookieJar, cookiejar_from_dict as cookiejar_from_dict, extract_cookies_to_jar as extract_cookies_to_jar, merge_cookies as merge_cookies
from .exceptions import ChunkedEncodingError as ChunkedEncodingError, ContentDecodingError as ContentDecodingError, InvalidSchema as InvalidSchema, TooManyRedirects as TooManyRedirects
from .hooks import default_hooks as default_hooks, dispatch_hook as dispatch_hook
from .models import DEFAULT_REDIRECT_LIMIT as DEFAULT_REDIRECT_LIMIT, PreparedRequest as PreparedRequest, REDIRECT_STATI as REDIRECT_STATI, Request as Request
from .status_codes import codes as codes
from .structures import CaseInsensitiveDict as CaseInsensitiveDict
from .utils import DEFAULT_PORTS as DEFAULT_PORTS, default_headers as default_headers, get_auth_from_url as get_auth_from_url, get_environ_proxies as get_environ_proxies, get_netrc_auth as get_netrc_auth, requote_uri as requote_uri, rewind_body as rewind_body, should_bypass_proxies as should_bypass_proxies, to_key_val_list as to_key_val_list
from typing import Any, Optional

preferred_clock = time.time

def merge_setting(request_setting: Any, session_setting: Any, dict_class: Any = ...): ...
def merge_hooks(request_hooks: Any, session_hooks: Any, dict_class: Any = ...): ...

class SessionRedirectMixin:
    def get_redirect_target(self, resp: Any): ...
    def should_strip_auth(self, old_url: Any, new_url: Any): ...
    def resolve_redirects(self, resp: Any, req: Any, stream: bool = ..., timeout: Optional[Any] = ..., verify: bool = ..., cert: Optional[Any] = ..., proxies: Optional[Any] = ..., yield_requests: bool = ..., **adapter_kwargs: Any) -> None: ...
    def rebuild_auth(self, prepared_request: Any, response: Any) -> None: ...
    def rebuild_proxies(self, prepared_request: Any, proxies: Any): ...
    def rebuild_method(self, prepared_request: Any, response: Any) -> None: ...

class Session(SessionRedirectMixin):
    __attrs__: Any = ...
    headers: Any = ...
    auth: Any = ...
    proxies: Any = ...
    hooks: Any = ...
    params: Any = ...
    stream: bool = ...
    verify: bool = ...
    cert: Any = ...
    max_redirects: Any = ...
    trust_env: bool = ...
    cookies: Any = ...
    adapters: Any = ...
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any) -> None: ...
    def prepare_request(self, request: Any): ...
    def request(self, method: Any, url: Any, params: Optional[Any] = ..., data: Optional[Any] = ..., headers: Optional[Any] = ..., cookies: Optional[Any] = ..., files: Optional[Any] = ..., auth: Optional[Any] = ..., timeout: Optional[Any] = ..., allow_redirects: bool = ..., proxies: Optional[Any] = ..., hooks: Optional[Any] = ..., stream: Optional[Any] = ..., verify: Optional[Any] = ..., cert: Optional[Any] = ..., json: Optional[Any] = ...): ...
    def get(self, url: Any, **kwargs: Any): ...
    def options(self, url: Any, **kwargs: Any): ...
    def head(self, url: Any, **kwargs: Any): ...
    def post(self, url: Any, data: Optional[Any] = ..., json: Optional[Any] = ..., **kwargs: Any): ...
    def put(self, url: Any, data: Optional[Any] = ..., **kwargs: Any): ...
    def patch(self, url: Any, data: Optional[Any] = ..., **kwargs: Any): ...
    def delete(self, url: Any, **kwargs: Any): ...
    def send(self, request: Any, **kwargs: Any): ...
    def merge_environment_settings(self, url: Any, proxies: Any, stream: Any, verify: Any, cert: Any): ...
    def get_adapter(self, url: Any): ...
    def close(self) -> None: ...
    def mount(self, prefix: Any, adapter: Any) -> None: ...

def session(): ...
