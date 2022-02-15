# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from typing import Tuple, Optional, Dict

from azure.functions.decorators.core import AuthLevel, Trigger, \
    OutputBinding, DataType, HttpMethod


class HttpTrigger(Trigger):
    @staticmethod
    def get_binding_name() -> str:
        return "httpTrigger"

    def __init__(self,
                 name,
                 methods: Tuple[HttpMethod, ...],
                 data_type: DataType,
                 auth_level: AuthLevel,
                 route: Optional[str] = None) -> None:
        self._auth_level = auth_level
        self._methods = methods
        self._route = route
        super().__init__(name=name, data_type=data_type)

    def get_dict_repr(self) -> Dict:
        dict_repr: Dict = {
            "authLevel": str(self.auth_level.value),
            "type": self.type,
            "direction": self._direction.name,
            "name": self.name,
            "dataType": self._data_type.name,
            "route": self.route
        }
        if self._methods is not None:
            dict_repr["methods"] = [str(m) for m in self.methods]

        return dict_repr

    @property
    def auth_level(self) -> AuthLevel:
        return self._auth_level

    @auth_level.setter
    def auth_level(self,
                   auth_level: AuthLevel) -> None:
        self._auth_level = auth_level

    @property
    def route(self) -> Optional[str]:
        return self._route

    @route.setter
    def route(self,
              route: str) -> None:
        self._route = route

    @property
    def methods(self) -> Tuple[HttpMethod, ...]:
        return self._methods

    @methods.setter
    def methods(self,
                methods: Tuple[HttpMethod, ...]) -> None:
        self._methods = methods


class HttpOutput(OutputBinding):
    @staticmethod
    def get_binding_name() -> str:
        return "http"

    def __init__(self,
                 name: str,
                 data_type: DataType) -> None:
        super().__init__(name=name, data_type=data_type)

    def get_dict_repr(self) -> Dict:
        return {
            "type": self.type,
            "direction": self._direction.name,
            "name": self.name,
            "dataType": self._data_type.name
        }