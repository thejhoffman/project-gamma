import os
from fastapi import Depends, APIRouter
from jwtdown_fastapi.authentication import Authenticator, Token
from queries.accounts import AccountQueries, AccountOut, AccountOutWithPassword


class ExampleAuthenticator(Authenticator):
    @property  # override router property in order to set custom tag
    def router(self):
        if self._router is None:
            router = APIRouter(tags=["Accounts"])
            router.post(f"/{self.path}", response_model=Token)(self.login)
            router.delete(f"/{self.path}", response_model=bool)(self.logout)
            self._router = router
        return self._router

    async def get_account_data(
        self,
        email: str,  # you can also call this email based on what your project is
        accounts: AccountQueries,
    ):
        # Use your repo to get the account based on the
        # email (which could be an email)
        return accounts.get(
            email
        )  # change to email if using email instead of email

    def get_account_getter(
        self,
        accounts: AccountQueries = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):
        # Return the email and the data for the cookie.
        # You must return TWO values from this method.
        return account.email, AccountOut(**account.dict())


authenticator = ExampleAuthenticator(os.environ["SIGNING_KEY"])
