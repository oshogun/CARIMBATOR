from pyasn1.type import (
    univ,
    namedtype,
    namedval,
    tag
)

from pyasn1_modules.rfc2459 import Extensions

from messageimprint import MessageImprint

class TsaPolicyId(univ.ObjectIdentifier):
    componentType = namedtype.NamedTypes(
        
    )
   

class TimeStampReq(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer().subtype(
            namedValues=namedval.NamedValues(('v1',1))
        )),
        namedtype.NamedType('messageImprint', MessageImprint()),
        namedtype.OptionalNamedType('reqPolicy', TsaPolicyId()),
     
        namedtype.OptionalNamedType('nonce', univ.Integer()),
        namedtype.OptionalNamedType('certReq', univ.Boolean(False)),
        # extensions defined in rfc 2459
        namedtype.OptionalNamedType('extensions', Extensions().subtype(
            implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)
        ))
    )

