# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6282, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[
        Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]
    ]


class SessionOperations(object):
    """SessionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~microsoft_bonsai_api.simulator.generated.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        workspace_name,  # type: str
        deployment_mode=None,  # type: Optional[str]
        session_status=None,  # type: Optional[str]
        collection=None,  # type: Optional[str]
        package=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.SimulatorSessionSummary"]
        """The deployment_mode appears in the query string. It can be one of
        Unspecified, Testing, or Hosted. If it has a 'neq:' prefix, that means "not;"
        e.g., {.../simulatorSessions?deployment_mode=neq:Hosted} means the response should not include
        simulators that are hosted.

        The session_status can be one of Attachable, Attached, Detaching, Rejected,
        and supports the neq: prefix.

        The collection appears in the query string

        The package appears in the query string

        The filter queries can appear together, like
        {.../simulatorSessions?deployment_mode=Hosted&collection=1234-455-33333}.

        Retrieves all of the simulators currently registered with all
        simulator gateways within this workspace.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param deployment_mode: A specifier to filter on deployment mode.
        :type deployment_mode: str
        :param session_status: A specifier to filter on session status.
        :type session_status: str
        :param collection: If present, only sessions in this collection.
        :type collection: str
        :param package: If present, only sessions in this package.
        :type package: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of SimulatorSessionSummary, or the result of cls(response)
        :rtype: list[~microsoft_bonsai_api.simulator.generated.models.SimulatorSessionSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop(
            "cls", None
        )  # type: ClsType[List["models.SimulatorSessionSummary"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct URL
        url = self.list.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if deployment_mode is not None:
            query_parameters["deployment_mode"] = self._serialize.query(
                "deployment_mode", deployment_mode, "str"
            )
        if session_status is not None:
            query_parameters["session_status"] = self._serialize.query(
                "session_status", session_status, "str"
            )
        if collection is not None:
            query_parameters["collection"] = self._serialize.query(
                "collection", collection, "str"
            )
        if package is not None:
            query_parameters["package"] = self._serialize.query(
                "package", package, "str"
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = "application/json"

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("[SimulatorSessionSummary]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions"}  # type: ignore

    def create(
        self,
        workspace_name,  # type: str
        body,  # type: "models.SimulatorInterface"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SimulatorSessionResponse"
        """Registers a simulator with the Bonsai platform.

        Registers a simulator with the Bonsai platform.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param body: Information and capabilities about the simulator.
        :type body: ~microsoft_bonsai_api.simulator.generated.models.SimulatorInterface
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimulatorSessionResponse, or the result of cls(response)
        :rtype: ~microsoft_bonsai_api.simulator.generated.models.SimulatorSessionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop(
            "cls", None
        )  # type: ClsType["models.SimulatorSessionResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json-patch+json")

        # Construct URL
        url = self.create.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header(
            "content_type", content_type, "str"
        )
        header_parameters["Accept"] = "application/json"

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "SimulatorInterface")
        body_content_kwargs["content"] = body_content
        request = self._client.post(
            url, query_parameters, header_parameters, **body_content_kwargs
        )

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimulatorSessionResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions"}  # type: ignore

    def get(
        self,
        workspace_name,  # type: str
        session_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SimulatorSessionResponse"
        """Retrieves a simulator session corresponding to the sessionId.

        Retrieves a simulator session corresponding to the sessionId.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param session_id: The sessionId of the simulator session to fetch.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SimulatorSessionResponse, or the result of cls(response)
        :rtype: ~microsoft_bonsai_api.simulator.generated.models.SimulatorSessionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop(
            "cls", None
        )  # type: ClsType["models.SimulatorSessionResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct URL
        url = self.get.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
            "sessionId": self._serialize.url("session_id", session_id, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = "application/json"

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("SimulatorSessionResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions/{sessionId}"}  # type: ignore

    def delete(
        self,
        workspace_name,  # type: str
        session_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the Simulator session.

        Deletes the Simulator session.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param session_id: The session ID generated during registration.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct URL
        url = self.delete.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
            "sessionId": self._serialize.url("session_id", session_id, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions/{sessionId}"}  # type: ignore

    def get_most_recent_action(
        self,
        workspace_name,  # type: str
        session_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Event"
        """Gets the most recent action sent to the simulator to process.

        Gets the most recent action sent to the simulator to process.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param session_id: Unique identification of the simulator.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event, or the result of cls(response)
        :rtype: ~microsoft_bonsai_api.simulator.generated.models.Event
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["models.Event"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        # Construct URL
        url = self.get_most_recent_action.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
            "sessionId": self._serialize.url("session_id", session_id, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Accept"] = "application/json"

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_most_recent_action.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions/{sessionId}/action"}  # type: ignore

    def advance(
        self,
        workspace_name,  # type: str
        session_id,  # type: str
        body,  # type: "models.SimulatorState"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Event"
        """Advance the RL agent with the new state of the simulator, and returns an action computed by our policy.
        Simulatorsession is supposed to use the returned action for stepping inside the sim and thne getting the new state.false
        You can send the same state again, as long as you didn't get a Non-Idle Action back.

        Advance the RL agent with the new state of the simulator, and returns an action computed by our
        policy.
        Simulatorsession is supposed to use the returned action for stepping inside the sim and thne
        getting the new state.false
        You can send the same state again, as long as you didn't get a Non-Idle Action back.

        :param workspace_name: The workspace identifier.
        :type workspace_name: str
        :param session_id: Unique identifier for the simulator.
        :type session_id: str
        :param body: The new state of the simulator.
        :type body: ~microsoft_bonsai_api.simulator.generated.models.SimulatorState
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event, or the result of cls(response)
        :rtype: ~microsoft_bonsai_api.simulator.generated.models.Event
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["models.Event"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json-patch+json")

        # Construct URL
        url = self.advance.metadata["url"]  # type: ignore
        path_format_arguments = {
            "workspaceName": self._serialize.url(
                "workspace_name", workspace_name, "str"
            ),
            "sessionId": self._serialize.url("session_id", session_id, "str"),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["Content-Type"] = self._serialize.header(
            "content_type", content_type, "str"
        )
        header_parameters["Accept"] = "application/json"

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, "SimulatorState")
        body_content_kwargs["content"] = body_content
        request = self._client.post(
            url, query_parameters, header_parameters, **body_content_kwargs
        )

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(models.ProblemDetails, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    advance.metadata = {"url": "/v2/workspaces/{workspaceName}/simulatorSessions/{sessionId}/advance"}  # type: ignore
