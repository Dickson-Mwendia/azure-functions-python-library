#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
import unittest

from azure.functions import DataType
from azure.functions.decorators import Cardinality
from azure.functions.decorators.core import BindingDirection
from azure.functions.decorators.eventhub import EventHubTrigger, EventHubOutput


class TestEventHub(unittest.TestCase):
    def test_event_hub_trigger_valid_creation(self):
        trigger = EventHubTrigger(name="req",
                                  connection="dummy_connection",
                                  event_hub_name="dummy_event_hub",
                                  cardinality=Cardinality.ONE,
                                  consumer_group="dummy_group",
                                  data_type=DataType.UNDEFINED)

        self.assertEqual(trigger.get_binding_name(), "eventHubTrigger")
        self.assertEqual(trigger.get_dict_repr(),
                         {"cardinality": str(Cardinality.ONE),
                          "connection": "dummy_connection",
                          "consumerGroup": "dummy_group",
                          "dataType": str(DataType.UNDEFINED),
                          "direction": str(BindingDirection.IN),
                          "eventHubName": "dummy_event_hub",
                          "name": "req",
                          "type": "eventHubTrigger"})

    def test_event_hub_output_valid_creation(self):
        output = EventHubOutput(name="res",
                                event_hub_name="dummy_event_hub",
                                connection="dummy_connection",
                                data_type=DataType.UNDEFINED)

        self.assertEqual(output.get_binding_name(), "eventHub")
        self.assertEqual(output.get_dict_repr(),
                         {'connection': 'dummy_connection',
                          'dataType': str(DataType.UNDEFINED),
                          'direction': str(BindingDirection.OUT),
                          'eventHubName': 'dummy_event_hub',
                          'name': 'res',
                          'type': 'eventHub'})