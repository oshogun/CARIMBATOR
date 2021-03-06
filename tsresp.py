from pyasn1.type import (
    univ,
    namedtype,
    namedval,
    tag
)

from pyasn1_modules.rfc2459 import Extensions


class TimeStampResp(univ.Sequence):
    componentType = namedType.NamedTypes(
        namedtype.NamedType("status", PKIStatusInfo())
        namedtype.OptionalNamedType("timeStampToken", TimeStampToken())
    )

