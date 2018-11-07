# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse20012ClientReferenceInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'code': 'str',
        'application_version': 'str',
        'application_name': 'str',
        'application_user': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'code': 'code',
        'application_version': 'applicationVersion',
        'application_name': 'applicationName',
        'application_user': 'applicationUser',
        'comments': 'comments'
    }

    def __init__(self, code=None, application_version=None, application_name=None, application_user=None, comments=None):
        """
        InlineResponse20012ClientReferenceInformation - a model defined in Swagger
        """

        self._code = None
        self._application_version = None
        self._application_name = None
        self._application_user = None
        self._comments = None

        if code is not None:
          self.code = code
        if application_version is not None:
          self.application_version = application_version
        if application_name is not None:
          self.application_name = application_name
        if application_user is not None:
          self.application_user = application_user
        if comments is not None:
          self.comments = comments

    @property
    def code(self):
        """
        Gets the code of this InlineResponse20012ClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value for each transaction so that you can perform meaningful searches for the transaction. 

        :return: The code of this InlineResponse20012ClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this InlineResponse20012ClientReferenceInformation.
        Client-generated order reference or tracking number. CyberSource recommends that you send a unique value for each transaction so that you can perform meaningful searches for the transaction. 

        :param code: The code of this InlineResponse20012ClientReferenceInformation.
        :type: str
        """
        if code is not None and len(code) > 50:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")

        self._code = code

    @property
    def application_version(self):
        """
        Gets the application_version of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :return: The application_version of this InlineResponse20012ClientReferenceInformation.
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :param application_version: The application_version of this InlineResponse20012ClientReferenceInformation.
        :type: str
        """

        self._application_version = application_version

    @property
    def application_name(self):
        """
        Gets the application_name of this InlineResponse20012ClientReferenceInformation.
        The application name of client which is used to submit the request.

        :return: The application_name of this InlineResponse20012ClientReferenceInformation.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this InlineResponse20012ClientReferenceInformation.
        The application name of client which is used to submit the request.

        :param application_name: The application_name of this InlineResponse20012ClientReferenceInformation.
        :type: str
        """

        self._application_name = application_name

    @property
    def application_user(self):
        """
        Gets the application_user of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :return: The application_user of this InlineResponse20012ClientReferenceInformation.
        :rtype: str
        """
        return self._application_user

    @application_user.setter
    def application_user(self, application_user):
        """
        Sets the application_user of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :param application_user: The application_user of this InlineResponse20012ClientReferenceInformation.
        :type: str
        """

        self._application_user = application_user

    @property
    def comments(self):
        """
        Gets the comments of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :return: The comments of this InlineResponse20012ClientReferenceInformation.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this InlineResponse20012ClientReferenceInformation.
        The description for this field is not available.

        :param comments: The comments of this InlineResponse20012ClientReferenceInformation.
        :type: str
        """

        self._comments = comments

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse20012ClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other