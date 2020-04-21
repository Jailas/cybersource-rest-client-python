# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Riskv1authenticationresultsPaymentInformation(object):
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
        'card': 'Riskv1authenticationresultsPaymentInformationCard',
        'tokenized_card': 'Riskv1authenticationresultsPaymentInformationTokenizedCard',
        'fluid_data': 'Riskv1authenticationsPaymentInformationFluidData'
    }

    attribute_map = {
        'card': 'card',
        'tokenized_card': 'tokenizedCard',
        'fluid_data': 'fluidData'
    }

    def __init__(self, card=None, tokenized_card=None, fluid_data=None):
        """
        Riskv1authenticationresultsPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._tokenized_card = None
        self._fluid_data = None

        if card is not None:
          self.card = card
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if fluid_data is not None:
          self.fluid_data = fluid_data

    @property
    def card(self):
        """
        Gets the card of this Riskv1authenticationresultsPaymentInformation.

        :return: The card of this Riskv1authenticationresultsPaymentInformation.
        :rtype: Riskv1authenticationresultsPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Riskv1authenticationresultsPaymentInformation.

        :param card: The card of this Riskv1authenticationresultsPaymentInformation.
        :type: Riskv1authenticationresultsPaymentInformationCard
        """

        self._card = card

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this Riskv1authenticationresultsPaymentInformation.

        :return: The tokenized_card of this Riskv1authenticationresultsPaymentInformation.
        :rtype: Riskv1authenticationresultsPaymentInformationTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this Riskv1authenticationresultsPaymentInformation.

        :param tokenized_card: The tokenized_card of this Riskv1authenticationresultsPaymentInformation.
        :type: Riskv1authenticationresultsPaymentInformationTokenizedCard
        """

        self._tokenized_card = tokenized_card

    @property
    def fluid_data(self):
        """
        Gets the fluid_data of this Riskv1authenticationresultsPaymentInformation.

        :return: The fluid_data of this Riskv1authenticationresultsPaymentInformation.
        :rtype: Riskv1authenticationsPaymentInformationFluidData
        """
        return self._fluid_data

    @fluid_data.setter
    def fluid_data(self, fluid_data):
        """
        Sets the fluid_data of this Riskv1authenticationresultsPaymentInformation.

        :param fluid_data: The fluid_data of this Riskv1authenticationresultsPaymentInformation.
        :type: Riskv1authenticationsPaymentInformationFluidData
        """

        self._fluid_data = fluid_data

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
        if not isinstance(other, Riskv1authenticationresultsPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
