from typing import Optional
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam, ChatCompletionToolMessageParam, ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam, ChatCompletionFunctionMessageParam, ChatCompletionAssistantMessageParam
import tiktoken
from openai_layer.usage.model import UsageTokenModel


class UsageUtils:
    @staticmethod
    async def token(message: str, model_name: Optional[str]) -> int:
        enc = tiktoken.encoding_name_for_model(
            model_name) if model_name != None else tiktoken.get_encoding("cl100k_base")
        value = len(enc.encode(message))
        return value

    @staticmethod
    async def messageTokenModel(message: str, model_name: Optional[str]) -> UsageTokenModel:
        token = UsageUtils.token(message=message, model_name=model_name)
        return UsageTokenModel(message, token)

    @staticmethod
    def tokenFromModel(message: ChatCompletionMessageParam, model_name: Optional[str], token: Optional[int] = None) -> UsageTokenModel:
        if isinstance(message, ChatCompletionToolMessageParam):
            return UsageUtils.tokenFromToolModel(message, model_name, token)
        elif isinstance(message, ChatCompletionSystemMessageParam):
            return UsageUtils.tokenFromSystemModel(message, model_name, token)
        elif isinstance(message, ChatCompletionAssistantMessageParam):
            return UsageUtils.tokenFromAssistantModel(message, model_name, token)
        elif isinstance(message, ChatCompletionUserMessageParam):
            return UsageUtils.tokenFromUserModel(message, model_name, token)
        elif isinstance(message, ChatCompletionFunctionMessageParam):
            return UsageUtils.tokenFromFunctionModel(message, model_name, token)
        else:
            raise Exception("Unknown params model type")

    @staticmethod
    def tokenFromToolModel(message: ChatCompletionToolMessageParam, model_name: Optional[str], token: Optional[int]) -> UsageTokenModel:
        if (token is None):
            raise Exception("tools message must input token")
        return UsageTokenModel("~tools_message~", token)

    @staticmethod
    def tokenFromSystemModel(message: ChatCompletionSystemMessageParam, model_name: Optional[str], token: Optional[int]) -> UsageTokenModel:
        message_content = message.content
        if (model_name):
            raise Exception("model can't be empty")
        tokenValue = token if token != None else UsageUtils.token(
            message=message_content, model_name=model_name)
        return UsageTokenModel(message.content, token=tokenValue)

    @staticmethod
    def tokenFromAssistantModel(message: ChatCompletionAssistantMessageParam, model_name: Optional[str], token: Optional[int]) -> UsageTokenModel:
        if (token is None):
            raise Exception("tools message must input token")
        return UsageTokenModel("~assistant_message~", token)

    @staticmethod
    def tokenFromUserModel(message: ChatCompletionUserMessageParam, model_name: Optional[str], token: Optional[int]) -> UsageTokenModel:
        message_content = message.content
        if (model_name):
            raise Exception("model can't be empty")
        tokenValue = token if token != None else UsageUtils.token(
            message=message_content, model_name=model_name)
        return UsageTokenModel(message.content, token=tokenValue)

    @staticmethod
    def tokenFromFunctionModel(message: ChatCompletionFunctionMessageParam, model_name: Optional[str], token: Optional[int]) -> UsageTokenModel:
        if (token is None):
            raise Exception("tools message must input token")
        return UsageTokenModel("~function_message~", token)
