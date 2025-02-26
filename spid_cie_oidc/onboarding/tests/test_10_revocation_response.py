from django.test import TestCase
from pydantic import ValidationError
from spid_cie_oidc.onboarding.tests.revocation_response_settings import (
    REVOCATION_RESPONSE_CIE,
    REVOCATION_RESPONSE_CIE_NO_CORRECT_ERROR,
    REVOCATION_RESPONSE_CIE_NO_CORRECT_ERROR_DESCRIPTION,
    REVOCATION_RESPONSE_CIE_NO_ERROR,
    REVOCATION_RESPONSE_CIE_NO_ERROR_DESCRIPTION,
)
from spid_cie_oidc.onboarding.schemas.revocation_response import (
    RevocationErrorResponseCie,
)


class RevocationResponseTest(TestCase):
    def test_validate_revocation_response(self):
        RevocationErrorResponseCie(**REVOCATION_RESPONSE_CIE)

    def test_validate_revocation_response_no_error(self):
        with self.assertRaises(ValidationError):
            RevocationErrorResponseCie(**REVOCATION_RESPONSE_CIE_NO_ERROR)

    def test_validate_revocation_response_no_correct_error(self):
        with self.assertRaises(ValidationError):
            RevocationErrorResponseCie(**REVOCATION_RESPONSE_CIE_NO_CORRECT_ERROR)

    def test_validate_revocation_response_no_error_description(self):
        with self.assertRaises(ValidationError):
            RevocationErrorResponseCie(**REVOCATION_RESPONSE_CIE_NO_ERROR_DESCRIPTION)

    def test_validate_revocation_response_no_correct_error_description(self):
        with self.assertRaises(ValidationError):
            RevocationErrorResponseCie(
                **REVOCATION_RESPONSE_CIE_NO_CORRECT_ERROR_DESCRIPTION
            )
