Register: __log__({ign: bytes <= 32, addr: address})
Update: __log__({ign: bytes <= 32, oldAddr: address, newAddr: address})

owner: address

# -------------------------------------------
# ---------- State Variables ----------------
# -------------------------------------------

# Represents the IGN associated to an address
names: public((bytes <= 32)[address])
# Represents the address associated to an IGN
addresses: public(address[bytes <= 32])

# -------------------------------------------
# -------------- Internal -------------------
# -------------------------------------------

@public
def __init__ ():
    self.owner = msg.sender

@public
def _tag (addr: address, ign: bytes <= 26) -> bytes <= 32:
    # Creates a tagged IGN for example Matt#ef25d
    bytesAddr = concat('', sha3(as_bytes32(addr)))
    addrHash = slice(bytesAddr, start=0, len=5)
    return concat(ign, "#", addrHash)

# -------------------------------------------
# -------------- Getters --------------------
# -------------------------------------------

@public
def getAddress (ign: bytes <= 32) -> address:
    # Return the address of an IGN
    return self.addresses[ign]

# -------------------------------------------
# -------------- External -------------------
# -------------------------------------------

@public
def register (ign: bytes <= 26):
    # If address is not already registered to an IGN register it
    assert len(self.names[msg.sender]) == 0
    # Tag the username to mitigate duplicate usernames
    taggedName = self._tag(msg.sender, ign)
    # Ensure this name tag combination is not already registered
    assert as_bytes32(self.addresses[taggedName]) == as_bytes32(0)
    # Set username assignment
    self.names[msg.sender] = taggedName
    self.addresses[taggedName] = msg.sender
    
    log.Register(taggedName, msg.sender)

@public
def changeAddress (newAddress: address):
    # Expect sender to have an IGN registered
    assert len(self.names[msg.sender]) > 0
    # Expect new address not to be registered already
    assert len(self.names[msg.sender]) == 0
    # Get current IGN
    ign = self.names[msg.sender]
    # Change address associated to IGN
    self.addresses[ign] = newAddress
    # Change name associated to address
    self.names[newAddress] = ign
    # Remove old address registration
    self.names[msg.sender] = None
    
    log.Update(ign, msg.sender, newAddress)
