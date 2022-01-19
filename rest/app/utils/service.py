from typing import Optional, Union, Any
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from .config import config

import traceback


class ServiceResult:
    exception: Optional[Exception] = None
    error_message: Optional[str] = None
    success: bool = True
    value: dict

    def set_err_description(self, msg: str):
        self.error_message = msg
        self.success = False

    def set_exception(self, e: Exception):
        self.exception = e
        self.success = False

    def set_success(self, is_success: bool):
        self.success = is_success

    def set_value(self, value: dict):
        self.value = value

    def __enter__(self):
        return self.value


def handle_result(result: Union[ServiceResult, Any]):
    if not isinstance(result, ServiceResult):
        return result

    if not result.success:
        e = result.exception
        fmt_tcback = traceback.format_exception(type(e), e, e.__traceback__)

        print("".join(fmt_tcback))

        resp = {
            "description": result.error_message
            if result.error_message
            else "Internal Server Error"
        }
        if config.debug:
            resp["debug"] = {
                "traceback": fmt_tcback,
                "exception": type(e).__module__ + "." + type(e).__qualname__,
            }

        return JSONResponse(
            content=resp,
            status_code=e.status_code if isinstance(e, HTTPException) else 500,
        )
    return result.value
