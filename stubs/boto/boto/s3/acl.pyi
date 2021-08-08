from typing import Any, Dict, List, Text

from .connection import S3Connection
from .user import User

CannedACLStrings: List[str]

class Policy:
    parent: Any
    namespace: Any
    acl: ACL
    def __init__(self, parent: Any | None = ...) -> None: ...
    owner: User
    def startElement(self, name: Text, attrs: Dict[str, Any], connection: S3Connection) -> None | User | ACL: ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class ACL:
    policy: Policy
    grants: List[Grant]
    def __init__(self, policy: Policy | None = ...) -> None: ...
    def add_grant(self, grant: Grant) -> None: ...
    def add_email_grant(self, permission: Text, email_address: Text) -> None: ...
    def add_user_grant(self, permission: Text, user_id: Text, display_name: Text | None = ...) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...

class Grant:
    NameSpace: Text
    permission: Text
    id: Text
    display_name: Text
    uri: Text
    email_address: Text
    type: Text
    def __init__(
        self,
        permission: Text | None = ...,
        type: Text | None = ...,
        id: Text | None = ...,
        display_name: Text | None = ...,
        uri: Text | None = ...,
        email_address: Text | None = ...,
    ) -> None: ...
    def startElement(self, name, attrs, connection): ...
    def endElement(self, name: Text, value: Any, connection: S3Connection) -> None: ...
    def to_xml(self) -> str: ...
