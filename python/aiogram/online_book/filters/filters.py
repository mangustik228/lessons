from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()
    
class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, cb: CallbackQuery) -> bool:
        return \
            isinstance(cb.data, str) and \
            'del' in cb.data and \
            cb.data[:-3].isdigit()