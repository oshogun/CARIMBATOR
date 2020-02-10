from pyasn1.type import (
    univ,
    namedtype,
    namedval,
    tag
)

from pyasn1_modules.rfc2459 import Extensions

class PKIStatus(univ.Integer):
    componentType = namedtype.NamedTypes (
        namedtype.NamedType('granted', univ.Integer(0)),
            # when the PKIStatus contains the value zero a TimeStampToken, as
            # requested, is present.
        namedtype.NamedType('grantedWithMods', univ.Integer(1)),
            # when the PKIStatus contains the value one a TimeStampToken,
            # with modifications, is present.
        namedtype.NamedType('rejection', univ.Integer(2)),
        namedtype.NamedType('waiting', univ.Integer(3)),
        namedtype.NamedType('revocationWarning', univ.Integer(4))
    )

class PKIFailureInfo(univ.BitString):
    componentType = namedtype.NamedTypes (
        namedtype.NamedType('badAlg', univ.Integer(0)),
            # unrecognized or unsupported Algorithm Identifier
        namedtype.NamedType('badRequest', univ.Integer(2)),
            # transaction not permitted or supported
        namedtype.NamedType('badDataFormat', univ.Integer(5)),
            # the data submitted has the wrong format
        namedtype.NamedType('timeNotAvailable', univ.Integer(14)),
            # the TSA's time source is not available
        namedtype.NamedType('unacceptedPolicy', univ.Integer(15)),
            # the requested TSA policy is not supported by the TSA
        namedtype.NamedType('unacceptedExtension', univ.Integer(16)),
            # the requested extension is not supported by the TSA
        namedtype.NamedType('addInfoNotAvailable', univ.Integer(17)),
            # the additional information requested could not be understood
            # or is not available
        namedtype.NamedType('systemFailure', univ.Integer(25))
            # the request cannot be handled due to system failure


    )

class PKIStatusInfo(univ.Sequence):
    componentType = namedtype.NamedTypes (
        namedtype.NamedType('status', PKIStatus()),
        namedtype.OptionalNamedType('statusString', PKIFreeText()),
        namedtype.OptionalNamedType('failInfo', PKIFailureInfo())
    )