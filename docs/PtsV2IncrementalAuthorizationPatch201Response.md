# PtsV2IncrementalAuthorizationPatch201Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PtsV2IncrementalAuthorizationPatch201ResponseLinks**](PtsV2IncrementalAuthorizationPatch201ResponseLinks.md) |  | [optional] 
**id** | **str** | An unique identification number assigned by CyberSource to identify the submitted request. It is also appended to the endpoint of the resource.  On incremental authorizations, this value with be the same as the identification number returned in the original authorization response.  | [optional] 
**submit_time_utc** | **str** | Time of request in UTC. Format: &#x60;YYYY-MM-DDThh:mm:ssZ&#x60; Example &#x60;2016-08-11T22:47:57Z&#x60; equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The &#x60;T&#x60; separates the date and the time. The &#x60;Z&#x60; indicates UTC.  Returned by authorization service.  | [optional] 
**status** | **str** | The status of the submitted transaction.  Possible values:  - AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - DECLINED  | [optional] 
**reconciliation_id** | **str** | Reference number for the transaction. This value is not returned for all processors.  Returned by authorization service.  #### Atos Positive string (6)  #### All other processors String (60)  | [optional] 
**error_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseErrorInformation**](PtsV2IncrementalAuthorizationPatch201ResponseErrorInformation.md) |  | [optional] 
**client_reference_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation**](PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation.md) |  | [optional] 
**processor_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseProcessorInformation**](PtsV2IncrementalAuthorizationPatch201ResponseProcessorInformation.md) |  | [optional] 
**payment_information** | [**PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation**](PtsV2IncrementalAuthorizationPatch201ResponsePaymentInformation.md) |  | [optional] 
**order_information** | [**PtsV2IncrementalAuthorizationPatch201ResponseOrderInformation**](PtsV2IncrementalAuthorizationPatch201ResponseOrderInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


