#!/usr/bin/python3


from typing import Any
from abc import ABC, abstractmethod


class DataProcessorError(Exception):
    def __init__(self, msg: str = "Unknown DataProcessor error.") -> None:
        print(msg)


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[Any] = []
        self._rank = 0
        super().__init__()

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self._data != []:
            self._rank += 1
            return (self._rank - 1, str(self._data.pop(0)))
        else:
            return (-1, "")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: (int | float | list[(int | float)])) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                self._data.append(data)
            elif isinstance(data, list):
                self._data.extend(data)
        else:
            raise DataProcessorError(" Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: (str | list[str])) -> None:
        if self.validate(data):
            if isinstance(data, (str)):
                self._data.append(data)
            elif isinstance(data, list):
                self._data.extend(data)
        else:
            raise DataProcessorError(" Got exception: Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def _validate_log(self, log: Any) -> bool:
        if isinstance(log, dict):
            if (isinstance(list(log.keys())[0], str)
                    and isinstance(list(log.keys())[1], str)
                    and isinstance(list(log.values())[0], str)
                    and isinstance(list(log.values())[1], str)
                    and list(log.keys())[0] == "log_level"
                    and list(log.keys())[1] == "log_message"
                    and len(log) == 2):
                return True
        return False

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._validate_log(data)
        elif isinstance(data, list):
            for item in data:
                if not self._validate_log(item):
                    return False
            return True
        return False

    def ingest(self, data: (dict[str, str] | list[dict[str, str]])) -> None:
        if self.validate(data):
            if isinstance(data, dict):
                self._data.append(f"{data['log_level']}: "
                                  f"{data['log_message']}")
            elif isinstance(data, list):
                for item in data:
                    self._data.append(f"{item['log_level']}: "
                                      f"{item['log_message']}")
        else:
            raise DataProcessorError(" Got exception: Improper log data")


def data_test(type: str, output_qty: int = 0) -> None:
    if type == "numeric":
        dp: DataProcessor = NumericProcessor()
        new_data: list[Any] = [1, 2, 3, 4, 5]
        output_text = "Numeric value"
    elif type == "text":
        dp = TextProcessor()
        new_data = ['Hello', 'Nexus', 'World']
        output_text = "Text value"
    elif type == "log":
        dp = LogProcessor()
        new_data = [{'log_level': 'NOTICE',
                     'log_message': 'Connection to server'},
                    {'log_level': 'ERROR',
                     'log_message': 'Unauthorized access!!'}]
        output_text = "Log entry"
    else:
        raise DataProcessorError("Testing Unknown DataProcessor Type")
    print(f" Trying to validate input '42': {dp.validate(42)}")
    print(f" Trying to validate input 'Hello': {dp.validate('Hello')}")
    print(f" Trying to validate input '3.1416': {dp.validate(3.1416)}")
    print(" Trying to validate input '[1, 2.0, 3, 4.0]': "
          f"{dp.validate([1, 2.0, 3, 4.0])}")
    print(" Trying to validate input '['A', 'b', 'C', 'd']': "
          f"{dp.validate(['A', 'b', 'C', 'd'])}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        dp.ingest("foo")
        print(" Valid ingest() call. Emptying DataProcessor ...")
        dp.output()
    except DataProcessorError:
        pass
    print(f" Processing Data: {new_data}")
    if dp.validate(new_data):
        dp.ingest(new_data)
    print(f" Extracting {output_qty} values...")
    for _ in range(output_qty):
        output = dp.output()
        print(f" {output_text} {output[0]}: {output[1]}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    data_test("numeric", 3)
    print("\nTesting Text Processor...")
    data_test("text", 1)
    print("\nTesting Log Processor...")
    data_test("log", 2)
    print()
