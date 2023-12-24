import typing


class MoySkladError(Exception):
    def __init__(
        self,
        json_error: dict,
        requested_json: typing.Optional[str] = None,
    ):
        self.error = json_error.get("error", "Unknown error")
        self.code = json_error.get("code", "Unknown code")
        self.more_info = json_error.get("moreInfo", "No link to more info")
        self.line = json_error.get("line")
        self.column = json_error.get("column")
        self.requested_json = requested_json
        self.message = (
            f"Error: {self.error} (Code {self.code})\n" f"More info: {self.more_info}\n"
        )
        if self.line and self.column:
            self.message += f"Error at line {self.line}, column {self.column}\n"

            # line and column are 1-indexed, but we need 0-indexed
            # (Строка и столбец индексируются с 1, но нам нужен 0-индекс)
            self.line -= 1
            self.column -= 1

            if self.requested_json:
                if self.requested_json.count("\n") == 0:
                    # show +-10 characters around the error, and highlight it using ^^^ under it
                    line_with_error = self.requested_json.splitlines()[self.line]
                    error_position = self.column
                    # remove all but the first 10 characters before the error and the last 10 after it
                    line_with_error = (
                        line_with_error[max(0, error_position - 10) : error_position]
                        + line_with_error[error_position : error_position + 10]
                    )
                    error_position -= max(0, error_position - 10)
                    self.message += f"Error in:\n{line_with_error}\n"
                    self.message += " " * error_position + "^^^\n"
                else:
                    # show +- 3 lines around the error, add ^ below the error
                    lines = self.requested_json.splitlines()
                    for i in range(self.line - 4, self.line + 4):
                        if i < 0:
                            continue
                        if i >= len(lines):
                            break
                        self.message += f"{lines[i]}\n"
                        if i == self.line:
                            self.message += " " * (self.column - 3) + "^^^^^^^\n"

    def __str__(self):
        return self.message
