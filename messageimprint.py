from pyasn1.type import (
    univ,
    namedtype,
    namedval,
    tag
)

from pyasn1_modules.rfc2459 import Extensions

class MessageImprint(univ.Sequence):
    componentType = namedType.NamedTypes(
        namedtype.NamedType('hashAlgorithm', AlgorithmIdentifier()),
        namedtype.NamedType('hashedMessage', univ.OctetString())
    )