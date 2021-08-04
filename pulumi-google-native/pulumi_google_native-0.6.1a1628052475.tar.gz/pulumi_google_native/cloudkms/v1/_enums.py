# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuditLogConfigLogType',
    'CryptoKeyPurpose',
    'CryptoKeyVersionState',
    'CryptoKeyVersionTemplateAlgorithm',
    'CryptoKeyVersionTemplateProtectionLevel',
    'ImportJobImportMethod',
    'ImportJobProtectionLevel',
]


class AuditLogConfigLogType(str, Enum):
    """
    The log type that this config enables.
    """
    LOG_TYPE_UNSPECIFIED = "LOG_TYPE_UNSPECIFIED"
    """Default case. Should never be this."""
    ADMIN_READ = "ADMIN_READ"
    """Admin reads. Example: CloudIAM getIamPolicy"""
    DATA_WRITE = "DATA_WRITE"
    """Data writes. Example: CloudSQL Users create"""
    DATA_READ = "DATA_READ"
    """Data reads. Example: CloudSQL Users list"""


class CryptoKeyPurpose(str, Enum):
    """
    Immutable. The immutable purpose of this CryptoKey.
    """
    CRYPTO_KEY_PURPOSE_UNSPECIFIED = "CRYPTO_KEY_PURPOSE_UNSPECIFIED"
    """Not specified."""
    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"
    """CryptoKeys with this purpose may be used with Encrypt and Decrypt."""
    ASYMMETRIC_SIGN = "ASYMMETRIC_SIGN"
    """CryptoKeys with this purpose may be used with AsymmetricSign and GetPublicKey."""
    ASYMMETRIC_DECRYPT = "ASYMMETRIC_DECRYPT"
    """CryptoKeys with this purpose may be used with AsymmetricDecrypt and GetPublicKey."""


class CryptoKeyVersionState(str, Enum):
    """
    The current state of the CryptoKeyVersion.
    """
    CRYPTO_KEY_VERSION_STATE_UNSPECIFIED = "CRYPTO_KEY_VERSION_STATE_UNSPECIFIED"
    """Not specified."""
    PENDING_GENERATION = "PENDING_GENERATION"
    """This version is still being generated. It may not be used, enabled, disabled, or destroyed yet. Cloud KMS will automatically mark this version ENABLED as soon as the version is ready."""
    ENABLED = "ENABLED"
    """This version may be used for cryptographic operations."""
    DISABLED = "DISABLED"
    """This version may not be used, but the key material is still available, and the version can be placed back into the ENABLED state."""
    DESTROYED = "DESTROYED"
    """This version is destroyed, and the key material is no longer stored."""
    DESTROY_SCHEDULED = "DESTROY_SCHEDULED"
    """This version is scheduled for destruction, and will be destroyed soon. Call RestoreCryptoKeyVersion to put it back into the DISABLED state."""
    PENDING_IMPORT = "PENDING_IMPORT"
    """This version is still being imported. It may not be used, enabled, disabled, or destroyed yet. Cloud KMS will automatically mark this version ENABLED as soon as the version is ready."""
    IMPORT_FAILED = "IMPORT_FAILED"
    """This version was not imported successfully. It may not be used, enabled, disabled, or destroyed. The submitted key material has been discarded. Additional details can be found in CryptoKeyVersion.import_failure_reason."""


class CryptoKeyVersionTemplateAlgorithm(str, Enum):
    """
    Required. Algorithm to use when creating a CryptoKeyVersion based on this template. For backwards compatibility, GOOGLE_SYMMETRIC_ENCRYPTION is implied if both this field is omitted and CryptoKey.purpose is ENCRYPT_DECRYPT.
    """
    CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED = "CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED"
    """Not specified."""
    GOOGLE_SYMMETRIC_ENCRYPTION = "GOOGLE_SYMMETRIC_ENCRYPTION"
    """Creates symmetric encryption keys."""
    RSA_SIGN_PSS2048_SHA256 = "RSA_SIGN_PSS_2048_SHA256"
    """RSASSA-PSS 2048 bit key with a SHA256 digest."""
    RSA_SIGN_PSS3072_SHA256 = "RSA_SIGN_PSS_3072_SHA256"
    """RSASSA-PSS 3072 bit key with a SHA256 digest."""
    RSA_SIGN_PSS4096_SHA256 = "RSA_SIGN_PSS_4096_SHA256"
    """RSASSA-PSS 4096 bit key with a SHA256 digest."""
    RSA_SIGN_PSS4096_SHA512 = "RSA_SIGN_PSS_4096_SHA512"
    """RSASSA-PSS 4096 bit key with a SHA512 digest."""
    RSA_SIGN_PKCS12048_SHA256 = "RSA_SIGN_PKCS1_2048_SHA256"
    """RSASSA-PKCS1-v1_5 with a 2048 bit key and a SHA256 digest."""
    RSA_SIGN_PKCS13072_SHA256 = "RSA_SIGN_PKCS1_3072_SHA256"
    """RSASSA-PKCS1-v1_5 with a 3072 bit key and a SHA256 digest."""
    RSA_SIGN_PKCS14096_SHA256 = "RSA_SIGN_PKCS1_4096_SHA256"
    """RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA256 digest."""
    RSA_SIGN_PKCS14096_SHA512 = "RSA_SIGN_PKCS1_4096_SHA512"
    """RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA512 digest."""
    RSA_DECRYPT_OAEP2048_SHA256 = "RSA_DECRYPT_OAEP_2048_SHA256"
    """RSAES-OAEP 2048 bit key with a SHA256 digest."""
    RSA_DECRYPT_OAEP3072_SHA256 = "RSA_DECRYPT_OAEP_3072_SHA256"
    """RSAES-OAEP 3072 bit key with a SHA256 digest."""
    RSA_DECRYPT_OAEP4096_SHA256 = "RSA_DECRYPT_OAEP_4096_SHA256"
    """RSAES-OAEP 4096 bit key with a SHA256 digest."""
    RSA_DECRYPT_OAEP4096_SHA512 = "RSA_DECRYPT_OAEP_4096_SHA512"
    """RSAES-OAEP 4096 bit key with a SHA512 digest."""
    EC_SIGN_P256_SHA256 = "EC_SIGN_P256_SHA256"
    """ECDSA on the NIST P-256 curve with a SHA256 digest."""
    EC_SIGN_P384_SHA384 = "EC_SIGN_P384_SHA384"
    """ECDSA on the NIST P-384 curve with a SHA384 digest."""
    EC_SIGN_SECP256K1_SHA256 = "EC_SIGN_SECP256K1_SHA256"
    """ECDSA on the non-NIST secp256k1 curve. This curve is only supported for HSM protection level."""
    EXTERNAL_SYMMETRIC_ENCRYPTION = "EXTERNAL_SYMMETRIC_ENCRYPTION"
    """Algorithm representing symmetric encryption by an external key manager."""


class CryptoKeyVersionTemplateProtectionLevel(str, Enum):
    """
    ProtectionLevel to use when creating a CryptoKeyVersion based on this template. Immutable. Defaults to SOFTWARE.
    """
    PROTECTION_LEVEL_UNSPECIFIED = "PROTECTION_LEVEL_UNSPECIFIED"
    """Not specified."""
    SOFTWARE = "SOFTWARE"
    """Crypto operations are performed in software."""
    HSM = "HSM"
    """Crypto operations are performed in a Hardware Security Module."""
    EXTERNAL = "EXTERNAL"
    """Crypto operations are performed by an external key manager."""


class ImportJobImportMethod(str, Enum):
    """
    Required. Immutable. The wrapping method to be used for incoming key material.
    """
    IMPORT_METHOD_UNSPECIFIED = "IMPORT_METHOD_UNSPECIFIED"
    """Not specified."""
    RSA_OAEP3072_SHA1_AES256 = "RSA_OAEP_3072_SHA1_AES_256"
    """This ImportMethod represents the CKM_RSA_AES_KEY_WRAP key wrapping scheme defined in the PKCS #11 standard. In summary, this involves wrapping the raw key with an ephemeral AES key, and wrapping the ephemeral AES key with a 3072 bit RSA key. For more details, see [RSA AES key wrap mechanism](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc408226908)."""
    RSA_OAEP4096_SHA1_AES256 = "RSA_OAEP_4096_SHA1_AES_256"
    """This ImportMethod represents the CKM_RSA_AES_KEY_WRAP key wrapping scheme defined in the PKCS #11 standard. In summary, this involves wrapping the raw key with an ephemeral AES key, and wrapping the ephemeral AES key with a 4096 bit RSA key. For more details, see [RSA AES key wrap mechanism](http://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc408226908)."""


class ImportJobProtectionLevel(str, Enum):
    """
    Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into.
    """
    PROTECTION_LEVEL_UNSPECIFIED = "PROTECTION_LEVEL_UNSPECIFIED"
    """Not specified."""
    SOFTWARE = "SOFTWARE"
    """Crypto operations are performed in software."""
    HSM = "HSM"
    """Crypto operations are performed in a Hardware Security Module."""
    EXTERNAL = "EXTERNAL"
    """Crypto operations are performed by an external key manager."""
