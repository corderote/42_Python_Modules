#!/usr/bin/python3


from typing import Any
from abc import ABC, abstractmethod


class DataProcessorError(Exception):
    def __init__(self, msg: str = "Unknown DataProcessor error.") -> None:
        print(msg)


class DataStreamError(Exception):
    def __init__(self, msg: str = "Unknown DataStream error.") -> None:
        print(msg)


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
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
    def __init__(self):
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
        if self.validate(data) == True:
            if isinstance(data, (int, float)):
                self._data.append(data)
            elif isinstance(data, list):
                self._data.extend(data)
        else:
            raise DataProcessorError(" Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
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
        if self.validate(data) == True:
            if isinstance(data, (str)):
                self._data.append(data)
            elif isinstance(data, list):
                self._data.extend(data)
        else:
            raise DataProcessorError(" Got exception: Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
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

    def ingest(self, data: (dict[str:str] | list[dict[str:str]])) -> None:
        if self.validate(data) == True:
            if isinstance(data, dict):
                self._data.append(f"{data["log_level"]}: {data["log_message"]}")
            elif isinstance(data, list):
                for item in data:
                    self._data.append(f"{item["log_level"]}: {item["log_message"]}")
        else:
            raise DataProcessorError(" Got exception: Improper log data")


class DataStream():
    def __init__(self):
        self.procs = []
        super().__init__()

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            self.procs.append(proc)
        
    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            try: 
                valid = False
                for proc in self.procs:
                    if proc.validate(item):
                        proc.ingest(item)
                        valid = True
                if valid == False:
                    raise DataStreamError("DataStream error - "
                                          "Can't process element in stream: "
                                          f"{item}")
            except DataStreamError:
                pass
        
    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if len(self.procs) == 0:
            print("No processor found, no data.")
        else:
            for proc in self.procs:
                print(f"{proc.__class__.__name__}: "
                      f"total {len(proc._data) + proc._rank} items processed, "
                      f"remaining {len(proc._data)} on processor.")
                
    def consume_elements(self, type: str, qty: int):
        for proc in self.procs:
            if type == "n" and isinstance(proc, NumericProcessor):
                for _ in range(qty):
                    proc.output()
            if type == "t" and isinstance(proc, TextProcessor):
                for _ in range(qty):
                    proc.output()
            if type == "l" and isinstance(proc, LogProcessor):
                for _ in range(qty):
                    proc.output()
    

if __name__ == "__main__":
    ds = DataStream()
    data = [
            'Hello world', 
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
            'log_message': 'User wil isconnected'}],
            42,
            ['Hi', 'five']]
    
    print("=== Code Nexus - Data Stream ===")
    print()
    ds.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    ds.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {data}")
    ds.process_stream(data)
    ds.print_processors_stats()
    print("\nRegistering other data procesors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())
    print("Send the same batch again")
    ds.process_stream(data)
    ds.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    ds.consume_elements("n", 3)
    ds.consume_elements("t", 2)
    ds.consume_elements("l", 1)
    ds.print_processors_stats()
    print()
