from pydantic_settings import BaseSettings
import warnings
from fastapiMpesa.api.b2c import B2C
from fastapiMpesa.api.c2b import C2B
from fastapiMpesa.api.b2b import B2B
from fastapiMpesa.api.balance import Balance
from fastapiMpesa.api.mpesa_express import MpesaExpress
from fastapiMpesa.api.reversal import Reversal
from fastapiMpesa.api.transaction_status import TransactionStatus


class Settings(BaseSettings):
    MPESA_API_ENVIRONMENT: str
    MPESA_API_KEY: str
    MPESA_API_SECRET: str


class MpesaAPI(object):

    def __init__(self, settings: Settings | None = None, **kwargs):
        self.settings = settings
        self.sandbox_url = "https://sandbox.safaricom.co.ke"
        self.live_url = "https://api.safaricom.co.ke"

        if settings:
            self.init_app(settings)
        else:
            warnings.warn(
                "Please pass the FastAPI settings object into MpesaApi class instance")

    def init_app(self, settings: Settings):
        if not settings.MPESA_API_KEY:
            warnings.warn(
                'APP_KEY is not set')
        if not settings.MPESA_API_SECRET:
            warnings.warn(
                'APP_SECRET is not set')
        if not settings.MPESA_API_ENVIRONMENT:
            warnings.warn(
                'API_ENVIRONMENT is not set')

    def get_credentials(self):
        """Helper method to return app_key, app_secret and api_environmentfrom the app's app.settings."""
        api_env = self.settings.MPESA_API_ENVIRONMENT
        app_key = self.settings.MPESA_API_KEY
        app_secret = self.settings.MPESA_API_SECRET
        return api_env, app_key, app_secret

    @property
    def C2B(self):
        """Method returns a C2B Object"""
        env, app_key, app_secret = self.get_credentials()
        return C2B(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def B2C(self):
        """Method returns a B2C Object"""
        env, app_key, app_secret = self.get_credentials()
        return B2C(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def B2B(self):
        """Method returns a B2B Object"""
        env, app_key, app_secret = self.get_credentials()
        return B2B(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def Balance(self):
        """Method returns a Balance Object"""
        env, app_key, app_secret = self.get_credentials()
        return Balance(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def MpesaExpress(self):
        """Method returns a MpesaExpress Object"""
        env, app_key, app_secret = self.get_credentials()
        return MpesaExpress(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def Reversal(self):
        """Method returns a Reversal Object"""
        env, app_key, app_secret = self.get_credentials()
        return Reversal(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def TransactionStatus(self):
        """Method returns a TransactionSatus Object"""
        env, app_key, app_secret = self.get_credentials()
        return TransactionStatus(env, app_key, app_secret, self.sandbox_url, self.live_url)
