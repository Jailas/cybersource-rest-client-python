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


class TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions(object):
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
        'sec_code': 'str'
    }

    attribute_map = {
        'sec_code': 'SECCode'
    }

    def __init__(self, sec_code=None):
        """
        TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions - a model defined in Swagger
        """

        self._sec_code = None

        if sec_code is not None:
          self.sec_code = sec_code

    @property
    def sec_code(self):
        """
        Gets the sec_code of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions.
        **Important** This field is required if your processor is TeleCheck.  Code that specifies the authorization method for the transaction. Possible values:  - **CCD**: corporate cash disbursement. Charge or credit against a business checking account. You can use one-time or recurring CCD transactions to transfer funds to or from a corporate entity. A standing authorization is required for recurring transactions. - **PPD**: prearranged payment and deposit entry. Charge or credit against a personal checking or savings account. You can originate a PPD entry only when the payment and deposit terms between you and the customer are prearranged. A written authorization from the customer is required for one-time transactions and a written standing authorization is required for recurring transactions. - **TEL**: telephone-initiated entry. One-time charge against a personal checking or savings account. You can originate a TEL entry only when there is a business relationship between you and the customer or when the customer initiates a telephone call to you. For a TEL entry, you must obtain a payment authorization from the customer over the telephone. There is no recurring billing option for TEL. - **WEB**: internet-initiated entry—charge against a personal checking or savings account. You can originate a one-time or recurring WEB entry when the customer initiates the transaction over the Internet. For a WEB entry, you must obtain payment authorization from the customer over the Internet. 

        :return: The sec_code of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions.
        :rtype: str
        """
        return self._sec_code

    @sec_code.setter
    def sec_code(self, sec_code):
        """
        Sets the sec_code of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions.
        **Important** This field is required if your processor is TeleCheck.  Code that specifies the authorization method for the transaction. Possible values:  - **CCD**: corporate cash disbursement. Charge or credit against a business checking account. You can use one-time or recurring CCD transactions to transfer funds to or from a corporate entity. A standing authorization is required for recurring transactions. - **PPD**: prearranged payment and deposit entry. Charge or credit against a personal checking or savings account. You can originate a PPD entry only when the payment and deposit terms between you and the customer are prearranged. A written authorization from the customer is required for one-time transactions and a written standing authorization is required for recurring transactions. - **TEL**: telephone-initiated entry. One-time charge against a personal checking or savings account. You can originate a TEL entry only when there is a business relationship between you and the customer or when the customer initiates a telephone call to you. For a TEL entry, you must obtain a payment authorization from the customer over the telephone. There is no recurring billing option for TEL. - **WEB**: internet-initiated entry—charge against a personal checking or savings account. You can originate a one-time or recurring WEB entry when the customer initiates the transaction over the Internet. For a WEB entry, you must obtain payment authorization from the customer over the Internet. 

        :param sec_code: The sec_code of this TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions.
        :type: str
        """
        allowed_values = ["CCD", "PPD", "TEL", "WEB"]
        if sec_code not in allowed_values:
            raise ValueError(
                "Invalid value for `sec_code` ({0}), must be one of {1}"
                .format(sec_code, allowed_values)
            )

        self._sec_code = sec_code

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
        if not isinstance(other, TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformationBankTransferOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other