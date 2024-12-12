# error_utils.py

class ErrorUtils:
    class CustomError(Exception):
        """自定义错误基类"""
        pass

    class ErrorA(CustomError):
        """错误A的具体信息"""
        pass

    class ErrorB(CustomError):
        """错误B的具体信息"""
        pass

    # ... 其他自定义错误类

    @staticmethod
    def raise_error_a(message="默认错误信息A"):
        raise ErrorUtils.ErrorA(message)

    @staticmethod
    def raise_error_b(message="默认错误信息B"):
        raise ErrorUtils.ErrorB(message)

    # ... 其他抛出错误的方法
