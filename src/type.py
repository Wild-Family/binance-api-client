import dataclasses
import os


@dataclasses.dataclass
class Failure:
    message: str
    exception: Exception = Exception()

    def exit(self) -> None:
        print("exit: ", self.message, self.exception)
        os.sys.exit(1)

    def print_message(self) -> None:
        print("message: ", self.message, self.exception)
