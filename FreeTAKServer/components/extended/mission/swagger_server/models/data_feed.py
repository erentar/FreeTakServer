# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.filter import Filter  # noqa: F401,E501
from swagger_server import util


class DataFeed(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, filtergroup: List[str]=None, filter: Filter=None, auth: str=None, auth_required: bool=None, name: str=None, protocol: str=None, port: int=None, group: str=None, iface: str=None, archive: bool=None, anongroup: bool=None, archive_only: bool=None, core_version: int=None, core_version2_tls_versions: str=None, uuid: str=None, type: str=None, tag: List[str]=None, sync: bool=None, sync_cache_retention_seconds: int=None):  # noqa: E501
        """DataFeed - a model defined in Swagger

        :param filtergroup: The filtergroup of this DataFeed.  # noqa: E501
        :type filtergroup: List[str]
        :param filter: The filter of this DataFeed.  # noqa: E501
        :type filter: Filter
        :param auth: The auth of this DataFeed.  # noqa: E501
        :type auth: str
        :param auth_required: The auth_required of this DataFeed.  # noqa: E501
        :type auth_required: bool
        :param name: The name of this DataFeed.  # noqa: E501
        :type name: str
        :param protocol: The protocol of this DataFeed.  # noqa: E501
        :type protocol: str
        :param port: The port of this DataFeed.  # noqa: E501
        :type port: int
        :param group: The group of this DataFeed.  # noqa: E501
        :type group: str
        :param iface: The iface of this DataFeed.  # noqa: E501
        :type iface: str
        :param archive: The archive of this DataFeed.  # noqa: E501
        :type archive: bool
        :param anongroup: The anongroup of this DataFeed.  # noqa: E501
        :type anongroup: bool
        :param archive_only: The archive_only of this DataFeed.  # noqa: E501
        :type archive_only: bool
        :param core_version: The core_version of this DataFeed.  # noqa: E501
        :type core_version: int
        :param core_version2_tls_versions: The core_version2_tls_versions of this DataFeed.  # noqa: E501
        :type core_version2_tls_versions: str
        :param uuid: The uuid of this DataFeed.  # noqa: E501
        :type uuid: str
        :param type: The type of this DataFeed.  # noqa: E501
        :type type: str
        :param tag: The tag of this DataFeed.  # noqa: E501
        :type tag: List[str]
        :param sync: The sync of this DataFeed.  # noqa: E501
        :type sync: bool
        :param sync_cache_retention_seconds: The sync_cache_retention_seconds of this DataFeed.  # noqa: E501
        :type sync_cache_retention_seconds: int
        """
        self.swagger_types = {
            'filtergroup': List[str],
            'filter': Filter,
            'auth': str,
            'auth_required': bool,
            'name': str,
            'protocol': str,
            'port': int,
            'group': str,
            'iface': str,
            'archive': bool,
            'anongroup': bool,
            'archive_only': bool,
            'core_version': int,
            'core_version2_tls_versions': str,
            'uuid': str,
            'type': str,
            'tag': List[str],
            'sync': bool,
            'sync_cache_retention_seconds': int
        }

        self.attribute_map = {
            'filtergroup': 'filtergroup',
            'filter': 'filter',
            'auth': 'auth',
            'auth_required': 'authRequired',
            'name': 'name',
            'protocol': 'protocol',
            'port': 'port',
            'group': 'group',
            'iface': 'iface',
            'archive': 'archive',
            'anongroup': 'anongroup',
            'archive_only': 'archiveOnly',
            'core_version': 'coreVersion',
            'core_version2_tls_versions': 'coreVersion2TlsVersions',
            'uuid': 'uuid',
            'type': 'type',
            'tag': 'tag',
            'sync': 'sync',
            'sync_cache_retention_seconds': 'syncCacheRetentionSeconds'
        }
        self._filtergroup = filtergroup
        self._filter = filter
        self._auth = auth
        self._auth_required = auth_required
        self._name = name
        self._protocol = protocol
        self._port = port
        self._group = group
        self._iface = iface
        self._archive = archive
        self._anongroup = anongroup
        self._archive_only = archive_only
        self._core_version = core_version
        self._core_version2_tls_versions = core_version2_tls_versions
        self._uuid = uuid
        self._type = type
        self._tag = tag
        self._sync = sync
        self._sync_cache_retention_seconds = sync_cache_retention_seconds

    @classmethod
    def from_dict(cls, dikt) -> 'DataFeed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataFeed of this DataFeed.  # noqa: E501
        :rtype: DataFeed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filtergroup(self) -> List[str]:
        """Gets the filtergroup of this DataFeed.


        :return: The filtergroup of this DataFeed.
        :rtype: List[str]
        """
        return self._filtergroup

    @filtergroup.setter
    def filtergroup(self, filtergroup: List[str]):
        """Sets the filtergroup of this DataFeed.


        :param filtergroup: The filtergroup of this DataFeed.
        :type filtergroup: List[str]
        """

        self._filtergroup = filtergroup

    @property
    def filter(self) -> Filter:
        """Gets the filter of this DataFeed.


        :return: The filter of this DataFeed.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter: Filter):
        """Sets the filter of this DataFeed.


        :param filter: The filter of this DataFeed.
        :type filter: Filter
        """

        self._filter = filter

    @property
    def auth(self) -> str:
        """Gets the auth of this DataFeed.


        :return: The auth of this DataFeed.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth: str):
        """Sets the auth of this DataFeed.


        :param auth: The auth of this DataFeed.
        :type auth: str
        """
        allowed_values = ["LDAP", "FILE", "ANONYMOUS", "X_509"]  # noqa: E501
        if auth not in allowed_values:
            raise ValueError(
                "Invalid value for `auth` ({0}), must be one of {1}"
                .format(auth, allowed_values)
            )

        self._auth = auth

    @property
    def auth_required(self) -> bool:
        """Gets the auth_required of this DataFeed.


        :return: The auth_required of this DataFeed.
        :rtype: bool
        """
        return self._auth_required

    @auth_required.setter
    def auth_required(self, auth_required: bool):
        """Sets the auth_required of this DataFeed.


        :param auth_required: The auth_required of this DataFeed.
        :type auth_required: bool
        """

        self._auth_required = auth_required

    @property
    def name(self) -> str:
        """Gets the name of this DataFeed.


        :return: The name of this DataFeed.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DataFeed.


        :param name: The name of this DataFeed.
        :type name: str
        """

        self._name = name

    @property
    def protocol(self) -> str:
        """Gets the protocol of this DataFeed.


        :return: The protocol of this DataFeed.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        """Sets the protocol of this DataFeed.


        :param protocol: The protocol of this DataFeed.
        :type protocol: str
        """

        self._protocol = protocol

    @property
    def port(self) -> int:
        """Gets the port of this DataFeed.


        :return: The port of this DataFeed.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this DataFeed.


        :param port: The port of this DataFeed.
        :type port: int
        """

        self._port = port

    @property
    def group(self) -> str:
        """Gets the group of this DataFeed.


        :return: The group of this DataFeed.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this DataFeed.


        :param group: The group of this DataFeed.
        :type group: str
        """

        self._group = group

    @property
    def iface(self) -> str:
        """Gets the iface of this DataFeed.


        :return: The iface of this DataFeed.
        :rtype: str
        """
        return self._iface

    @iface.setter
    def iface(self, iface: str):
        """Sets the iface of this DataFeed.


        :param iface: The iface of this DataFeed.
        :type iface: str
        """

        self._iface = iface

    @property
    def archive(self) -> bool:
        """Gets the archive of this DataFeed.


        :return: The archive of this DataFeed.
        :rtype: bool
        """
        return self._archive

    @archive.setter
    def archive(self, archive: bool):
        """Sets the archive of this DataFeed.


        :param archive: The archive of this DataFeed.
        :type archive: bool
        """

        self._archive = archive

    @property
    def anongroup(self) -> bool:
        """Gets the anongroup of this DataFeed.


        :return: The anongroup of this DataFeed.
        :rtype: bool
        """
        return self._anongroup

    @anongroup.setter
    def anongroup(self, anongroup: bool):
        """Sets the anongroup of this DataFeed.


        :param anongroup: The anongroup of this DataFeed.
        :type anongroup: bool
        """

        self._anongroup = anongroup

    @property
    def archive_only(self) -> bool:
        """Gets the archive_only of this DataFeed.


        :return: The archive_only of this DataFeed.
        :rtype: bool
        """
        return self._archive_only

    @archive_only.setter
    def archive_only(self, archive_only: bool):
        """Sets the archive_only of this DataFeed.


        :param archive_only: The archive_only of this DataFeed.
        :type archive_only: bool
        """

        self._archive_only = archive_only

    @property
    def core_version(self) -> int:
        """Gets the core_version of this DataFeed.


        :return: The core_version of this DataFeed.
        :rtype: int
        """
        return self._core_version

    @core_version.setter
    def core_version(self, core_version: int):
        """Sets the core_version of this DataFeed.


        :param core_version: The core_version of this DataFeed.
        :type core_version: int
        """

        self._core_version = core_version

    @property
    def core_version2_tls_versions(self) -> str:
        """Gets the core_version2_tls_versions of this DataFeed.


        :return: The core_version2_tls_versions of this DataFeed.
        :rtype: str
        """
        return self._core_version2_tls_versions

    @core_version2_tls_versions.setter
    def core_version2_tls_versions(self, core_version2_tls_versions: str):
        """Sets the core_version2_tls_versions of this DataFeed.


        :param core_version2_tls_versions: The core_version2_tls_versions of this DataFeed.
        :type core_version2_tls_versions: str
        """

        self._core_version2_tls_versions = core_version2_tls_versions

    @property
    def uuid(self) -> str:
        """Gets the uuid of this DataFeed.


        :return: The uuid of this DataFeed.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this DataFeed.


        :param uuid: The uuid of this DataFeed.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def type(self) -> str:
        """Gets the type of this DataFeed.


        :return: The type of this DataFeed.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this DataFeed.


        :param type: The type of this DataFeed.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tag(self) -> List[str]:
        """Gets the tag of this DataFeed.


        :return: The tag of this DataFeed.
        :rtype: List[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag: List[str]):
        """Sets the tag of this DataFeed.


        :param tag: The tag of this DataFeed.
        :type tag: List[str]
        """

        self._tag = tag

    @property
    def sync(self) -> bool:
        """Gets the sync of this DataFeed.


        :return: The sync of this DataFeed.
        :rtype: bool
        """
        return self._sync

    @sync.setter
    def sync(self, sync: bool):
        """Sets the sync of this DataFeed.


        :param sync: The sync of this DataFeed.
        :type sync: bool
        """

        self._sync = sync

    @property
    def sync_cache_retention_seconds(self) -> int:
        """Gets the sync_cache_retention_seconds of this DataFeed.


        :return: The sync_cache_retention_seconds of this DataFeed.
        :rtype: int
        """
        return self._sync_cache_retention_seconds

    @sync_cache_retention_seconds.setter
    def sync_cache_retention_seconds(self, sync_cache_retention_seconds: int):
        """Sets the sync_cache_retention_seconds of this DataFeed.


        :param sync_cache_retention_seconds: The sync_cache_retention_seconds of this DataFeed.
        :type sync_cache_retention_seconds: int
        """

        self._sync_cache_retention_seconds = sync_cache_retention_seconds