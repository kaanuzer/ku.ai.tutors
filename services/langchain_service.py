from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from core.config import settings


async def generate_response(prompt: str):
    """
    OpenAI API'sini kullanarak verilen prompt için yanıt üretir.
    """
    try:
        # OpenAI API bağlantısı için ChatOpenAI kullanımı
        chat = ChatOpenAI(
            temperature=0.9,
            openai_api_key=settings.openai_api_key  # API key burada kullanılıyor
        )

        # Prompt ile yanıt oluştur
        response = chat([HumanMessage(content=prompt)])

        return response.content
    except Exception as e:
        # Hata durumunda hata mesajı döndür
        raise RuntimeError(f"LangChain error: {str(e)}")

