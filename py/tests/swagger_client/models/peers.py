# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.peers_peers import PeersPeers  # noqa: F401,E501


class Peers(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'peers': 'list[PeersPeers]',
        'blocked': 'list[str]'
    }

    attribute_map = {
        'peers': 'peers',
        'blocked': 'blocked'
    }

    def __init__(self, peers=None, blocked=None):  # noqa: E501
        """Peers - a model defined in Swagger"""  # noqa: E501

        self._peers = None
        self._blocked = None
        self.discriminator = None

        if peers is not None:
            self.peers = peers
        if blocked is not None:
            self.blocked = blocked

    @property
    def peers(self):
        """Gets the peers of this Peers.  # noqa: E501

        All connected peers  # noqa: E501

        :return: The peers of this Peers.  # noqa: E501
        :rtype: list[PeersPeers]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this Peers.

        All connected peers  # noqa: E501

        :param peers: The peers of this Peers.  # noqa: E501
        :type: list[PeersPeers]
        """

        self._peers = peers

    @property
    def blocked(self):
        """Gets the blocked of this Peers.  # noqa: E501

        All blocked peers  # noqa: E501

        :return: The blocked of this Peers.  # noqa: E501
        :rtype: list[str]
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this Peers.

        All blocked peers  # noqa: E501

        :param blocked: The blocked of this Peers.  # noqa: E501
        :type: list[str]
        """

        self._blocked = blocked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Peers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
